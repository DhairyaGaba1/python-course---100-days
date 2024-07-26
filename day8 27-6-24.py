#Code for video 23
# l = [1,2,3,4,7,8,5,4,3]
# l.sort()
# print(l)
# l.append(10)
# print(l)
# l.reverse()
# print(l)
# print(l.index(5))
# print(l.count(3))
# l.insert(10,100)
# print(l)
# a=[100,400,80]
# l.extend(a)
# print(l)

#Code for video 24,25
t = (1,5,6)
print(t)
print(type(t))
t[1:]
a=list(t)
a.extend([45,67,89,34,78])
a.pop(5)
t = tuple(a)
print(t)
print(t.count(5))
print(t.index(45))
print(len(t))