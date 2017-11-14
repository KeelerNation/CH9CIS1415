class Employee:
    def __init__(self, Name, ID, Depart, JT):
        self.Name = Name
        self.ID = ID
        self.Depart = Depart
        self.JT = JT



    #set funcations

    def setName(self, Name):
        self.Name = Name

    def setID(self, ID):
        self.ID = ID

    def setDepart(self, Depart):
        self.Depart = Depart

    def setJT(self, JT):
        self.JT = JT


    #get funcations
    def getName(self):
        return self.Name

    def getID(self):
        return self.ID


    def getDepart(self):
        return self.Depart


    def getJT(self):
        return self.JT


    def __str__(self):
        return 'Name: ' + self.Name + \
                '\nID number: ' + self.ID + \
                '\nDepartment: ' + self.Depart + \
                '\nTitle: ' + self.JT









emp1 = Employee('name', 'id', 'department', 'title')
emp2 = Employee('name', 'id', 'department', 'title')
emp3 = Employee('name', 'id', 'department', 'title')

emp1.setName('Susan Meyers')
emp1.setID('47899')
emp1.setDepart('Accounting')
emp1.setJT('Vice President')

emp2.setName('Mark Jones')
emp2.setID('39119')
emp2.setDepart('IT')
emp2.setJT('Programmer')

emp3.setName('Joy Rogersr')
emp3.setID('81774')
emp3.setDepart('Manufacturing')
emp3.setJT('Engineer')


print(emp1)
print('')
print(emp2)
print('')
print(emp3)