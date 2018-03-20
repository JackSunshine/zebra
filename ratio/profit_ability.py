

class ProfitAbility(object):

    def __init__(self, balance_sheet, cash_flow, profit_statement, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        self.profit = profit_statement

        self.roe = []
        self.gross_margin = []
        self.operating_profit_rate = []
        self.net_profit_rate = []
        self.operating_expense_rate = []
        self.operation_safety_rate = []
        self.basic_per_share = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        for current_year, last_year in zip(years, years[1:] + [None]):
            income = self.profit.total_operating_income(current_year)
            cost = self.profit.operating_costs(current_year)

            self.roe.append(self.profit.net_profit(current_year) /
                            self.balance_sheet.equity())
            self.gross_margin.append((income - cost) / income)
            self.operating_profit_rate.append(self.profit.operating_profit(current_year) /
                                              income)
            self.net_profit_rate.append(self.profit.net_profit(current_year) /
                                        income)
            self.operating_expense_rate.append(((income - cost) / income) -
                                               (self.profit.operating_profit(current_year) /
                                               income))
            self.operation_safety_rate.append((self.profit.operating_profit(current_year) / income) /
                                              ((income - cost) / income))
            self.basic_per_share.append(self.profit.basic_per_share(current_year))

    def roe(self):
        return self.roe

    def gross_margin(self):
        return self.gross_margin

    def operating_profit_rate(self):
        return self.operating_profit_rate

    def net_profit_rate(self):
        return self.net_profit_rate

    def operating_expense_rate(self):
        return self.operating_expense_rate

    def operation_safety_rate(self):
        return self.operation_safety_rate

    def basic_per_share(self):
        return self.basic_per_share


