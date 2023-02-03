"""
THE REGRESSIONS MODULE

Author: Yanzhong Huang
Email: yanzhong.huang@outlook.com

----------------------------------------

This module contains basic regression module
"""
import statsmodels.api as sm


def ols(y_input: object, x_input: object) -> object:
    return sm.OLS(y_input, sm.add_constant(x_input)).fit()


def gls(y_input: object, x_input: object) -> object:
    return sm.GLS(y_input, sm.add_constant(x_input)).fit()
