
correct_password = 'password123'
password = input('Enter the password:')

if password == correct_password:
    print ('You are logged in')
else:
    print ('Wrong password')


day_in_week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
day_number = int(input('Enter day number (1-7):'))
if day_number == 1:
    print ("Monday")
elif day_number == 2:
    print ("Tuesday")
elif day_number == 3:
    print  ("Wednesday")
elif day_number == 4:
    print  ("Thursday")
elif day_number == 5:
    print  ("Friday")
elif day_number == 6:
    print  ("Saturday")
elif day_number == 7:
    print  ("Sunday")
else:
    print("Incorrect day number. Please enter a number between 1 and 7.")


for i in range (1, 11):
    print (i)


a = 30
b = 2
c = (a**b)
if a > 10 and b == 2:
    print (a+b+c)
else:
    print('wrong condition')

number = input('Enter number')
for i in range (1,10):
    print(f'{number}*{i}')