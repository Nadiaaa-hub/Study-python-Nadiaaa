a = (1, 2, 3, 4, 5,5)
print (a[0], a[1], a[2])
print (a[:2], a [-2:])

print (a.count(5))
a.index (5)
print (a.index (5))

#Словникики
test_dict = {'user': 'Yurii', 'age': 29, 'country': 'Ukraine'}
print (test_dict['user'], test_dict['age'], test_dict['country'])
print (test_dict.get ('animal', 'key not found'))
test_dict['age'] = 30
print (test_dict['age'])
test_dict['animal'] = 'cat'
print (test_dict['animal'])
animal = test_dict.pop ('animal')
print (test_dict)
print (animal)

copy_test = test_dict.copy()
test_dict.clear()
print (test_dict)
print (copy_test)

for key, value in copy_test.items():
    print (f'Key: {key}, Value: {value}')

wrong_key = copy_test.pop('currency', 'key not found') #дефолтне значення
print (wrong_key)

dict_update = {'new role': 'admin', 'salary':10000}
copy_test.update(dict_update)
print (copy_test)
