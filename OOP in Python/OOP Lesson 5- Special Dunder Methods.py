# Lesson on Magic/Dunder methods

class Employee:
    # Class variable
    raise_amount = 1.04
    num_of_emps = 0  # Counter to track number of Employees

    # Classes need an init method
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = self.fname.lower() + '.' + self.lname.lower() + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return self.fname + " " + self.lname

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    # It is generally considered necessary to have at least a repr method to provide information on the class
    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # Custom add dunder to illustrate operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    def len(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 90000)
emp_2 = Employee('Jane', 'Foster', 110000)

# By default this uses str if str is not available it uses repr
print(emp_1)
print(emp_1 + emp_2)