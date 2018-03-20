# -*- coding: utf-8 -*
import tushare as ts
import utils

cash_flow_index = {
    'net_cash_flow_operating': 11,
    'cash_dividend': 33
}


class CashFlow(object):

    def __init__(self, code, years):
        self.cash_flows = None
        self._make_cash_flows(code, years)
        self.net_cash_flow_operating = [self.cash_flows[year][cash_flow_index['net_cash_flow_operating']]
                                        for year in years]
        self.cash_dividend = [self.cash_flows[year][cash_flow_index['cash_dividend']]
                              for year in years]

    @utils.retry_after_sleep
    def _make_cash_flows(self, code, years):
        cash_flows = ts.get_cash_flow(code)
        self.cash_flows = {year: utils.convert_to_float(cash_flows[year]) for year in years}

    def net_cash_flow_operating(self, year):
        return self.cash_flows[year][cash_flow_index['net_cash_flow_operating']]

    def cash_dividend(self, year):
        return self.cash_flows[year][cash_flow_index['cash_dividend']]
