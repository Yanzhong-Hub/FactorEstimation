"""
save initial data

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""
import multiprocessing

from data_module.db_connector import RawCon
from .init_download import DownloadSingleCode


class LoopSave(RawCon):

    def __init__(self, start_date, end_date, stock_list):
        super().__init__()
        self.stock_list = stock_list
        self.start_date = start_date
        self.end_date = end_date

    def save_single(self, code):
        """download all data for single stock"""

        # create downloader instance
        downloader = DownloadSingleCode(code=code, start_date=self.start_date, end_date=self.end_date)
        # download all data
        data_dict = downloader.download_all()

        # save data for each result
        for name, data in data_dict.items():
            # print(name, data)
            self.sql.save_data(data=data, table_name=name, if_exists='append')

        return f'Downloading finished: {code}'

    def loop_save(self):
        """looping download using multiprocessing"""
        multiprocessing.set_start_method(method='fork')

        # drop existing table
        for name in ['stock_daily', 'stock_daily_hfq', 'balance_sheet', 'cash_flow', 'income_sheet', 'finance_ratio']:
            self.sql.drop_table(table_name=name)

        stock_list = list(self.stock_list['ts_code'])

        processes = []
        for stock in stock_list:
            p = multiprocessing.Process(target=save_single, args=(self, stock))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()


def save_single(self, code):
    """download all data for single stock"""

    # create downloader instance
    downloader = DownloadSingleCode(code=code, start_date=self.start_date, end_date=self.end_date)
    # download all data
    data_dict = downloader.download_all()

    # save data for each result
    for name, data in data_dict.items():
        # print(name, data)
        self.sql.save_data(data=data, table_name=name, if_exists='append')

    print(f'Downloading finished: {code}')
