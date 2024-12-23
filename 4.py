a = [1, 2 ,3 ,4 ,5]
b = ['apple', 'banana', 'cherry']

print (a[0], a [1], a[-1]) #-1 це перша цифра з кінця
print (b[2],)

print (a[1:4], a[::2])
print (b[::2])

#перевернути список з кінця
print (a[::-1])
print (b[::-1])

#Методи списків
a.append(6) #додає до кінця списку
b.append('tomato')
print (a,b)

a.insert (2, 7.4) #вставляє між списками
b.insert (3, 'bottle')
print (a,b)

a.remove (7.4) # видаляє значення
b.remove ('bottle')
print (a,b)

last_elem_1 = a.pop ()#видаляє 'останній' елемент
last_elem_2 = b.pop ()
print (last_elem_1,last_elem_2) #показує яку позицію ми видалили

print (a.index (3), b.index ('banana')) #визначає індекс (по порядку)

a.extend([5,5,5]) #додає до списку
b.extend(['cherry','banana', 'banana' ])
print (a.count (5), b.count ('banana'), b.count ('cherry'))
print (a,b)

a.sort(reverse = True)
b.sort(reverse = True)
print (a,b)
a.reverse()
b.reverse()
print (a,b)
