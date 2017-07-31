# l=[1,1,2,2,3,4]
# for i in l:
#     no=0
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>1:
#         del l[]
#
#     no+=1
a=[1,2,4,2,4,5,6,5,7,8,9,0]
b={}
b=b.fromkeys(a)
print b

a=list(b.keys())
print a

a=[1,2,4,2,4,5,6,5,7,8,9,0]
a=list(set(a))
print a


