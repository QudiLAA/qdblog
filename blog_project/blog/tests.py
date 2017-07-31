#coding:utf-8
from django.test import TestCase

# Create your tests here.
#用 Python 编写一个 decorator，@retry(retry_num)，如果被修饰的函数抛异常则进行重试，
# 直到函数不再抛异常或重试次数已经达到 retry_num
# count=0
# def retry(retry_num,aClass,*args):
#     if count>=retry_num:
#         return aClass
#     try:
#         aClass()
#     except Exception as e:
#         print e
#         retry(retry_num,aClass)
#
# #一个 dict 中存放了学校学生的考试成绩，key 是名字，value 是成绩，
# # 例如：score= {"zhangsan":62,"lisi":59,"xiaoming":61}，用 Python 实现按成绩从高到低打印名字和对应成绩
# score= {"zhangsan":62,"lisi":59,"xiaoming":61,"xiaoming2":40}
# result=sorted(score.iteritems(),key=lambda asd:asd[1],reverse=True)
# for i in result:
#     print ('%s:%s')%(i[0],i[1])
# print result
#
# # for k,v in score.items():
# #     print k,v
# #     l1.append(k)
# #     l2.append(v)
# #     print l1,l2
# # max_num=l2[0]
# # for i in l2:
# #     if i>max_num:
# #         test_num=i

#
# def func(x,l=[1,3,5]):
#     for item in xrange(1,x):
#         print l
#  #       print item
#         print item**item
#         l.append(item**item)
#     print l
# # func(2)
# #func(3,[0])
# func(3)

# import os
# import os.path
#
# path='C:/'
# filea='a'
# fileb='b'
# for file in filea:
#     print os.path.join(path,filea)
#     for file2 in fileb:
#         if file is file2:
#             if os.path.isdir(file):
#                 pass

# ls=[]
# sum=0
# b=0
# n=int(raw_input('n:\n'))
# a=int(raw_input('a:\n'))
# b=a
# for i in range(n):
#     sum=sum+b
#     b=b*10+a
#     print('%d+')%b
# # print sum
#
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# if __name__ == '__main__':
#     from Tkinter import *
#
#     canvas = Canvas(width=800, height=600, bg='yellow')
#     canvas.pack(expand=YES, fill=BOTH)
#     k = 1
#     j = 1
#     for i in range(0,10):
#         canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
#         k += j
#         j += 0.3
#
#     mainloop()

#!/usr/bin/python# -*- coding: UTF-8 -*-
# if __name__ == '__main__':
#     a = []
#     for i in range(10):
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     for i in range(10):
#         a[i][0] = 1
#         a[i][i] = 1
#     for i in range(2,10):
#         for j in range(1,i):
#             a[i][j] = a[i - 1][j-1] + a[i - 1][j]
#     from sys import stdout
#     for i in range(10):
#         for j in range(i + 1):
#             stdout.write(str(a[i][j]))
#             stdout.write(' ')
#         print
#
# def triangles():
#     ret = [1]
#     while True:
#         yield ret
#         for i in range(1, len(ret)):
#             ret[i] = pre[i] + pre[i - 1]
#         ret.append(1)
#         pre = ret[:]
# ls=triangles()
# print type(ls)
#
# for i in ls:
#     print i

# #!/usr/bin/python# -*- coding: UTF-8 -*-
# #杨辉三角
# if __name__ == '__main__':
#     a = []
#     for i in range(10):
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     for i in range(10):
#         a[i][0] = 1
#         a[i][i] = 1
#     for i in range(2,10):
#         for j in range(1,i):
#             a[i][j] = a[i - 1][j-1] + a[i - 1][j]
#     # from sys import stdout
#     # for i in range(10):
#     #     for j in range(i + 1):
#     #         stdout.write(str(a[i][j]))
#     #         stdout.write(' ')
#     #     print
#     for i in range(0,10):
#         for j in range(0,10):
#             if a[i][j]!=0:
#                 print a[i][j],
#                 if i==j:
#                    print
#


# #有n个整数的数组，写一个函数使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# def move(arry,n,m):
#     arry_end=arry[n-1]
#     for i in range(n-1,-1,-1):
#         arry[i]=arry[i-1]
#     arry[0]=arry_end
#     m-=1
#     if m>0:
#         move(arry,n,m)
#
# l=[1,2,3,4,5,6,7,8,9]
# n=len(l)
# move(l,n,2)
# print l

# def odd(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%2!=0:
#             sum=1.0/i+sum
#     return sum
#
# def even(n):
#     sum=0
#     for i in range(2,n+1):
#         if i%2==0:
#             print 1.0/i
#             sum=1.0/i+sum
#     return sum
#
# def main():
#     n=int(raw_input('请输入：'))
#     if n%2==0:
#         print even(n)
#     else:
#         print odd(n)
# if __name__ == '__main__':
#     main()

# words = ['This','is','a','dog','!']
# words.sort(key=lambda x:x.lower())
# print words

# alist = ['a','s','d','f']
# try:
#     alist.index('a1')
#     print 'find it'
# except:
#     print 'no find'
#

# l=[2,3]
# for i in range(100):
#     l.append(i)
# print l
# b=list(set(l))
# print b

def sting_reverse(str1):
    str2=''
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    print(str2)
str1='abcdefg'
sting_reverse(str1)
