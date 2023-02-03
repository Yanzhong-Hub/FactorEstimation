"""
factor back test main

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
import types

from utils import init_data_base
from factor_signal_module.factor_signal import FactorCal
from factor_signal_module.factor_cals import *


class FactorBackTest:

    def __init__(self):
        # sql connections
        self.raw_data_con = YzSQL('data/raw_data.sql')
        self.factor_data_con = YzSQL('data/factor_signal.sql')
        self.factor_test_result_con = YzSQL('data/factor_result.sql')

        # useful data
        self.stock_list = query_stock_list(self.raw_data_con, market=('主板', '中小板', '创业板'))
        self.trade_cal = query_trade_cal(self.raw_data_con)

    def init_db_run(self, start_date, end_date):
        """init data base"""
        init_data_base(self.raw_data_con, start_date, end_date)

    def update_data_base(self):
        pass

    def factor_data_to_sql(self, name, factor_cal):
        factor = FactorCal(name=name,
                           raw_con=self.raw_data_con,
                           factor_con=self.factor_data_con,
                           stock_list=self.stock_list,
                           trade_cal=self.trade_cal)
        factor.factor_cal = types.MethodType(factor_cal, factor)
        factor.loop_cal()

    def factor_result_cal(self):
        pass


def _test():
    bt = FactorBackTest()
    data = bt.factor_data_con.query("SELECT trade_date from next_drifts WHERE ts_code = '000001.SZ'")
    print(data)
    # bt.factor_data_to_sql(name='q_roe', factor_cal=q_roe_cal)
    # bt.factor_data_to_sql(name='bm', factor_cal=bm_cal)
    # bt.factor_data_to_sql(name='next_drifts', factor_cal=next_drifts)
    # bt.factor_data_to_sql(name='bm_tushare', factor_cal=bm_tushare_cal)


if __name__ == '__main__':
    _test()
