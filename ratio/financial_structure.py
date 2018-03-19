

class FinancialStructure(object):

    def __init__(self, balance_sheet, years):
        self.balance_sheet = balance_sheet
        self.debt_to_assets_ratio = []

        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):

        self.debt_to_assets_ratio = [self.balance_sheet.total_liabilities(year) /
                                     self.balance_sheet.total_assets(year)
                                     for year in years]

    def debt_to_assets_ratio(self, years):

        return self.debt_to_assets_ratio

    def longterm_capital_to_property_equipment_ratio(self, years):
        return []
