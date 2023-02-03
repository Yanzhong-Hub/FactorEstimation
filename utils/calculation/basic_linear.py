"""
The basic calculation module

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com

----------------------------------------
"""

import pandas as pd
import numpy as np


def drifts_cal(data):
    """calculate last drift"""
    return data / data.shift(1) - 1


def next_drifts_cal(data):
    drifts = drifts_cal(data)
    return drifts.shift(-1)


def annualize_drifts(expected_drifts, t_count):
    return (1 + expected_drifts) ** t_count - 1


def annualize_volatility(volatility, t_count):
    return volatility * np.sqrt(t_count)


def draw_back(data):
    """回撤时序数据"""
    return (data - np.maximum.accumulate(data)) / np.maximum.accumulate(data)
