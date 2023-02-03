"""
SCRIPT NAME HERE

==========
Created by Yanzhong Huang
Email: yanzhong.huang@outlook.com
"""

from data_module import *
from utils import sigma_exclude, normalized, ols


class CrossSectionCal:

    def __init__(self,
                 factor_con,
                 trade_date,
                 predict_n):
        self.factor_con = factor_con  # sql connection

        self.trade_date = trade_date  # trade_calendar
        self.predict_n = predict_n  # predict period, count by trade day

        # auto add next drifts data
        self.data = self.add_next_drifts()
        self.ranked_data = None
        self.grouped_data = dict()
        self.group_num = 10

        # result
        self.result = dict()

    def change_predict_n(self, predict_n: int):
        self.predict_n = predict_n
        self.data = self.add_next_drifts()

    def add_next_drifts(self):
        """add next_drifts"""
        return query_next_drifts_by_date(yz_sql=self.factor_con,
                                         predict_n=self.predict_n,
                                         trade_date=self.trade_date)

    def add_factor_data(self, factor_name):
        """adding cross section data"""
        # query factor data
        factor_data = query_cross_section_factor(yz_sql=self.factor_con,
                                                 trade_date=self.trade_date,
                                                 factor_name=factor_name)

        # data cleaned
        factor_data = sigma_exclude(data=factor_data)
        factor_data = normalized(factor_data)

        if factor_name not in self.data.columns:  # judge existence of factor

            self.data = pd.concat([self.data, factor_data], axis=1)
            self.ranked_data = self.data.rank()  # add ranked_data
            self.add_group_data(group_num=self.group_num, factor_name=factor_name)  # adding group data
        else:
            print('因子已存在')

    def add_group_data(self, group_num, factor_name):
        factor_group = dict()  # generate factor dict
        self.grouped_data[factor_name] = factor_group

        group_names = [f'group_{_}' for _ in range(1, group_num + 1)]  # create group name: group_1, group_2...
        cut_result = pd.qcut(self.data[factor_name], group_num, labels=group_names)

        for group_name in group_names:
            factor_group[group_name] = \
                self.data[[f'shifts_{self.predict_n}', factor_name]].loc[cut_result.loc[cut_result == group_name].index]

    def result_cal(self, factor_name):
        """calculate all result and add to self.result[factor_name]"""
        ic = self.ic_cal(factor_name)
        rank_ic = self.rank_ic_cal(factor_name)
        factor_lambda = self.lambda_cal(factor_name)
        self.result[factor_name] = pd.DataFrame({self.trade_date: [ic, rank_ic, factor_lambda]},
                                                index=['IC', 'RankIC', 'Lambda'])

        grouped_table = self.grouped_data_average(factor_name)
        grouped_ic = self.grouped_data_ic(grouped_table)
        grouped_rank_ic = self.grouped_data_rank_ic(grouped_table)
        self.result[f'{factor_name}_grouped_result'] = pd.DataFrame({self.trade_date: [grouped_ic, grouped_rank_ic]},
                                                                    index=['IC', 'RankIC'])
        self.result[f'{factor_name}_groups_average'] = grouped_table

    def ic_cal(self, factor_name):
        return self.data[factor_name].corr(self.data[f'shifts_{self.predict_n}'])

    def lambda_cal(self, factor_name):
        reg_data = self.data[[f'shifts_{self.predict_n}', factor_name]].copy()
        reg_data.dropna(inplace=True)
        reg_model = ols(y_input=reg_data[f'shifts_{self.predict_n}'],
                        x_input=reg_data[factor_name])
        return None

    def rank_ic_cal(self, factor_name):
        return self.ranked_data[factor_name].corr(self.ranked_data[f'shifts_{self.predict_n}'])

    def grouped_data_average(self, factor_name):
        mean_list = []
        for item in self.grouped_data[factor_name].values():
            mean_list.append(item.mean())
        return pd.concat(mean_list, axis=1).T

    @staticmethod
    def grouped_data_ic(grouped_data_table):
        return grouped_data_table.iloc[:, 0].corr(grouped_data_table.iloc[:, 1])

    @staticmethod
    def grouped_data_rank_ic(grouped_data_table):
        ranked = grouped_data_table.rank()
        return ranked.iloc[:, 0].corr(ranked.iloc[:, 1])
