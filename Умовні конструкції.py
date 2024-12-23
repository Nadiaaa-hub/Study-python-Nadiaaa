num = int(input ('Enter num:'))
# ==, <, >, <=, >=, != (#перевірка на нерівнісь)
isHasCar = False
if num >= 60 and not isHasCar:
#перевіряємо на рівність
    print ('Yes')
    print('More text')
    if num==100:
        print('num is 100')
elif num < 40:
    print ("Num is less 40")
elif num == 55:
    print ("Num is 55")
else: #якщо код не спрацьовує (пишеться в кінці)
    print('Else')

isHappy = True
if isHappy: # if not
    print('Yes, he is Happy')