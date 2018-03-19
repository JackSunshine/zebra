# -*- coding: utf-8 -*
import tushare as ts
import utils
import time
import filter.pipeline as pipeline


class Stocks(object):

    def __init__(self):
        self.counter = 1
        self.stocks = {}
        self.profit_statements = None
        self.balance_sheets = None
        self.cash_flows = None
        self.years = ['20161231', '20151231', '20141231', '20131231', '20121231']
        self.actual_years = []

    def _remove_st_stocks(self):
        self.stocks_not_st = {x: y for x, y in self.all_stocks.items() if 'ST' not in y}

    def _get_all_stocks(self):
        stocks = ts.get_stock_basics()
        industries = {x: y for x, y in stocks['industry'].iteritems()}
        self.all_stocks = {x: y for x, y in stocks['name'].iteritems() if industries[x] not in ['银行', '证券', '保险']}

    @utils.retry_after_sleep
    def _get_actual_years(self, code):
        time.sleep(2)
        cash_flows = ts.get_cash_flow(code)
        time.sleep(2)
        if (cash_flows.shape[1] - 1) // 4 >= 5:
            self.actual_years = self.years[:]
        else:
            self.actual_years = self.years[:(cash_flows.shape[1] - 1) // 4]

    def start_washing(self):
        self._get_all_stocks()
        self._remove_st_stocks()
        result = {}
        for code, name in self.stocks_not_st.items():
            print("This is the %dth stock, code is %s" % (self.counter, code))
            self._get_actual_years(code)
            if pipeline.PipeLine(code, self.actual_years).filter():
                result[code] = name
                print("The valuable stock is %s, %s"%(code, name))
            self.counter = self.counter + 1
        print(result)
