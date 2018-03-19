import statements.balance_sheet as balance_sheet
import statements.cash_flow as cash_flow
import statements.profit_statement as profit_statement
import ratio.asset_liability_ratio as asset_liability_ratio
import ratio.cash_flow_ratio as cash_flow_ratio
import ratio.debtpaying_ability as debtpaying_ability
import ratio.financial_structure as financial_structure
import ratio.growth_ability as growth_ability
import ratio.operational_capacity as operational_capacity
import ratio.profit_ability as profit_ability

class PipeLine(object):

    def __init__(self, code, years):
        self.balance_sheet = balance_sheet.BalanceSheet(code, years)
        self.cash_flow = cash_flow.CashFlow(code, years)
        self.profit = profit_statement.ProfitStatement(code, years)

        self.asset_liability_ratio = asset_liability_ratio.AssetLiabilityRatio

    def _filter_by_esp(self):
        if self.basic_per_share[0] < 0.8:
            return False
        return True

    def _filter_by_cash_flow_ratio(self):
        for ratio in self.cash_flow_ratio:
            if ratio < 0.1:
                return False
        return True

    def _filter_by_cash_flow(self):
        for cash_flow in self.net_cash_flow_operating:
            if cash_flow < 0:
                return False
        return True

    def _filter_by_gpr_and_npr(self):
        for rate in self.net_profit_rate:
            if rate < 0.1:
                return False
        return True

    def _filter_by_debt_to_assets_ratio(self):
        for rate in self.debt_to_assets_ratio:
            if rate > 0.5:
                return False
        return True

    def _filter_by_cash_to_assets_ratio(self):
        for ratio in self.cash_to_total_asset_ratio:
            if ratio < 0.2:
                return False
        return True

    def filter(self):
        if not self._filter_by_cash_flow():
            return False
        if not self._filter_by_cash_flow_ratio():
            return False
        if not self._filter_by_cash_to_assets_ratio():
            return False
        if not self._filter_by_debt_to_assets_ratio():
            return False
        if not self._filter_by_gpr_and_npr():
            return False
        if not self._filter_by_esp():
            return False
        if not self._filter_by_gpr_and_npr():
            return False
        return True
