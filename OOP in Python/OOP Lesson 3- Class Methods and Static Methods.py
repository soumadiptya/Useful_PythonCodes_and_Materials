# Lesson on Regular Methods, Class Methods and Static Methods
# Regular methods take an instance as the argument, class methods take the class itself whereas static methods are
# like regular functions

# Imports
import datetime


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
        self.salary = self.salary * self.raise_amount  # self.class_var is required you cant directly use it

    @classmethod
    def set_raise_amt(cls, raise_amt):
        cls.raise_amount = raise_amt

    @classmethod
    def create_employee(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        salary = int(salary)
        return cls(fname, lname, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Soumadiptya', 'Chakraborty', 92000)
emp_2 = Employee('Surbhi', 'Welekar', 65000)

# Use class method
print(emp_1.raise_amount)
Employee.set_raise_amt(1.05)
print(emp_1.raise_amount)

# Class methods as constructors
emp_3 = Employee.create_employee('Promita-Panja-69000')
print(emp_3.email)
emp_3.apply_raise()
print(emp_3.salary)

# Use a static method
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
