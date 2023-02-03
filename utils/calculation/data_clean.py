"""
THE SCRIPT NAME HERE!

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com

----------------------------------------

"""

import pandas as pd


def mad_replace(data, n: int = 5):
    """
    filter data with MAD method:
    change all outlier into the boundary value
    """
    median = data.median()
    mad = ((data - median).abs()).median()
    min_range = median - n * mad
    max_range = median + n * mad
    return data.clip(lower=min_range, upper=max_range, axis=1)


def sigma_replace(data, n: int = 3):
    mean = data.mean()
    sigma = data.std()
    min_range = mean - n * sigma
    max_range = mean + n * sigma
    return data.clip(lower=min_range, upper=max_range, axis=1)


def percentile_replace(data, range: tuple = (0.01, 0.99)):
    """
    :param data: dataframe
    :param range: tuple: (min, max) for the boundary
    :return:
    """
    limit = data.quantile(q=range, interpolation='nearest')
    return data.clip(lower=limit.iloc[0], upper=limit.iloc[1], axis=1)


def exclude_outlier(data, min_values: list, max_values: list):
    temp = []
    for column, lower, upper in zip(data.columns, min_values, max_values):
        temp.append(data[column].loc[(data[column] >= lower) & (data[column] <= upper)])
    return pd.concat(temp, axis=1, join='inner')


def mad_exclude(data, n: int = 5):
    """
    filter data with MAD method:
    change all outlier into the boundary value
    """
    median = data.median()
    mad = ((data - median).abs()).median()
    min_range = list(median - n * mad)
    max_range = list(median + n * mad)
    return exclude_outlier(data, min_range, max_range)


def sigma_exclude(data, n: int = 3):
    mean = data.mean()
    sigma = data.std()
    min_range = mean - n * sigma
    max_range = mean + n * sigma
    return exclude_outlier(data, min_range, max_range)


def percentile_exclude(data, range_limit: tuple = (0.01, 0.99)):
    """
    :param data: dataframe
    :param range_limit: tuple: (min, max) for the boundary
    :return:
    """
    limit = data.quantile(q=range_limit, interpolation='nearest')
    min_values = list(limit.loc[range_limit[0]])
    max_values = list(limit.loc[range_limit[1]])

    return exclude_outlier(data, min_values, max_values)


def normalized(data: object) -> object:
    mean = data.mean()
    sigma = data.std()
    return (data - mean) / sigma


def _test():
    import pandas as pd
    from utils.yz_sql import YzSQL
    yz_sql = YzSQL(db_path='../../data/raw_data.sql')
    data = yz_sql.query(sql="SELECT trade_date, close FROM stock_daily WHERE ts_code = '000001.SZ'",
                        index_col='trade_date')
    data.index = pd.to_datetime(data.index)
    data.sort_index(inplace=True)
    data.columns = ['a']
    data_2 = yz_sql.query(sql="SELECT trade_date, close FROM stock_daily WHERE ts_code = '000005.SZ'",
                          index_col='trade_date')
    data_2.index = pd.to_datetime(data_2.index)
    data_2 = pd.concat([data, data_2], axis=1)
    data_2.sort_index(inplace=True)
    data_2.columns = ['a', 'b']
    data_2.dropna(inplace=True)

    print(data.max())
    print('********')
    # print(sigma_replace(data_2).min(), sigma_replace(data_2).max())
    print(percentile_exclude(data).max())
    print(percentile_exclude(data).shape)
    print(data.shape)


if __name__ == '__main__':
    _test()
