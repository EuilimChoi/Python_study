import time
from typing import List
import pyupbit
import datetime

access = "dD3wt0TXI4Fi8zaNY4RtxvMS18EM7MdxssjNeWxx"
secret = "X851zHL4PHe4QCei4fj3q8xQJW9cpf0htiEU95tL"
maincoin = pyupbit.get_tickers(fiat='KRW')


def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + \
        (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    print(ticker, target_price)
    return target_price


def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time


def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0


def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]


# 로그인
upbit = pyupbit.Upbit(access, secret)
balances = upbit.get_balances()
print("autotrade start", balances[0]['currency'])

# 자동매매 시작 왜 숫자로 변환이 안되는지 모르겠음!!!!
for coin in balances[1:]:
    money = float(coin['balance'])
    if money > 0.00008:
        upbit.sell_market_order("KRW-%s" %
                                coin['currency'], coin['currency']*0.9995)
