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


class Pipeline(object):

    def __init__(self, code, years):
        self.balance_sheet = balance_sheet.BalanceSheet(code, years)
        self.cash_flow = cash_flow.CashFlow(code, years)
        self.profit = profit_statement.ProfitStatement(code, years)

        self.asset_liability_ratio = asset_liability_ratio.AssetLiabilityRatio(self.balance_sheet,
                                                                               years)
        self.cash_flow_ratio = cash_flow_ratio.CashFlowRatio(self.balance_sheet,
                                                             self.cash_flow,
                                                             years)
        self.debtpaying_ability = debtpaying_ability.DebtPayingAbility(self.balance_sheet,
                                                                       self.cash_flow,
                                                                       years)
        self.financial_structure = financial_structure.FinancialStructure(self.balance_sheet,
                                                                          years)
        self.growth_ability = growth_ability.GrowthAbility(self.balance_sheet,
                                                           self.cash_flow,
                                                           years)
        self.operational_capacity = operational_capacity.OperationalCapacity(self.balance_sheet,
                                                                             self.cash_flow,
                                                                             self.profit,
                                                                             years)
        self.profit_ability = profit_ability.ProfitAbility(self.balance_sheet,
                                                           self.cash_flow,
                                                           self.profit,
                                                           years)

    def _filter_by_esp(self):
        if self.profit_ability.basic_per_share[0] < 0.8:
            return False
        return True

    def _filter_by_cash_flow_ratio(self):
        for ratio in self.cash_flow_ratio.cash_flow_ratio:
            if ratio < 0.1:
                return False
        return True

    def _filter_by_cash_flow(self):
        for net_cash in self.cash_flow.all_net_cash_flow_operating():
            if net_cash < 0:
                return False
        return True

    def _filter_by_gpr_and_npr(self):
        for rate in self.profit_ability.net_profit_rate():
            if rate < 0.1:
                return False
        return True

    def _filter_by_debt_to_assets_ratio(self):
        for rate in self.financial_structure.debt_to_assets_ratio():
            if rate > 0.5:
                return False
        return True

    def _filter_by_cash_to_assets_ratio(self):
        for ratio in self.asset_liability_ratio.cash_to_total_asset_ratio():
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
