class Employee:
    def __init__(self):
        self.name = 'none'
        self.id_number = 0
        self.department = 'none'
        self.job_title = 'none'

susan_m = Employee()
mark_j = Employee()
joy_r = Employee()

susan_m.name = input("Enter a name:\n")
susan_m.id_number = int(input("Enter ID Number: \n"))
susan_m.department = input("Enter Department: \n")
susan_m.job_title = input("Enter job title: \n")

mark_j.name = input("Enter a name:\n")
mark_j.id_number = int(input("Enter ID Number: \n"))
mark_j.department = input("Enter Department: \n")
mark_j.job_title = input("Enter job title: \n")

joy_r.name = input("Enter a name:\n")
joy_r.id_number = int(input("Enter ID Number: \n"))
joy_r.department = input("Enter Department: \n")
joy_r.job_title = input("Enter job title: \n")

print('{:<16} {:<15} {:<18} {:<15}'.format('Name', 'ID Number', 'Department', 'Job Title'))
print('{:<16} {:<15} {:<18} {:<15}'.format(susan_m.name, susan_m.id_number,susan_m.department, susan_m.job_title))
print('{:<16} {:<15} {:<18} {:<15}'.format(mark_j.name, mark_j.id_number,mark_j.department , mark_j.job_title))
print('{:<16} {:<15} {:<18} {:<15}'.format(joy_r.name, joy_r.id_number, joy_r.department, joy_r.job_title))

