#for i in range (5):
#    print(i)

for i in range (-5,20,2): #кінцева цифра це діапазон розриву
    print(i)

print ('\n\n\n')

word = 'Some text'
for i in word:
    if i =='m':
        print ('Літера m є у тексті')

#Цикл while
#i = 100
#while i >= 10:
#    print (i)
#    i -= 10
#input()

#Практичне використання
work = True
while work:
    user_input = input('Enter word STOP:')
    if user_input == 'STOP':
        work = False

print('While loop is done')

