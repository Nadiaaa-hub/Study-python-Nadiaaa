num_1 = "Hello"
print(type(num_1))
num_2 = 3
print(type(num_2))
num_3 = 5.6
print(type(num_3))
num_4 = False
print(type(num_4))
num_5 = [3, 7, 9.8, 'Gatcha']
print(type(num_5))
num_6 = {'Name':'Nadia', 'Age': '18', 'Palce': 'Kyiv'}
print(type(num_6))
num_7 = (4, 8, 4/6, 'Meow')
print(type(num_7))
print(type(None))

num_str = 125
print(type(num_str))
num_str1 = str(num_str)
print(type(num_str1))

message = 'Hi, my name is Python!'
message = (message.replace ('y', '0'))
message = (message.replace ('i', '1'))
print (message)

split_test = 'This is a split test'
print (split_test.split())
string_join = (''. join(split_test))
print (''. join(string_join))
print(len('string_join'))

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print (list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print (list_extend)
print (list_extend .index(6))

print (len('list_append'))

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print (dict_test['car'])
print (dict_test['where'])
print (dict_test.keys())
print (dict_test.values())
print (dict_test.items())