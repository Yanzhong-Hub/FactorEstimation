"""
News data from tushare.pro

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com

----------------------------------------

"""

from .pro import TusharePro


class News(TusharePro):

    @staticmethod
    def news(start_date, end_date, src: str = 'sina'):
        """src list:
        sina
        wallstreetcn
        10jqka
        eastmoney
        yuncaijing
        """
        df = TusharePro.pro.news(**{
                "start_date": start_date,
                "end_date": end_date,
                "src": src,
                "limit": "",
                "offset": ""
            }, fields=[
                "datetime",
                "content",
                "title",
                "channels",
                "score"
            ])
        return df