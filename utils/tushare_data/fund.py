"""
Public Fund from tushare.pro

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com

----------------------------------------

"""
from .pro import TusharePro


class TushareFund(TusharePro):

    @staticmethod
    def fund_list(market: str = 'E'):  # 场内基金
        df = TusharePro.pro.fund_basic(**{
            "ts_code": "",
            "market": market,
            "update_flag": "",
            "offset": "",
            "limit": "",
            "status": "",
            "name": ""
        }, fields=[
            "ts_code",
            "name",
            "management",
            "custodian",
            "fund_type",
            "found_date",
            "due_date",
            "list_date",
            "issue_date",
            "delist_date",
            "issue_amount",
            "m_fee",
            "c_fee",
            "duration_year",
            "p_value",
            "min_amount",
            "exp_return",
            "benchmark",
            "status",
            "invest_type",
            "type",
            "trustee",
            "purc_startdate",
            "redm_startdate",
            "market"
        ])
        return df

    @staticmethod
    def fund_company():
        df = TusharePro.pro.fund_company(**{
            "setup_date": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "name",
            "shortname",
            "province",
            "city",
            "address",
            "phone",
            "office",
            "website",
            "chairman",
            "manager",
            "reg_capital",
            "setup_date",
            "end_date",
            "employees",
            "main_business",
            "org_code",
            "credit_code"
        ])
        return df

    @staticmethod
    def fund_manager(ts_code, ann_date, name):
        df = TusharePro.pro.fund_manager(**{
            "ts_code": ts_code,
            "ann_date": ann_date,
            "name": name,
            "offset": "",
            "limit": ""
        }, fields=[
            "ts_code",
            "ann_date",
            "name",
            "gender",
            "birth_year",
            "edu",
            "nationality",
            "begin_date",
            "end_date",
            "resume"
        ])
        return df

    @staticmethod
    def fund_share(ts_code, trade_date='', start_date='', end_date=''):
        df = TusharePro.pro.fund_share(**{
            "ts_code": ts_code,
            "trade_date": trade_date,
            "start_date": start_date,
            "end_date": end_date,
            "market": "",
            "fund_type": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "fd_share",
            "fund_type",
            "market"])
        return df

    @staticmethod
    def fund_nav(ts_code, nav_date='', market='E', start_date='', end_date=''):
        df = TusharePro.pro.fund_nav(**{
            "ts_code": ts_code,
            "nav_date": nav_date,
            "offset": "",
            "limit": "",
            "market": market,
            "start_date": start_date,
            "end_date": end_date
        }, fields=[
            "ts_code",
            "ann_date",
            "nav_date",
            "unit_nav",
            "accum_nav",
            "accum_div",
            "net_asset",
            "total_netasset",
            "adj_nav",
            "update_flag"
        ])
        return df

    @staticmethod
    def fund_div(ts_code='', ann_date='', ex_date='', pay_date=''):
        df = TusharePro.pro.fund_div(**{
            "ann_date": ann_date,
            "ex_date": ex_date,
            "pay_date": pay_date,
            "ts_code": ts_code,
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "ann_date",
            "imp_anndate",
            "base_date",
            "div_proc",
            "record_date",
            "ex_date",
            "pay_date",
            "earpay_date",
            "net_ex_date",
            "div_cash",
            "base_unit",
            "ear_distr",
            "ear_amount",
            "account_date",
            "base_year"
        ])
        return df

    @staticmethod
    def fund_portfolio(ts_code='', ann_date='', start_date='', end_date=''):
        df = TusharePro.pro.fund_portfolio(**{
            "ts_code": ts_code,
            "ann_date": ann_date,
            "start_date": start_date,
            "end_date": end_date,
            "period": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "ann_date",
            "end_date",
            "symbol",
            "mkv",
            "amount",
            "stk_mkv_ratio",
            "stk_float_ratio"
        ])
        return df

    @staticmethod
    def fund_daily(ts_code='', trade_date='', start_date='', end_date=''):
        df = TusharePro.pro.fund_daily(**{
            "trade_date": trade_date,
            "start_date": start_date,
            "end_date": end_date,
            "ts_code": ts_code,
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "pre_close",
            "open",
            "high",
            "low",
            "close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])
        return df

    @staticmethod
    def fund_adj(ts_code='', trade_date='', start_date='', end_date=''):
        df = TusharePro.pro.fund_adj(**{
            "ts_code": ts_code,
            "trade_date": trade_date,
            "start_date": start_date,
            "end_date": end_date,
            "offset": "",
            "limit": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "adj_factor"
        ])
        return df
