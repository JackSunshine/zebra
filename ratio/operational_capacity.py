

class OperationalCapacity(object):

    def __init__(self, balance_sheet, cash_flow, profit_statement, years):
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
        self.profit = profit_statement

        self.total_asset_turnover = []
        self.accounts_receivable_turnover = []
        self.accounts_receivable_turnover_days = []
        self.inventory_turnover = []
        self.inventory_turnover_days = []
        self.business_cycle = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        for current_year, last_year in zip(years, years[1:] + [None]):
            income = self.profit.total_operating_income(current_year)
            cost = self.profit.operating_costs(current_year)

            average_total_asset = self.balance_sheet.total_assets(current_year)
            average_accounts = self.balance_sheet.bill_receivable(current_year) + \
                               self.balance_sheet.accounts_receivable(current_year)
            average_inventory = self.balance_sheet.inventory(current_year)

            if last_year:
                average_total_asset = (self.balance_sheet.total_assets(current_year) +
                                       self.balance_sheet.total_assets(last_year)) / 2

                average_accounts = (self.balance_sheet.bill_receivable(current_year) +
                                    self.balance_sheet.accounts_receivable(current_year) +
                                    self.balance_sheet.bill_receivable(last_year) +
                                    self.balance_sheet.accounts_receivable(last_year)) / 2

                average_inventory = (self.balance_sheet.inventory(current_year) +
                                     self.balance_sheet.inventory(last_year)) / 2

            self.total_asset_turnover.append(income / average_total_asset)
            if average_accounts != 0:
                self.accounts_receivable_turnover.append(income / average_accounts)
                self.accounts_receivable_turnover_days.append(360 / (income / average_accounts))
            else:
                self.accounts_receivable_turnover.append(0)
                self.accounts_receivable_turnover_days.append(0)

            if average_inventory != 0:
                self.inventory_turnover.append(cost / average_inventory)
                self.inventory_turnover_days.append(360 / (cost / average_inventory))
            else:
                self.inventory_turnover.append(0)
                self.inventory_turnover_days.append(0)

            if average_accounts != 0 and average_inventory != 0:
                self.business_cycle.append(360 / (income / average_accounts) + 360 / (cost / average_inventory))

    def accounts_receivable_turnover(self):
        return self.accounts_receivable_turnover

    def accounts_receivable_turnover_days(self):
        return self.accounts_receivable_turnover_days

    def inventory_turnover(self):
        return self.inventory_turnover

    def inventory_turnover_days(self):
        return self.inventory_turnover_days

    def total_business_cycle(self):
        return self.business_cycle

    def total_asset_turnover(self):
        return self.total_asset_turnover
