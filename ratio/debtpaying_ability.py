

class DebtPayingAbility(object):

    def __init__(self, balance_sheet, cash_flow, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow

        self._current_ratio = []
        self._quick_ratio = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        self._current_ratio = [self.balance_sheet.total_current_assets(year) /
                               self.balance_sheet.total_current_liabilities(year)
                               for year in years]

        self._quick_ratio = [(self.balance_sheet.total_current_assets(year) -
                              self.balance_sheet.inventory(year) -
                              self.balance_sheet.prepayments(year)) /
                             self.balance_sheet.total_current_liabilities(year)
                             for year in years]

    def current_ratio(self):
        return self._current_ratio

    def quick_ratio(self):
        return self._quick_ratio
