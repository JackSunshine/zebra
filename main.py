# -*- coding: utf-8 -*
import stock
import sys

if __name__ == '__main__':
    stock = stock.Stocks()
    stock.counter = sys.argv[1]
    stock.start_washing()
