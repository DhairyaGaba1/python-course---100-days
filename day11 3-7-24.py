#Code for video 36  
'''
a=input("Enter a number: ")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except Exception as e:
    print("Invalid input")
print("end of program")
'''

#Code for video 37
'''
try:
    l=[1,5,6,7]
    i=int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured.")
finally:
    print("I am always executed.")
'''

#Code for video 38
'''
a=int(input("Enter any value between 5 and 9"))
if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
#Defining custom exception
class CustomError(Exception):
  # code ...
  pass
try:
  # code ...
except CustomError:
  # code...
'''