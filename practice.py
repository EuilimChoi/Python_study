a = "good to see you \n bro~"
b = "\nwhat?"

print(a+b)
print(a*100)
print(a[::-2])

number = 10
day = 3


name = 'chldmlfa'
age = 33

a = "number = %s, day = %s" % (number, day)
b = "age = {age}, name = {name}" .format(name=name, age=age)
c = f"age={age},name = {name}"
print(a)
print(b)
print(c)

a = ['a', 'b', 'c', 'd']
a.append('e')
a.sort()
a.reverse()
a.insert(0, 1)
a.remove('a')
b = a.count(1)
a.extend([1, 2, 3, 4, 5, 6])
print(a)
