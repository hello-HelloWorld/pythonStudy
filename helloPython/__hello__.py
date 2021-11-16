# -*- coding:utf-8 -*-
# coding=utf-8

print("hello python")

num1 = 4
num2 = 5.3
result = num1 + num2
print(result)
print (type(num1))
print (type(num2))

# 查看关键字
import keyword

print (keyword.kwlist)

# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print"hello", "python"
print '100 + 200 =', 100 + 200
print ('hi,%s,you have %d' % ('python', 666))

# 输入的都作为字符串
# shuru=raw_input("aa")
# 输入的都作为表达式
# shuru2=input(1+2)
# print (shuru)
# print (shuru2)

# if elif else
age = 6
if age >= 18:
    print'your age 大于18'
elif age >= 6:
    print 'your age is', age
else:
    print 'aa'

# birth = input("birth:")
# birth=int(birth)
# if birth<2000:
#     print '00前'
# else:
#     print '00后'

# while循环
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print '和为%d' % sum

# for循环
for letter in 'python':
    print '当前字母：', letter

fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
    print '水果：', fruit

for index in range(len(fruits)):
    print '水果：', fruits[index]

# break结束循环
i2 = 1
while i2 < 100:
    print i2
    i2 += 1
    if i2 > 10:
        break
print 'end'

# continue 结束本次循环，执行下一次
i3 = 1
while i3 < 10:
    i3 += 1
    if i3 % 2 == 0:
        continue
    print i3

# 字符串
name = 'abcdef'
print name[2]  # c
print name[1:3]  # bc
print name[2:]  # cdef

print name.find('bc', 0, len(name))
print name.index('bc', 0, len(name))
print name.count('bc', 0, len(name))
name2 = name.replace('bc', 'zz')
print name2

# 列表
list = ['aa', 'bb', 'cc']
print len(list)

a = [1, 2]
b = [3, 4]
a.append(b)
print a
