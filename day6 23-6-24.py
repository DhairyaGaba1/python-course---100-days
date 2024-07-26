#Code for video - 14

# x=int((input("Enter your age: ")))
# if x>18:
#     print("You can drive.")
# elif x==18:
#     ask=input("Have you learnt driving(Y/N):")
#     if ask=="y" or ask=="Y":
#         print("You can drive")
#     else:
#         print("You cant drive.")
# else:
#     print("You cant drive.")

#Code for video - 16
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
        
#Code for video - 17
name = "parth"
for i in name:
    print(i,end=",")
for i in range(0,11):
    print(i)
for i in range(5,101,5):
    print(i)
    
#Code for video - 18:
i=0
while i<=10:
    print(i)
    i+=1
else:
    print("Loop is over.")
    
#Code for video - 19:
for i in range(1,51):
    if i==21:
        continue
    print(i)
    if i==50:
        break

#Do-while loop in python:
while True:
    print(i)
    i+=1
    if i%100==0:
        break

#Code for video - 20:
def gmean(a,b):
    g=(a*b)**(1/2)
    return g
x=int(input(("Enter a number: ")))
y=int(input(("Enter a number: ")))
print(gmean(x,y))