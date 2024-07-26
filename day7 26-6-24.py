#Code for video - 21

def avg(a=2,b=6):
    print((a+b)/2)
# avg(3,3)
# avg(5)
avg(b=5,a=8)

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)

#Code for video - 22

a=[1,2,3,4]
b=[45,78,'abc']

if 1 in a:
    print(True)
else:
    print(False)
    
print(b[1:3])

lst = [i*i for i in range(20) if i%2==0]
print(lst)