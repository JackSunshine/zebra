

class CashFlowRatio(object):

    def __init__(self, balance_sheet, cash_flow, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        self._cash_flow_ratio = []
        self._cash_flow_adequacy_ratio = []
        self._cash_reinvestment_ratio = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):

        self._cash_flow_ratio = [self.cash_flow.net_cash_flow_operating(year) /
                                 self.balance_sheet.total_current_liabilities(year)
                                for year in years]
        self._cash_flow_adequacy_ratio = []
        self._cash_reinvestment_ratio = [(self.cash_flow.net_cash_flow_operating(year) -
                                          self.cash_flow.cash_dividend(year)) /
                                         (self.balance_sheet.total_assets(year) -
                                          self.balance_sheet.total_current_liabilities(year))
                                         for year in years]

    def cash_flow_ratio(self):
        return self._cash_flow_ratio

    def cash_flow_adequacy_ratio(self):
        return self._cash_flow_adequacy_ratio

    def cash_reinvestment_ratio(self):
        return self._cash_reinvestment_ratio
