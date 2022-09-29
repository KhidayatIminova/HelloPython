# a = int(input('Введите a: '))
# b = int(input('Введите b: '))

# if a==b*b or b==a*a:
#     print ('да')
# else:
#     print('Нет')


# a = 5

# array = []
# for i in range (a):
#     z = int(input('Введите число: '))
#     array.append(z)

# print(array)

# num = 0

# for i in array:
#     if array[i] > num:
#         num = array[i]
# print (num)

from random import randint
count = 5
nums = [randint(1,20) for i in range(count)]
print (nums)
# my_max = nums[0]
my_max = 0
# my_min = nums[0]
for i in range(count):
    if nums[i]>my_max:
        my_max = nums[i]
    # if nums[i]<my_min:
    #     my_min = nums[i]
# print ('Max', my_max, 'Min', my_min)
print ('Max', my_max)

# Программа, которая принимает на вход дробь и показывает первую цифру дробной части числа
# 6.72 --> 7, 5.345 --> 3, 4 --> нет

num = input('Введите число: ')
for i in num:
    count +=1
    if i=='.' or i ==',':
        print(num[count])
