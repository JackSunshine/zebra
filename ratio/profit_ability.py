

class ProfitAbility(object):

    def __init__(self, balance_sheet, cash_flow, profit_statement, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        self.profit = profit_statement

        self._roe = []
        self._gross_margin = []
        self._operating_profit_rate = []
        self._net_profit_rate = []
        self._operating_expense_rate = []
        self._operation_safety_rate = []
        self._basic_per_share = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        for current_year, last_year in zip(years, years[1:] + [None]):
            income = self.profit.total_operating_income(current_year)
            cost = self.profit.operating_costs(current_year)

            self._roe.append(self.profit.net_profit(current_year) /
                            self.balance_sheet.equity(current_year))
            self._gross_margin.append((income - cost) / income)
            self._operating_profit_rate.append(self.profit.operating_profit(current_year) /
                                               income)
            self._net_profit_rate.append(self.profit.net_profit(current_year) /
                                         income)
            self._operating_expense_rate.append(((income - cost) / income) -
                                                (self.profit.operating_profit(current_year) /
                                                 income))
            self._operation_safety_rate.append((self.profit.operating_profit(current_year) / income) /
                                               ((income - cost) / income))
            self._basic_per_share.append(self.profit.basic_per_share(current_year))

    def roe(self):
        return self._roe

    def gross_margin(self):
        return self._gross_margin

    def operating_profit_rate(self):
        return self._operating_profit_rate

    def net_profit_rate(self):
        return self._net_profit_rate

    def operating_expense_rate(self):
        return self._operating_expense_rate

    def operation_safety_rate(self):
        return self._operation_safety_rate

    def basic_per_share(self):
        return self._basic_per_share


