#Code for video 30

#Code for finding factorial
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
'''

#Code for fibonacci series
'''
def fib(n,a=0,b=1):
     if n>0:
        print(a)
        fib(n-1,b,a+b)
fib(7) 
'''

#Code for video 31, 32
'''
s={2,2,2,4,5,6,7,7}
print(s)
a=set()
print(type(a))
for i in s:
    print(i)
    
s1={1,2,3,6,7,8}
s2={5,8,9,1,2}
# s=s1.union(s2)
# print(s)
# s1.update(s2)
# print(s1)
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)
# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# s1.add(10)
# print(s1)
# s1.update(s2)
# print(s1)
# s1.remove(3)
# s1.discard(20)
# print(s1)
# a=s1.pop()
# print(a)
# del s1
# print(s1)
# s1.clear()
# print(s1)
# if 3 in s1:
#print("yes")
'''

#Code for video 33, 34

a={1:"parth", 2:"abc", 3:"xyz"}
# print(a[2])
# print(a.get(5))
# print(a.keys())
# print(a.values())
# for i in a.keys():
#     print(f"{i}:{a[i]}")
# for key,value in a.items():
#     print(f"{key}:{value}")

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# print(ep1)
# ep1.clear()
# print(ep1)
# ep1.pop(123)
# print(ep1)
# ep1.popitem()
# print(ep1)
# del ep1
# del ep1[122]
# print(ep1)

#Code for video 35
for i in range(4):
    print(i)
else:
    print("Done")