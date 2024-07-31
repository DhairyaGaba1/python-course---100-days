#Code for video 59


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good morning")
#         fx(*args, **kwargs)
#         print("Thnaks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello world")
    
# def add(a,b):
#     print(a+b)

# hello()
# greet(add)(1,2)

#Code for video 60

# class MyClass:
#     def __init__(self, value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10*self._value
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value=new_value/10
    
# obj=MyClass(10)
# obj.ten_value=67
# print(obj.ten_value)
# obj.show()

#Code for video 61

class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
        
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")
        
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")
e1=Employee("Parth", 18)
e1.showDetails()
e2=Programmer("Alpha", 4210)
e2.showDetails()
e2.showLanguage()

#Code for video 62

# class Employee:
#     def __init__(self):
#         self.__name="Harry"

# a=Employee()
# print(a._Employee__name)
# print(a.__name) #Cant be accessed directly

# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))
# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())