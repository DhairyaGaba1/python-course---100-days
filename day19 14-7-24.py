#Code for video 78

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# d=Dog("Dog", "Doggerman")
# d.make_sound()

# a=Animal("Dog", "Dog")
# a.make_sound()

# #Quick quiz

# class Cat(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Cat")
#         self.breed=breed
        
#     def make_sound(self):
#         print("meow")
        
#Code for video 79

# class Employee:
#     def __init__(self, name):
#         self.name=name
#     def show(self):
#         print(f"The name is {self.name}")

# class Dancer:
#     def __init__(self, dance):
#         self.dance=dance
#     def show(self):
#         print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#     def __init__(self, dance, name):
#         self.dance=dance
#         self.name=name

# o=DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show()
# print(DancerEmployee.mro())

#Code for video 80

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")
        
# o=GoldenRetriever("tommy", "black")
# o.show_details()

#Code for video 81

# class BaseClass:
#     pass

# class Derived1(BaseClass):
#     pass

# class Derived2(BaseClass):
#     pass

# class Derived3(Derived1, Derived2):
#     pass

# class Baseclass:
#     pass

# class D1(Baseclass):
#     pass
# class D2(Baseclass):
#     pass

# class D3(D1):
#     pass

#Code for video 84

# import time

# def usingWhile():
#     i=0
#     while i<50:
#         i+=1
#         print(i)

# def usingFor():
#     for i in range(50):
#         print(i)

# init=time.time()
# usingFor()
# t1 = (time.time() - init)
# usingWhile()
# print(t1)
# print(time.time() - init)

# print(4)
# time.sleep(3)
# print("Hello")

# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

# print(formatted_time)

#Code for video 85

# import argparse
# import requests

# def download_file(url, local_filename): 
#   if local_filename is None:
#     local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#   with requests.get(url, stream=True) as r:
#       r.raise_for_status()
#       with open(local_filename, 'wb') as f:
#           for chunk in r.iter_content(chunk_size=8192): 
#               # If you have chunk encoded response uncomment if
#               # and set chunk_size parameter to None.
#               #if chunk: 
#               f.write(chunk)
#   return local_filename
  
# parser = argparse.ArgumentParser()

# # Add command line arguments
# parser.add_argument("url", help="Url of the file to download")
# # parser.add_argument("output", help="by which name do you want to save your file")
# parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# # Parse the arguments
# args = parser.parse_args()

# # Use the arguments in your code
# print(args.url)
# print(args.output, type(args.output))
# download_file(args.url, args.output)

#Alternate video code

# import argparse
# import sys

# def calc(args):
#     if args.o == 'add':
#         return args.x + args.y

#     elif args.o == 'mul':
#         return args.x * args.y

#     elif args.o == 'sub':
#         return args.x - args.y

#     elif args.o == 'div':
#         return args.x / args.y

#     else:
#         return "Something went wrong"

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0,
#                         help="Enter first number. This is a utility for calculation. Please contact harry bhai")

#     parser.add_argument('--y', type=float, default=3.0,
#                         help="Enter second number. This is a utility for calculation. Please contact harry bhai")

#     parser.add_argument('--o', type=str, default="add",
#                         help="This is a utility for calculation. Please contact harry bhai for more")

#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))
