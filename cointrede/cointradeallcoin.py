import time
from typing import List
import pyupbit
import datetime

access = "dD3wt0TXI4Fi8zaNY4RtxvMS18EM7MdxssjNeWxx"
secret = "X851zHL4PHe4QCei4fj3q8xQJW9cpf0htiEU95tL"
maincoin = pyupbit.get_tickers(fiat='KRW')


def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=7)
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

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        for coin in maincoin:
            if start_time < now < end_time - datetime.timedelta(seconds=10):
                target_price = get_target_price(coin, 0.5)
                current_price = get_current_price(coin)
                if target_price < current_price:
                    krw = get_balance("KRW")
                    if krw > 5000:
                        print(coin, '산다아아아아아아')
                        #upbit.buy_market_order(coin, krw*0.9995)
            else:
                balances = upbit.get_balances()
                for coin in balances[1:]:
                    coin['currency'] = get_balance(coin['balance'])
                    btc = get_balance(coin)
                    if btc > 0.00008:
                        upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
