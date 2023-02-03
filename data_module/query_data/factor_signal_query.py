"""
SCRIPT NAME HERE

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
import pandas as pd

from data_module.db_connector import FactorSignalCon
from utils import YzSQL


class FactorSignalTimeSeries(FactorSignalCon):

    def query_next_drifts(self, ts_code, predict_n):
        return self.sql.query(sql=f"SELECT trade_date, drifts_{predict_n} FROM next_drifts "
                                f"WHERE ts_code = {ts_code}",
                            index_col='trade_date')


def query_next_drifts_by_date(yz_sql, trade_date, predict_n):
    column_name = f'shifts_{predict_n}'
    return yz_sql.query(sql=f"SELECT ts_code, {column_name} FROM next_drifts "
                            f"WHERE trade_date = '{trade_date}'",
                        index_col='ts_code')


def query_factor_data_by_code(yz_sql, factor_name, ts_code):
    return yz_sql.query(sql=f"SELECT trade_date, {factor_name} FROM {factor_name} "
                            f"WHERE ts_code= {ts_code}",
                        index_col='trade_date')


def query_factor_data_by_date(yz_sql, factor_name, trade_date):
    return yz_sql.query(sql=f"SELECT ts_code, {factor_name} FROM {factor_name} "
                            f"WHERE trade_date= '{trade_date}'",
                        index_col='ts_code')

