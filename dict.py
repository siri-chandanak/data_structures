# Dictionaries
# Mutable
'''
Operation ---> Average Case

k in d ---> O(1)
Copy[3] ---> O(n)
Get Item ---> O(1)
Set Item[1] ---> O(1)
Delete Item ---> O(1)
Iteration[3] ---> O(n)
'''

dict1 = {i: False for i in "ABCDEFGHIK"}
print(dict1)

dict2={i:i**i for i in range(1,10)}
print(dict2)

print(dict1['A'])

dict1['A'] = True

dict1['Z'] = dict1.get('Z',True)
print(dict1)

print('A' in dict1)
print('S' in dict1)

dict2=dict1
dict3=dict1.copy()

print(id(dict1))
print(id(dict2))
print(id(dict3))

del dict1['A']
print(dict1)

dict1.pop('E')
print(dict1)

dict1.popitem()
print(dict1)

for i in dict1.items():
    print(i)

for i in dict1.keys():
    print(i)