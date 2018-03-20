

class FinancialStructure(object):

    def __init__(self, balance_sheet, years):
        self.balance_sheet = balance_sheet
        self._debt_to_assets_ratio = []
        self._long_term_capital_to_property_equipment_ratio = []
        self._generate_analysis_data(years)

    def _generate_analysis_data(self, years):

        self._debt_to_assets_ratio = [self.balance_sheet.total_liabilities(year) /
                                      self.balance_sheet.total_assets(year)
                                      for year in years]
        self._long_term_capital_to_property_equipment_ratio = \
            [(self.balance_sheet.equity(year) +
              self.balance_sheet.total_fixed_liabilities(year)) /
             (self.balance_sheet.fixed_assets(year) +
             self.balance_sheet.construction_in_progress(year) +
             self.balance_sheet.engineer_material(year))
             for year in years]

    def debt_to_assets_ratio(self):
        return self._debt_to_assets_ratio

    def long_term_capital_to_property_equipment_ratio(self):
        return self._long_term_capital_to_property_equipment_ratio
