from ттт import num_2

string = 'hello world!'
if 'hello' not in string:
    print('hello in string')
elif 'world' in string:
    print ('word in string')
else:
    print ('word not in string')


a = 10
b = 20
if a ==11 and b==20 or b<30:
    print (a+b)
else:
    print('wrong condition')

Test_list = ['Hello', 'test', '2',1, True]
if 'test' in Test_list and 1 in Test_list:
    print ('test 1')
elif 'Hello' in Test_list and '2' not in Test_list:
    print ('Hello is not 2')
else:
    print ('not found')

c=10
d=20
r= 'chat is active'
w = 'count of users'
if c >=d:
    print(c)
elif len(w) <= len(r):
    print(w)
else:
    print('incorrect')
print (len(w))
print (len(r))

user1 = {
    'name': 'Tom',
    'age': 21,
    'balance': 20000,
    'currency':'USD',
    'status': True
}

user2= {
    'name': 'Nina',
    'age': 15,
    'balance': 5000,
    'currency': 'EUR',
    'status': False
}

user3 = {
    'name': 'Karina',
    'age': 30,
    'balance': 100000,
    'currency': 'UAH',
    'status': True
}

list_of_currency = ['USD', 'EUR', 'UAH']

if user1 ['name'] and user1 ['age']>= 18 and user1 ['status']:
    if user1 ['balance'] >= 10000 and user1 ['currency'] in list_of_currency:
        print(f'Hello! You can create your binance account, welcome {user1['name']}')
    elif user1 ['balance'] >= 10000 and user1 ['currency'] in list_of_currency:
        print ('Ypu need more money')
    else:
        print ('money critical not enough')
elif user1 ['name']:
    print ('Please, write name in your account description')
elif user1 ['age']< 18:
    print ('For registry binance account you have to be 18 years old')
else:
    print('Something went wrong')


test_list = [1, 2, 3, 4, 5, 6]

for num in test_list:
    print(f'You got a {num**2}')

a = 0

while a <10:
    a += 1
    print (a, '-----<')

test_list1 = [1, 2, 3, 4, 5]

while (len(test_list1)) < 10:
    test_list1.append(6)
    print (test_list1)


test_list2 = ['test', 'python', 'code']

for s in test_list2:
    print (s, '------<')
    if s == 'test':
        print (s)
    elif s == 'python':
        print (s)
    else:
        print (s)

a = 0
add_list = []

while len(add_list) <10:
    print (len(add_list))
    add_list.append (a)
    a += 1
    if len(add_list) ==5:
        print ('You are at middle of list')


user_1 = {
    "user_name": 'Sarah',
    'role': 'admin',
    'account_connection': True
}

user_2 = {
    "user_name": 'Bob',
    'role': 'user',
    'account_connection': False
}

user_3 = {
    "user_name": 'Alex',
    'role': 'pro_user',
    'account_connection': True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print (f'work with {user['user_name']} account --------<')
    if not user ['account_connection']:
        count_of_tries = 10
        while  count_of_tries != 0:
            print('try to connect to user account')
            count_of_tries -= 1
            print ('Connect of tries left',count_of_tries)
    elif user ['role'] == 'admin':
            print (f'Hello in system {user['user_name']}')
    else:
        print (" Welcome on the board")

print('All users were checked!')

