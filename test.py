"""

------------------------------------------

Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

from time import time
import datetime
import data_module as dm


def download_test():
    import data_module
    import pandas as pd

    download_basic = dm.DownloadBasic(start_date='20000101',
                                   end_date='20221231')
    print(download_basic.download_trade_cal().head())
    print(download_basic.download_stock_list().head())

    # download_single = data_module.DownloadSingleCode(code='000001.SZ', start_date='20000101', end_date='20221231')
    # print(download_single.download_all())

    # stock_list = pd.DataFrame({'ts_code': ['000001.SZ',
    #                                        '000005.SZ'
    #                                        ], 'name': ['000001', '000005']})
    # loop_save = data_module.LoopSave(stock_list=stock_list, start_date='20100101', end_date='20221231')
    # loop_save.loop_save()


if __name__ == '__main__':
    run_start = time()

    """tests"""
    # mapping_test()
    download_test()
    # query_factor_data_test()
    # cross_section_test()
    # factor_signal_test()

    # measure process time
    run_end = time()
    print(f'End in {run_end - run_start} seconds')
    