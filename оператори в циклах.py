from _ast import If

for i in range (1,11):
    if i % 2 == 0:
        continue #(пропускає все, що ділиться на 2)
    if i == 7:
        break #вийти повністю з циклу
    print("El:", i)

print ('\n\n')

#Else в циклі
for i in "Hello word":
    if i == 'o':
        print ('Done')
        break
else:
    print("Not found")

print('\n\n')
for i in range (10,20):
    while i % 3 == 0:
        break
    print (i)
