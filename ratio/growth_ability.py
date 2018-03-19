

class GrowthAbility(object):

    def __init__(self, balance_sheet, cash_flow, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow

        self.increase_rate_of_business_revenue = []
        self.net_profit_growth_rate = []
        self.net_capital_growth_rate = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        pass

    def increase_rate_of_business_revenue(self):
        return self.increase_rate_of_business_revenue

    def net_profit_growth_rate(self):
        return self.net_profit_growth_rate

    def net_capital_growth_rate(self):
        return self.net_capital_growth_rate
