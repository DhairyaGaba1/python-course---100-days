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