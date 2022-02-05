import pyupbit

access = "dD3wt0TXI4Fi8zaNY4RtxvMS18EM7MdxssjNeWxx"
secret = "X851zHL4PHe4QCei4fj3q8xQJW9cpf0htiEU95tL"
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-XRP"))  # 내 지갑에 있는걸 보여준다.
print(upbit.get_balance("KRW"))
