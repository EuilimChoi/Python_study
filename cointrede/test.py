import pyupbit

access = ""
secret = ""
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-XRP"))  # 내 지갑에 있는걸 보여준다.
print(upbit.get_balance("KRW"))


dic = {'name': 'limchoi', 'age': 15}
print(dic['name'])
