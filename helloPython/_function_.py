# -*- coding:utf-8 -*-
# coding=utf-8

def printInfo():
    print '定义函数'


printInfo()


def add2num(a, b):
    c = a + b
    print c


add2num(2, 3)


def printInfo2(name, age=18):
    print 'name', name
    print 'age', age


printInfo2('张三')
printInfo2('李四', 22)


# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典
def fun(a, b, *args, **kwargs):
    print 'a=', a
    print 'b=', b
    print 'args=', args
    print 'kwargs='
    for key, value in kwargs.items():
        print key, '=', value


fun(1, 2, 3, 4, 5, m='ff', n=7, p=8)


def fun2(a, b):
    return a + b


c = fun2(1, 2)
print c


# 函数返回值也可以返回多个值
def fun3(a, b):
    jia = a + b
    jian = a - b
    return jia, jian


jia1, jian1 = fun3(3, 2)
print jia1
print jian1

# 全局变量
a = 200


# 如果全局变量和局部变量名一样，则使用的是局部变量
def test1():
    a = 30
    print 'test1-1 %d' % a
    a = 40
    print 'test1-2 %d' % a


"""
 函数中修改全局变量，那么就需要使用global进行声明，否则出错
1、如果全局变量是可变类型：所以在函数里面任意修改（值，引用）
2、如果全局变量是不可变类型：在函数里面不能修改值，也不能修改引用，除非加上global才能修改引用。
"""


def test2():
    global a
    a += 100
    print 'test2 %d' % a


test1()
test2()


# 递归函数
def test1(n):
    if n == 1:
        return 1
    return n * test1(n - 1)

print test1(4)
