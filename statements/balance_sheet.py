# -*- coding: utf-8 -*
import tushare as ts
import utils


balance_sheet_index = {
    'cash': 2,
    'bill_receivable': 5,
    'accounts_receivable': 6,
    'prepayments': 7,
    'inventory': 12,
    'total_current_assets': 18,
    'total_fixed_assets': 39,
    'total_assets': 40,
    'bill_payables': 44,
    'payables': 45,
    'total_current_liabilities': 58,
    'total_fixed_liabilities': 69,
    'total_liabilities': 70,
    'equity': 82
}


class BalanceSheet(object):

    def __init__(self, code, years):
        self.balance_sheets = None
        self._make_balance_sheets(code, years)

    @utils.retry_after_sleep
    def _make_balance_sheets(self, code, years):
        balances = ts.get_balance_sheet(code)
        self.balance_sheets = {year: utils.convert_to_float(balances[year]) for year in years}

    def cash(self, year):
        return self.balance_sheets[year][balance_sheet_index['cash']]

    def bill_receivable(self, year):
        return self.balance_sheets[year][balance_sheet_index['bill_receivable']]

    def accounts_receivable(self, year):
        return self.balance_sheets[year][balance_sheet_index['accounts_receivable']]

    def prepayments(self, year):
        return self.balance_sheets[year][balance_sheet_index['prepayments']]

    def inventory(self, year):
        return self.balance_sheets[year][balance_sheet_index['inventory']]

    def total_current_assets(self, year):
        return self.balance_sheets[year][balance_sheet_index['total_current_assets']]

    def total_fixed_assets(self, year):
        return self.balance_sheets[year][balance_sheet_index['total_fixed_assets']]

    def total_assets(self, year):
        return self.balance_sheets[year][balance_sheet_index['total_assets']]

    def bill_payables(self, year):
        return self.balance_sheets[year][balance_sheet_index['bill_payables']]

    def payables(self, year):
        return self.balance_sheets[year][balance_sheet_index['payables']]

    def total_current_liabilities(self, year):
        return self.balance_sheets[year][balance_sheet_index['total_current_liabilities']]

    def total_fixed_liabilities(self, year):
        return self.balance_sheets[year][balance_sheet_index['total_fixed_liabilities']]

    def total_liabilities(self, year):
        return self.balance_sheets[year][balance_sheet_index['total_liabilities']]

    def equity(self, year):
        return self.balance_sheets[year][balance_sheet_index['equity']]
