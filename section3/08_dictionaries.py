# Dictionarioes are key-value pairs
# my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict)  # {'key1': 'value1', 'key2': 'value2'}
# print(my_dict['key1'])  # value1
# print(my_dict['key2'])  # value2

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)  # {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])  # value1
print(my_dict['key2'])  # value2

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup['apple'])  # 2.99
print(prices_lookup['oranges'])  # 1.99
print(prices_lookup['milk'])  # 5.8

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'inside_key': 100}}
print(d['k1'])  # 123
print(d['k2'])  # [0, 1, 2]
print(d['k3'])  # {'inside_key': 100}
print(d['k3']['inside_key'])  # 100

d = {'key1': ['a', 'b', 'c']}
print(d['key1'])  # ['a', 'b', 'c']
print(d['key1'][2])  # c
print(d['key1'][2].upper())  # C

d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)  # {'k1': 100, 'k2': 200, 'k3': 300}
d['k1'] = 'NEW VALUE'
print(d)  # {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())  # dict_keys(['k1', 'k2', 'k3'])
print(d.values())  # dict_values([100, 200, 300])
print(d.items())  # dict_items([('k1', 100), ('k2', 200), ('k3', 300)])

my_list = d['key1']
print(my_list)  # ['a', 'b', 'c']
letter = my_list[2]
print(letter)  # c
print(letter.upper())  # C

