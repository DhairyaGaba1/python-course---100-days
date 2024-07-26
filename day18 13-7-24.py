#Code for video 71
# x=(1, 2, 3)
# print(dir(x))
# print(x.__add__)

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         self.version=1
        
# p=Person("John", 30)
# print(p.__dict__)

# print(help(Person))

#Code for video 72

# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Parth")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

# class Employee:
#     def __init__(self, name, id):
#         self.name=name
#         self.id=id

# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#         super().__init__(name,id)
#         self.lang=lang
        
# rohan=Employee("Rohan das", "420")
# parth=Programmer("Parth","4210","Python")
# print(parth.name)
# print(parth.id)
# print(parth.lang)

#Code for video 73

# from emp import Employee

# e=Employee("Parth")
# print(str(e))
# print(repr(e))
# e()
# print(e.name)
# print(len(e))

#Code for video 74

# class Shape:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius,radius)
#     def area(self):
#         return 3.14 * super().area()

# # rec = Shape(3,5)
# # print(rec.area())

# c=Circle(5)
# print(c.area())

#Code for video 77

# class vector:
#     def __init__(self, i, j, k):
#         self.i=i
#         self.j=j
#         self.k=k
    
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
        
#     def __add__(self, x):
#         return vector(self.i + x.i, self.j + x.j, self.k + x.k)
# v1=vector(3, 5, 6)
# print(v1)

# v2=vector(1, 2, 9)
# print(v2)

# print(v1 + v2)
# print(type(v1+v2))
