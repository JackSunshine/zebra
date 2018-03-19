

class DebtPayingAbility(object):

    def __init__(self, balance_sheet, cash_flow, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow

        self.current_ratio = []
        self.quick_ratio = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        pass

    def current_ratio(self):
        return self.current_ratio

    def quick_ratio(self):
        return self.quick_ratio
