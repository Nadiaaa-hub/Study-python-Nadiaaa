a = [3,6,9,12]
a.extend([10]), a.extend([20])
print (a.remove(10))
print (a)

b = [1,4,5,7,8]
total_sum = sum(b)
print(total_sum)

list_1 = [20,30,40]
i = [number * 2 for number in list_1]
print (i)

lst = ("яблуко", "банан", "апельсин")
print (lst[0])
print (lst[1])
print (lst[2])

a = (9,4,5,6)
b = (8,4,6,7)
print (a+b)

dict_1 = {'ім''я':'Олекса́ндр Олекса́ндрович У́сик','вік':37, 'спорт':'бокс' }
print (dict_1 ['ім''я'],dict_1 ['вік'], dict_1 ['спорт'])

dict_2={'Назва книги': 'Приборкай своїх драконів','рік видання':2020}
dict_2['Назва книги'] = 'Кораліна'
print (dict_2 )

country = (input('Write the country name:'))
Country_list = {
    'Ukraine': 'Kyiv',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}


if country in Country_list :
    print (f'The capital of {country} is {Country_list[country]}')
else:
    print ('This country is not in the dictionary')

