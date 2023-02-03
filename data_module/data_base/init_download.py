"""
Download data through tushare.pro

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

import datetime
import pandas as pd

from utils.tushare_data import StockBasic, TusharePro, TushareFundamental


class DownloadBasic:

    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def download_trade_cal(self):
        trade_cal = StockBasic.trade_cal(start_date=self.start_date, end_date=self.end_date)
        trade_cal['cal_date'] = pd.to_datetime(trade_cal['cal_date']).dt.date
        trade_cal['pretrade_date'] = pd.to_datetime(trade_cal['pretrade_date']).dt.date
        return trade_cal

    @staticmethod
    def download_stock_list():
        return StockBasic.stock_list(list_status='L')


class DownloadSingleCode:

    def __init__(self, code: str, start_date: str, end_date: str):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date

    def download_all(self):
        return {'stock_daily': self.download_stock_daily(),
                'stock_daily_hfq': self.download_stock_daily_hfq(),
                'balance_sheet': self.download_balance_sheet(),
                'cash_flow': self.download_cash_flow(),
                'income_sheet': self.download_income_sheet(),
                'finance_ratio': self.download_finance_ratio()}

    def download_stock_daily(self):
        return TusharePro.pro_bar(ts_code=self.code, start_date=self.start_date, end_date=self.end_date, adj='')

    def download_stock_daily_hfq(self):
        return TusharePro.pro_bar(ts_code=self.code, start_date=self.start_date, end_date=self.end_date)

    def download_balance_sheet(self):
        return TushareFundamental.balance_sheet(ts_code=self.code, start_date=self.start_date, end_date=self.end_date)

    def download_cash_flow(self):
        return TushareFundamental.cash_flow(ts_code=self.code, start_date=self.start_date, end_date=self.end_date)

    def download_income_sheet(self):
        return TushareFundamental.income_sheet(ts_code=self.code, start_date=self.start_date, end_date=self.end_date)

    def download_finance_ratio(self):
        return TushareFundamental.finance_ratio(ts_code=self.code, start_date=self.start_date, end_date=self.end_date)




