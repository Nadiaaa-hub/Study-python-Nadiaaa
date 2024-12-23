#Списки з даними
nums = [5, 7, 4, 6.76, 7]
nums [0] = 34.4
#print (nums[3])

nums2 = [4, 5, 6 , [9, 'text', True]]
#print (nums2[-2])

nums.append(33) #додає до списку ще одне значення в кінці
nums.insert(1,False)
#nums.extend ([nums2]) #дадати інший список
nums.sort() #сортування
nums.reverse()
nums.pop() # видалення останього числа
nums.remove(6.76) # видалення числа
#nums.clear() #видалення всіх чисел
print (nums)
print (nums.count(7)) #скілки чисел  7 в списку
print(len(nums))

print ('\n\n')
#Списки та цикли
nums = [5, 3, 2, 6.6]

for el in nums:
    res = el ** 2
    print(res)

print ('\n\n')
#Практичне використання
user_count_hobby = int(input ('Enter hobby number:'))
i = 0
hobby = []
while i < user_count_hobby:
    text = 'Enter hobby:' + str(i + 1) + ':'
    hobby.append (input(text))

    i+=1

    print (hobby)