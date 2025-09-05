# lis = ['a', 'b', 'c', 'd', 'e']

# for ch in lis:
#     print(ch)

dict = {'apple' : 1200, 'banana' : 800, 'orange' : 1500}

# for key in dict.items():
#     print(key)

items = dict.items()
for key, value in items:
    print(key, value)

values = dict.values()

for value in values:
    print(value)

keys = dict.keys()

for key in keys:
    print(key)