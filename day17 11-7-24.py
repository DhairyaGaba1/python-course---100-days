#Code for video 65
# class Math:
#     def __init__(self, num):
#         self.num=num
    
#     def addtonum(self,n):
#         self.num=self.num + n
#     @staticmethod
#     def add(a, b):
#         return a + b

# # result = Math.add(1, 2)
# # print(result) 
# a=Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# print(a.add(7,2))

#Code for video 66

# class Employee:
#     company_name="Microsoft"
#     noOfEmployee=0  
#     def __init__(self, name):
#         self.name=name
#         self.raise_amount=0.02
#         Employee.noOfEmployee+=1
#     def showDetails(self):
#         print(f"The name of employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.company_name} is {self.raise_amount}")

# emp1=Employee("Parth")
# emp1.raise_amount=0.3
# emp1.company_name = "Microsoft India"
# emp1.showDetails()
# Employee.company_name="Google"
# emp2=Employee("Rohan")
# emp2.company_name="TCS"
# emp2.showDetails()

#Code for video 69

# class Employee:
#     company="Microsoft"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
#     @classmethod
#     def change_company(cls, newCompany):
#         cls.company=newCompany

# e1=Employee()
# e1.name="Parth"
# e1.change_company("Tesla")
# e1.show()
# print(Employee.company)

#Code for video 70

# class Employee:
#     def __init__(self, name, salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def fromStr(cls, string):
#         return cls(string.split("-")[0], int(string.split("-")[1]))
        
# e=Employee("Parth", 120000)
# print(e.name)
# print(e.salary)

# string="Parth-120000"
# e2=Employee.fromStr(string)
# print(e2.name)
# print(e2.salary)
