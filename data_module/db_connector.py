"""
Database connection

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

from abc import ABC, abstractmethod

from utils import YzSQL


class DbConnector(ABC):

    @abstractmethod
    def connection(self):
        pass


class RawCon(DbConnector):

    def __init__(self):
        self.sql = self.connection()

    def connection(self):
        return YzSQL(db_path='data/raw_data.sql')


class FactorSignalCon(DbConnector):

    def __init__(self):
        self.sql = self.connection()

    def connection(self):
        return YzSQL(db_path='data/factor_signal.sql')


class FactorResultCon(DbConnector):

    def __init__(self):
        self.sql = self.connection()

    def connection(self):
        return YzSQL(db_path='data/factor_result.sql')
