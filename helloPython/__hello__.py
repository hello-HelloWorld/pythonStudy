# -*- coding:utf-8 -*-
# coding=utf-8

# 多行注释，"""..."""
"""
1、可变类型，值可以改变：
列表 list
字典 dict
2、不可变类型，值不可以改变：
数值类型 int, long, bool, float
字符串 str
元组 tuple
set  （没有value的字典）
"""

print("hello python")
# '''...'''表示多行数据
print ('''a 
b
c''')

# 有了变量名和数值，不用指定类型，就能自动辨别类型
num1 = 4
num2 = 5.3
result = num1 + num2
print(result)
# type() 查看变量的类型
print (type(num1))
print (type(num2))

# 查看关键字
import keyword

print (keyword.kwlist)

# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print"hello", "python"
print '100 + 200 =', 100 + 200
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print ("hi,%s,you have %d" % ("python", 666))

# 输入的都作为字符串
# shuru = raw_input("键盘输入:")
# print (shuru)
# 输入的都作为表达式
# shuru2=input("键盘输入表达式:")
# print (shuru2)

# if elif else
age = 6
if age >= 18:
    print'your age 大于18'
elif age >= 6:
    print 'your age is', age
else:
    print 'aa'

# 输入的内容为字符串，要转换为数值类型再做比较
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
# 左闭右开
print name[1:3]  # bc
print name[2:]  # cdef

print name.find('bc', 0, len(name))
print name.index('bc', 0, len(name))
print name.count('bc', 0, len(name))
name2 = name.replace('bc', 'zz')
print name2
print name.split("c")

# 列表,索引下标从0开始,数据可以修改
list = ['aa', 'bb', 'cc']
print list[0]
print len(list)

a = [1, 2]
b = [3, 4]
a.append(b)  # [1, 2, [3, 4]]
# extend可以将另一个集合中的元素逐一添加到列表中
a.extend(b)  # [1, 2, [3, 4], 3, 4]
print a

# insert(index, object) 在指定位置index前插入元素object
b.insert(1, 5)
print b

# del：根据下标进行删除，其实可以删除所有变量
# pop：默认删除最后一个元素
# remove：根据括号中元素的值进行删除第一个
del a[0]
print a
a.pop()
print a
a.remove(3)
print a

# 排序
c = [1, 4, 2, 3]
c.sort()
print c
c.sort(reverse=True)
print c

chars = ['a', 'c', 'b', 'd']
for value in chars:
    print value
for i, chr in enumerate(chars):
    print i, chr

# 元组 和list类似，但是元素不可以修改
# 只有1个元素的tuple定义时必须加一个逗号
tuplea = (1,)
print tuplea
# 元组元素指向不变
tupleb = (1, 2, [3, 4])
tupleb[2][0] = 3.1
tupleb[2][1] = 4.1
print tupleb

# dict 字典，相当于是map
dict1 = {"aa": 1, "bb": 2}
print dict1["aa"]

bb = dict1.get("b")
print bb
# 如果不存在该键，则会用默认的值
bb = dict1.get("b", 3)
print bb
# 修改、新增元素值
dict1["aa"] = 3
print dict1
# 删除元素值
del dict1["aa"]
print dict1
# 删除字典
# del dict1
# print dict1
# 清空字典
dict1.clear()
print dict1

dict2 = {"aa": 1, "bb": 2, "cc": 3}
keys = dict2.keys()
print keys
values = dict2.values()
print values
items = dict2.items()
print items
exists = dict2.has_key("aa")
print exists
# 遍历字典
for key in dict2.keys():
    print key, dict2[key]

for value in dict2.values():
    print value

for item in dict2.items():
    print item

for key, value in dict2.items():
    print key
    print value
    print "key=%s,value=%d" % (key, value)
