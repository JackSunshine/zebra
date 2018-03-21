# -*- coding: utf-8 -*
import tushare as ts
import utils
import time
import filter.pipeline as pipeline
import analysis.evaluation as ev


class Stocks(object):

    def __init__(self):
        self.counter = 1
        self.stocks = {}
        self.pes = {}
        self.time_to_market = {}
        self.outstanding_to_totals = {}
        self.totals = {}
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
        self.pes = {x: y for x, y in stocks['pe'].iteritems()}
        self.time_to_market = {x: y for x, y in stocks['timeToMarket'].iteritems()}
        self.outstanding_to_totals = {x: y for x, y in (stocks.outstanding / stocks.totals).iteritems()}
        self.totals = {x: y for x, y in stocks['totals'].iteritems()}
        self.all_stocks = {x: y for x, y in stocks['name'].iteritems() if industries[x] not in ['银行', '证券', '保险']}

    @utils.retry_after_sleep
    def _get_actual_years(self, code):
        self.actual_years = []
        time.sleep(2)
        cash_flows = ts.get_cash_flow(code)
        time.sleep(2)
        self.actual_years = [year for year in self.years if year in cash_flows.columns]

    def start_washing(self):
        self._get_all_stocks()
        self._remove_st_stocks()
        result = {}
        for code, name in self.stocks_not_st.items():
            print("This is the %dth stock, code is %s" % (self.counter, code))
            self._get_actual_years(code)
            pl = pipeline.Pipeline(code, self.actual_years)
            if pl.filter():
                result[code] = name
                asset_liability_ratio, growth_ability, operational_capacity, profit_ability = \
                    pl.get_abilities()
                ev_price = ev.evaluation(self.pes.get(code), self.totals.get(code),
                                         asset_liability_ratio, operational_capacity, profit_ability)
                print("The valuable stock is %s, %s, time to market is %s,"
                      "outstanding/totals is %s, evaluated price is %s, peg is %s"
                      % (code, name, self.time_to_market.get(code, ''),
                         self.outstanding_to_totals.get(code, ''),
                         ev_price,
                         ev.latest_peg(self.pes.get(code), growth_ability)))

            self.counter = self.counter + 1
        print(result)
