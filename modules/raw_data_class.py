"""
SCRIPT NAME HERE

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

from utils import YzSQL, init_data_base


class RawData:
    """
    Managing raw_data.sql

    Attributes
    ====================
    sql:
        YzSQL method connect to raw_data.sql

    Methods
    ====================
    init_db_run(start_date, end_date):
        initialized raw_data.sql, re-download data from tushare

    update_db_run(end_date):
        update raw_data.sql until the end_date
    """

    def __init__(self, raw_data_con):
        self.sql = raw_data_con

    def init_db_run(self, start_date, end_date):
        """

        :param start_date: download start_date
        :param end_date: download end_date
        :return:
        """
        init_data_base(self.sql, start_date, end_date)

    def update_db_run(self, end_date):
        """

        :param end_date: download end_date
        :return:
        """
        pass
