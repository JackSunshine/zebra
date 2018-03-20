

class AssetLiabilityRatio(object):

    def __init__(self, balance_sheet, years):
        self.balance_sheet = balance_sheet

        self.cash_to_total_asset_ratio = []
        self.ar_to_total_asset_ratio = []
        self.inventory_to_total_asset_ratio = []
        self.current_asset_to_total_asset_ratio = []
        self.fixed_asset_to_total_asset_ratio = []

        self.payables_to_total_asset_ratio = []
        self.current_liability_to_total_asset_ratio = []
        self.fixed_liability_to_total_asset_ratio = []
        self.equity_to_total_asset_ratio = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):
        for current_year, last_year in zip(years, years[1:] + [None]):
            total_assets = self.balance_sheet.total_assets(current_year)

            cash_equity = self.balance_sheet.cash(current_year) + \
                          self.balance_sheet.prepayments(current_year)
            self.cash_to_total_asset_ratio.append(cash_equity / total_assets)

            accounts = self.balance_sheet.bill_receivable(current_year) + \
                       self.balance_sheet.accounts_receivable(current_year)
            self.ar_to_total_asset_ratio.append(accounts / total_assets)

            self.inventory_to_total_asset_ratio.append(self.balance_sheet.inventory(current_year) /
                                                       total_assets)
            self.current_asset_to_total_asset_ratio.append(self.balance_sheet.total_current_assets(current_year) /
                                                           total_assets)
            self.fixed_asset_to_total_asset_ratio.append(self.balance_sheet.fixed_assets(current_year) /
                                                         total_assets)

            payables = self.balance_sheet.bill_payables(current_year) + \
                       self.balance_sheet.payables(current_year)
            self.payables_to_total_asset_ratio.append(payables / total_assets)

            self.current_liability_to_total_asset_ratio.append(
                self.balance_sheet.total_current_liabilities(current_year) /
                total_assets)

            self.fixed_liability_to_total_asset_ratio.append(
                self.balance_sheet.total_fixed_liabilities(current_year) /
                total_assets)

            self.equity_to_total_asset_ratio.append(self.balance_sheet.equity(current_year) /
                                                    total_assets)

    def cash_to_total_asset_ratio(self):
        return self.cash_to_total_asset_ratio

    def ar_to_total_asset_ratio(self):
        return self.ar_to_total_asset_ratio

    def inventory_to_total_asset_ratio(self):
        return self.inventory_to_total_asset_ratio

    def current_asset_to_total_asset_ratio(self):
        return self.current_asset_to_total_asset_ratio

    def fixed_asset_to_total_asset_ratio(self):
        return self.fixed_asset_to_total_asset_ratio

    def payables_to_total_asset_ratio(self):
        return self.payables_to_total_asset_ratio

    def current_liability_to_total_asset_ratio(self):
        return self.current_liability_to_total_asset_ratio

    def fixed_liability_to_total_asset_ratio(self):
        return self.fixed_liability_to_total_asset_ratio

    def equity_to_total_asset_ratio(self):
        return self.equity_to_total_asset_ratio


