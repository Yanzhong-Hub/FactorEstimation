"""
Handle factor signal

- query raw data
- process to factor signals
- save factor signals

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

import pandas as pd


class FactorSignal:
    """
    Factor signal object
    """

    def __init__(self, name, raw_con):
        """

        :param name: factor name, such as 'bm', 'q_roe'
        :param raw_con: raw data connection
        """
        self.name = name  # factor name
        self.raw_con = raw_con  # sql setting

    def query_fundamental_data(self, ts_code, account_name, sheet_name):
        return query_fundamentals(yz_sql=self.raw_con, ts_code=ts_code,
                                  account_name=account_name, sheet_name=sheet_name)


class FactorSignalProcess(FactorSignal):

    def __init__(self, name, raw_con, trade_cal, stock_list):
        super().__init__(name=name, raw_con=raw_con)

        # calculation params
        self.trade_cal = trade_cal  # calculating factor data through time-line
        self.stock_list = stock_list  # looping calculation through all stock

    def factor_cal(self, ts_code):
        """this is the factor calculation function, should be empty at default"""
        pass

    @staticmethod
    def fill_factor_data(trade_cal, factor_data):
        """if factor data does not match the trade calendar, fill the data"""
        data = pd.concat([trade_cal, factor_data], axis=1, join='outer')
        data.sort_index(inplace=True)

        data.fillna(method='ffill', inplace=True)
        return data.iloc[:, 1:]

class FactorSignalProcessLoop(FactorSignalProcess):

    def loop_cal(self):

        # drop existing table
        self.factor_data_con.drop_table(table_name=self.name)

        # looping
        for ts_code in self.stock_list['ts_code']:

            print(f'calculating {self.name} for {ts_code}')

            # calculate factor data
            factor_data = self.factor_cal(ts_code=ts_code)
            # fill factor data
            factor_data = self.fill_factor_data(trade_cal=self.trade_cal, factor_data=factor_data)

            # optimize format of output
            factor_data.index.name = 'trade_date'
            factor_data['ts_code'] = ts_code

            # saving
            self.factor_data_con.save_data(factor_data, table_name=self.name, if_exists='append', index=True)


