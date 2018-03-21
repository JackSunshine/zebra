import utils


class GrowthAbility(object):

    def __init__(self, profit, years):
        self.profit = profit
        self._increase_rate_of_business_revenue = []
        self._net_profit_growth_rate = []
        self._net_capital_growth_rate = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        for current_year, last_year in zip(years, years[1:]):
            current_income = self.profit.total_operating_income(current_year)
            last_income = self.profit.total_operating_income(last_year)
            current_net_profit = self.profit.net_profit(current_year)
            last_net_profit = self.profit.net_profit(last_year)
            self._increase_rate_of_business_revenue.append((current_income - last_income) / last_income)
            self._net_profit_growth_rate.append((current_net_profit - last_net_profit) / last_net_profit)

    def increase_rate_of_business_revenue(self):
        return self._increase_rate_of_business_revenue

    def net_profit_growth_rate(self):
        return self._net_profit_growth_rate

    def net_capital_growth_rate(self):
        return self._net_capital_growth_rate
