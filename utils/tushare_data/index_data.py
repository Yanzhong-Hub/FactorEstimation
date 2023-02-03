"""
Stock Index data from tushare.pro

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com

----------------------------------------

"""

from .pro import TusharePro


class IndexData(TusharePro):

    @staticmethod
    def index_basic():
        df = TusharePro.pro.index_basic(**{
            "ts_code": "",
            "market": "",
            "publisher": "",
            "category": "",
            "name": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "name",
            "market",
            "publisher",
            "category",
            "base_date",
            "base_point",
            "list_date"
        ])
        return df

    @staticmethod
    def index_daily(ts_code: str, start_date: str = '', end_date: str = ''):
        df = TusharePro.pro.index_daily(**{
            "ts_code": ts_code,
            "trade_date": "",
            "start_date": start_date,
            "end_date": end_date,
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "close",
            "open",
            "high",
            "low",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])
        return df

    @staticmethod
    def index_weekly(ts_code: str = '', start_date: str = '', end_date: str = ''):
        df = TusharePro.pro.index_weekly(**{
            "ts_code": ts_code,
            "trade_date": "",
            "start_date": start_date,
            "end_date": end_date,
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "close",
            "open",
            "high",
            "low",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])
        return df

    @staticmethod
    def index_monthly(ts_code: str = '', start_date: str = '', end_date: str = ''):
        df = TusharePro.pro.index_monthly(**{
            "ts_code": ts_code,
            "trade_date": "",
            "start_date": start_date,
            "end_date": end_date,
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "close",
            "open",
            "high",
            "low",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])
        return df

    @staticmethod
    def index_weight(ts_code: str = '', start_date: str = '', end_date: str = ''):
        df = TusharePro.pro.index_weight(**{
            "index_code": ts_code,
            "trade_date": "",
            "start_date": start_date,
            "end_date": end_date,
            "limit": "",
            "offset": ""
        }, fields=[
            "index_code",
            "con_code",
            "trade_date",
            "weight"
        ])
        return df

    @staticmethod
    def industry_list(level: str = 'L1', src: str = 'SW2021'):
        df = TusharePro.pro.index_classify(**{
            "index_code": "",
            "level": level,
            "src": src,
            "parent_code": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "index_code",
            "industry_name",
            "level",
            "industry_code",
            "is_pub",
            "parent_code"
        ])
        return df
