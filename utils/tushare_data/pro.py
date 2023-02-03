"""
Optimise tushare module
@author: Yanzhong Huang
Date: 15 Oct 2021
"""

import tushare as ts


class TusharePro:
    """
    base class for tushare data

    Attributes
    ==========
    pro:
        tushare pro class
        example: self.pro.index_daily()
    """
    pro = ts.pro_api('8048cbf9b5b32cf6c5ca12b8863a1869901b566749dccbd796b458b5')
    ts.set_token('8048cbf9b5b32cf6c5ca12b8863a1869901b566749dccbd796b458b5')

    # pro bar, general api for all data_get
    # https://tushare.pro/document/2?doc_id=109
    @staticmethod
    def pro_bar(ts_code, start_date='', end_date='', asset='E', adj='hfq', freq='D'):
        df = ts.pro_bar(ts_code=ts_code,
                        start_date=start_date,
                        end_date=end_date,
                        asset=asset,
                        adj=adj,
                        freq=freq)
        return df
