import logging
from .observer import Observer
import json
import time
import os
from brokers import kkex_bch_btc
import math
import random
import sys
import traceback
import config
from .basicbot import BasicBot
import threading

class PriceMonitor(Observer):
    out_dir = './'

    def __init__(self):
        super().__init__()
        self.OKCoin_BTC_CNY = 'OKCoin_BTC_CNY'
        self.OKEx_Future_Quarter = 'OKEx_Future_Quarter'
        self.rate = 6.5754

    def tick(self, depths):

        OKEx_Future_Quarter_bid = (depths[self.OKEx_Future_Quarter]["bids"][0]['price'])
        OKCoin_BTC_CNY_ask = (depths[self.OKCoin_BTC_CNY]["asks"][0]['price'])

        diff = int(OKEx_Future_Quarter_bid*self.rate - OKCoin_BTC_CNY_ask)

        logging.info("refer_bid_price, refer_ask_price=(%s/%s), diff=%s" % (OKEx_Future_Quarter_bid*self.rate, OKCoin_BTC_CNY_ask, diff))
       
        need_header = False

        filename = self.out_dir + 'diff.csv'

        if not os.path.exists(filename):
            need_header = True

        fp = open(filename, 'a+')

        if need_header:
            fp.write("timestamp, diff\n")

        fp.write(("%d") % time.time() +','+("%.2f") % diff +'\n')
        fp.close()

        return

  