"""
query raw data

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
import pandas as pd

from data_module.db_connector import RawCon


class RawQueryBasic(RawCon):
    """query basic data such as stock list, trade calendar"""

    def __init__(self):
        super().__init__()

    def query_stock_list(self, market: tuple):
        """包含主板、中小板、创业板股票，剔除所有ST股"""
        if len(market) == 1:
            stock_list = self.sql.query(sql=f"SELECT ts_code, name, industry, market, list_date "
                                            f"FROM stock_list "
                                            f"WHERE market == '{market[0]}'")
        else:
            stock_list = self.sql.query(sql=f"SELECT ts_code, name, industry, market, list_date "
                                            f"FROM stock_list "
                                            f"WHERE market IN {market}")
        stock_list = stock_list.loc[~stock_list['name'].str.contains('ST')]
        stock_list.reset_index(inplace=True)
        return stock_list

    def query_trade_cal(self, start_date, end_date):
        trade_cal = self.sql.query(sql=f"SELECT cal_date, is_open FROM trade_cal "
                                       f"WHERE is_open == 1 AND (cal_date >= '{start_date}' AND cal_date <= '{end_date}')",
                                   index_col='cal_date')
        trade_cal.index = pd.to_datetime(trade_cal.index).date
        trade_cal.sort_index(inplace=True)
        return trade_cal


class RawQueryTimeSeries(RawCon):
    """query time series data, index by date"""

    def __init__(self):
        super().__init__()

    def query_daily_original(self, ts_code):
        daily_close = self.yz_sql.query(sql=f"SELECT trade_date, close "
                                            f"FROM stock_price_original "
                                            f"WHERE ts_code = '{ts_code}'",
                                        index_col='trade_date')
        daily_close.index = pd.to_datetime(daily_close.index).date
        daily_close.sort_index(inplace=True)
        return daily_close

    def query_daily_close(self, ts_code):
        daily_close = self.sql.query(sql=f"SELECT trade_date, close FROM stock_daily WHERE ts_code = '{ts_code}'",
                                     index_col='trade_date')
        daily_close.index = pd.to_datetime(daily_close.index).date
        daily_close.sort_index(inplace=True)
        return daily_close

    def query_monthly_close(self, ts_code):
        monthly_close = self.sql.query(sql=f"SELECT trade_date, close FROM stock_monthly WHERE ts_code = '{ts_code}'",
                                       index_col='trade_date')
        monthly_close.index = pd.to_datetime(monthly_close.index).date
        monthly_close.sort_index(inplace=True)
        return monthly_close

    def query_fundamentals(self, ts_code, account_name, sheet_name):
        data = self.sql.query(sql=f"SELECT ann_date, {account_name} FROM {sheet_name} WHERE ts_code = '{ts_code}'")
        data.dropna(inplace=True)
        data = data.loc[~data['ann_date'].duplicated(keep='last')]
        data.set_index('ann_date', inplace=True)
        data.index = pd.to_datetime(data.index).date
        data.sort_index(ascending=True, inplace=True)
        return data


class RawQueryCrossSection(RawCon):

    def __init__(self):
        super().__init__()

    def query_close(self, trade_date):
        data = self.sql.query(sql=f"SELECT ts_code, close FROM stock_daily "
                                  f"WHERE trade_date = '{trade_date}' ",
                              index_col='ts_code')
        data.columns = [trade_date]
        return data
