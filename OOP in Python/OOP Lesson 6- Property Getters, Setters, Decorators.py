# Lesson on property decorators, getter, setter and deleter
# @property- Let's a method be treated as an attribute. Useful in cases like defining an email which is a combination
# of first and last names


class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @property
    def email(self):
        email = self.fname.lower() + '.' + self.lname.lower() + '@company.com'
        return email

    @property
    def fullname(self):
        fullname = self.fname + " " + self.lname
        return fullname

    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.lname = None


emp_1 = Employee('Ajit', 'Choudhary', 90000)
emp_2 = Employee('Moutusi', 'Ghatak', 100000)
print(emp_1.email)

emp_2.fullname = 'Big boobies'
print(emp_2.fname)
print(emp_2.email)
print(emp_2.fullname)

# Using a deleter
del emp_1.fullname
print(emp_1.fname) # This gives None
