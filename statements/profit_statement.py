# -*- coding: utf-8 -*
import tushare as ts
import utils

profit_statements_index = {
    'total_operating_income': 1,
    'total_operating_costs': 3,
    'operating_costs': 4,
    'operating_profit': 14,
    'net_profit': 20,
    'basic_per_share': 24

}


class ProfitStatement(object):

    def __init__(self, code, years):
        self.profit_statements = None
        self._make_profit_statements(code, years)

    @utils.retry_after_sleep
    def _make_profit_statements(self, code, years):
        profits = ts.get_profit_statement(code)
        self.profit_statements = {year: utils.convert_to_float(profits[year]) for year in years}

    def total_operating_income(self, year):
        return self.profit_statements[year][profit_statements_index['total_operating_income']]

    def total_operating_costs(self, year):
        return self.profit_statements[year][profit_statements_index['total_operating_costs']]

    def operating_costs(self, year):
        return self.profit_statements[year][profit_statements_index['operating_costs']]

    def operating_profit(self, year):
        return self.profit_statements[year][profit_statements_index['operating_profit']]

    def net_profit(self, year):
        return self.profit_statements[year][profit_statements_index['net_profit']]

    def basic_per_share(self, year):
        return self.profit_statements[year][profit_statements_index['basic_per_share']]
