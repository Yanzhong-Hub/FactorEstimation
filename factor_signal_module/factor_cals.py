"""
factor calculation

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
from data_module.query_data.raw_query import *
from utils import YzSQL


def next_drifts(self, ts_code):
    price = query_daily_close(ts_code, self.raw_data_con)
    shifts_list = []
    for num in range(1, 201):
        shifts = price.shift(-num) / price - 1
        shifts.columns = [f'shifts_{num}']
        shifts_list.append(shifts)

    return pd.concat(shifts_list, axis=1)


def q_roe_cal(self, ts_code):
    return query_fundamentals(ts_code=ts_code, yz_sql=self.raw_data_con,
                              account_name='q_roe', sheet_name='finance_ratio')


def bm_cal(self, ts_code):
    # 股东权益
    total_hldr_eqy_exc_min_int = query_fundamentals(yz_sql=self.raw_data_con,
                                                    ts_code=ts_code,
                                                    account_name='total_hldr_eqy_exc_min_int',
                                                    sheet_name='balance_sheet')
    # 股票数量
    total_share_number = query_fundamentals(yz_sql=self.raw_data_con,
                                            ts_code=ts_code,
                                            account_name='total_share',
                                            sheet_name='balance_sheet')
    # 股价
    price_daily = query_daily_original(ts_code=ts_code, yz_sql=self.raw_data_con)

    factor_data = pd.concat([price_daily, total_hldr_eqy_exc_min_int, total_share_number], axis=1, join='outer')
    factor_data.fillna(method='ffill', inplace=True)

    factor_data['bm'] = factor_data['total_hldr_eqy_exc_min_int'] / (factor_data['close'] * factor_data['total_share'])
    return factor_data['bm']


def bm_tushare_cal(self, ts_code):
    # 股东权益
    bps = query_fundamentals(yz_sql=self.raw_data_con,
                             ts_code=ts_code,
                             account_name='bps',
                             sheet_name='finance_ratio')
    # 股价
    price_daily = query_daily_original(ts_code=ts_code, yz_sql=self.raw_data_con)

    factor_data = pd.concat([price_daily, bps], axis=1, join='outer')
    factor_data.fillna(method='ffill', inplace=True)

    factor_data['bm_tushare'] = factor_data['bps'] / factor_data['close']
    return factor_data['bm_tushare']


class FactorCalTest:

    def __init__(self):
        # sql connections
        self.raw_data_con = YzSQL('../data/raw_data.sql')
        self.factor_data_con = YzSQL('../data/factor_signal.sql')
        self.factor_test_result_con = YzSQL('../data/factor_result.sql')

        # useful data
        self.stock_list = query_stock_list(self.raw_data_con)
        self.trade_cal = query_trade_cal(self.raw_data_con)


def _test():
    con = FactorCalTest()
    print(next_drifts(con, ts_code='000001.SZ'))


if __name__ == '__main__':
    _test()
