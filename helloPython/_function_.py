# -*- coding:utf-8 -*-
# coding=utf-8

def printInfo():
    print '定义函数'
printInfo()

def add2num(a,b):
    c=a+b
    print c
add2num(2,3)

def printInfo2(name,age=18):
    print 'name',name
    print 'age',age
printInfo2('张三')
printInfo2('李四',22)

def fun(a,b,*args,**kwargs):
    print 'a=',a
    print 'b=',b
    print 'args=',args
    print 'kwargs='
    for key,value in kwargs.items():
        print key,'=',value
fun(1,2,3,4,5,m=6,n=7,p=8)

def fun2(a,b):
    return a+b
c=fun2(1,2)
print c

def fun3(a,b):
    jia=a+b
    jian=a-b
    return jia,jian
jia1,jian1=fun3(3,2)
print jia1
print jian1

#全局变量
a=200
def test1():
    a=30
    print 'test1-1 %d'%a
    a=40
    print 'test1-2 %d'%a
def test2():
    global a
    a+=100
    print 'test2 %d'%a
test1()
test2()