# #Code for video 53

# #MAP

# def cube(x):
#     return x**3
# l=[1,2,4,5,6,7]
# newl=list(map(cube,l))
# # print(newl)

# #FILTER

# def filter_function(a):
#     return a>4
# newl2 = list(filter(filter_function, l))
# # print(newl2)

#REDUCE

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# sum = reduce(lambda x, y: x + y, numbers)
# print(sum)

#Code for video 54
# a=4
# b="4"
# print(a is b)
# print(a==b)

#Code for video 57

# class Person:
#     name = "Parth"
#     occupation = "Student"
#     networth = "0"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = Person()
# a.name="shubham"
# a.occupation="teacher"
# # print(a.name, a.occupation)
# a.info()

#Code for video 58

# class person:
#     def __init__(self, n, o):
#         print("Hey! I am a person")
#         self.name = n
#         self.occ = o
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = person("Parth", "student")
# b = person("Divya", "teacher")
# c = person(1,2,3)
# a.info()
# b.info()