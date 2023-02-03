"""
Tushare stock package

@author: Yanzhong Huang

数据包含
# 沪深股票
## 基础数据
- 股票列表
- 各交易所交易日历
- 沪深股通成份股
- 股票曾用名
- 上市公司基本信息
- IPO新股列表
"""

from .pro import TusharePro


class StockBasic(TusharePro):

    @staticmethod
    def stock_list(list_status='L'):
        """
        :return: 获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
        """

        df = TusharePro.pro.stock_basic(**{
                "ts_code": "",
                "name": "",
                "exchange": "",
                "market": "",
                "is_hs": "",
                "list_status": list_status,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "symbol",
                "name",
                "area",
                "industry",
                "market",
                "list_date",
                "fullname",
                "enname",
                "cnspell",
                "exchange",
                "curr_type",
                "list_status",
                "delist_date",
                "is_hs"
            ])
        return df

    @staticmethod
    def trade_cal(start_date='', end_date='', exchange='SSE'):
        """

        :param exchange: 交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源
        :param start_date: 开始日期 （格式：YYYYMMDD 下同）
        :param end_date: 结束日期
        :return: 取各大交易所交易日历数据,默认提取的是上交所
        """

        df = TusharePro.pro.trade_cal(**{
                "exchange": exchange,
                "cal_date": "",
                "start_date": start_date,
                "end_date": end_date,
                "is_open": "",
                "limit": "",
                "offset": ""
            }, fields=[
                "exchange",
                "cal_date",
                "is_open",
                "pretrade_date"
            ])
        return df

    # weekly trading calendar
    @staticmethod
    def trade_cal_weekly(start_date='', end_date=''):
        df = TusharePro.pro.index_weekly(**{
            "ts_code": "000300.sh",
            "trade_date": "",
            "start_date": start_date,
            "end_date": end_date,
            "limit": "",
            "offset": ""
        }, fields=[
            "trade_date",
        ])
        return df

    @staticmethod
    def name_change(ts_code='', start_date='', end_date=''):
        """
        :param ts_code: TS代码
        :param start_date: 公告开始日期
        :param end_date: 公告结束日期
        :return: 历史名称变更记录
        """

        df = TusharePro.pro.namechange(**{
                "ts_code": ts_code,
                "start_date": start_date,
                "end_date": end_date,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "name",
                "start_date",
                "end_date",
                "ann_date",
                "change_reason"
            ])
        return df

    @staticmethod
    def hs_const(hs_type='SH', is_new=''):
        """
        :param hs_type: 类型，SH沪股通，SZ深股通
        :param is_new: 是否最新，1最新，0不是
        :return: 获取沪股通、深股通成分数据
        """
        df = TusharePro.pro.hs_const(**{
                "hs_type": hs_type,
                "is_new": is_new,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "hs_type",
                "in_date",
                "out_date",
                "is_new"
            ])
        return df

    @staticmethod
    def stock_company(ts_code='', exchange='', status=''):
        """
        :param ts_code: 股票代码
        :param exchange: 交易所代码
        :param status: 状态
        :return: 获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取
        """
        df = TusharePro.pro.stock_company(**{
                "ts_code": ts_code,
                "exchange": exchange,
                "status": status,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "exchange",
                "chairman",
                "manager",
                "secretary",
                "reg_capital",
                "setup_date",
                "province",
                "city",
                "website",
                "email",
                "employees",
                "introduction",
                "ann_date",
                "office",
                "business_scope",
                "main_business"
            ])
        return df

    @staticmethod
    def stock_managers(ts_code='', ann_date='', start_date='', end_date=''):
        """

        :param ts_code: 股票代码
        :param ann_date: 公告日期
        :param start_date: 公告开始日期
        :param end_date: 公告结束日期
        :return: 获取上市公司管理层
        """
        df = TusharePro.pro.stk_managers(**{
                "ts_code": ts_code,
                "ann_date": ann_date,
                "start_date": start_date,
                "end_date": end_date,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "ann_date",
                "name",
                "gender",
                "lev",
                "title",
                "edu",
                "national",
                "birthday",
                "begin_date",
                "end_date",
                "resume"
            ])
        return df

    @staticmethod
    def stock_managers_rewards(ts_code, ann_date=''):
        """

        :param ts_code: 股票代码，必填项
        :param ann_date: 报告期
        :return: 获取上市公司管理层薪酬和持股
        """

        df = TusharePro.pro.stk_rewards(**{
                "ts_code": ts_code,
                "end_date": ann_date,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "ann_date",
                "end_date",
                "name",
                "title",
                "reward",
                "hold_vol"
            ])
        return df

    @staticmethod
    def new_share(start_date='', end_date=''):
        """

        :param start_date:
        :param end_date:
        :return: 获取新股上市列表数据
        """
        df = TusharePro.pro.new_share(**{
                "start_date": start_date,
                "end_date": end_date,
                "limit": "",
                "offset": ""
            }, fields=[
                "ts_code",
                "sub_code",
                "name",
                "ipo_date",
                "issue_date",
                "amount",
                "market_amount",
                "price",
                "pe",
                "limit_amount",
                "funds",
                "ballot"
            ])
        return df

    @staticmethod
    def stock_basic_back_up(trade_date='', ts_code=''):
        """

        :param trade_date: 交易日期
        :param ts_code: 股票代码
        :return: 获取备用基础列表，数据从2016年开始。单次最大5000条，可以根据日期参数循环获取历史，正式权限需要5000积分。

        ## 输出参数
        rade_date	str	Y	交易日期
        ts_code	str	Y	TS股票代码
        name	str	Y	股票名称
        industry	str	Y	行业
        area	str	Y	地域
        pe	float	Y	市盈率（动）
        float_share	float	Y	流通股本（亿）
        total_share	float	Y	总股本（亿）
        total_assets	float	Y	总资产（亿）
        liquid_assets	float	Y	流动资产（亿）
        fixed_assets	float	Y	固定资产（亿）
        reserved	float	Y	公积金
        reserved_pershare	float	Y	每股公积金
        eps	float	Y	每股收益
        bvps	float	Y	每股净资产
        pb	float	Y	市净率
        list_date	str	Y	上市日期
        undp	float	Y	未分配利润
        per_undp	float	Y	每股未分配利润
        rev_yoy	float	Y	收入同比（%）
        profit_yoy	float	Y	利润同比（%）
        gpr	float	Y	毛利率（%）
        npr	float	Y	净利润率（%）
        holder_num	int	Y	股东人数
        """
        df = TusharePro.pro.bak_basic(**{
                "trade_date": trade_date,
                "ts_code": ts_code,
                "limit": "",
                "offset": ""
            }, fields=[
                "trade_date",
                "ts_code",
                "name",
                "industry",
                "area",
                "pe",
                "float_share",
                "total_share",
                "total_assets",
                "liquid_assets",
                "fixed_assets",
                "reserved",
                "reserved_pershare",
                "eps",
                "bvps",
                "pb",
                "list_date",
                "undp",
                "per_undp",
                "rev_yoy",
                "profit_yoy",
                "gpr",
                "npr",
                "holder_num"
            ])
        return df
