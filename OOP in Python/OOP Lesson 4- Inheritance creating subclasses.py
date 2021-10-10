# Lesson on Class Inheritance. Creating Developer and Manager subclasses

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


class Developer(Employee):
    raise_amount = 1.10

    # Subclasses need their own inits in general
    def __init__(self, fname, lname, salary, prog_lang):
        super().__init__(fname, lname, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.02

    def __init__(self, fname, lname, salary, years_of_exp, employees_managed=None):
        super(Manager, self).__init__(fname, lname, salary)
        self.years_of_exp = years_of_exp
        if employees_managed is None:
            self.employees_managed = []
        else:
            self.employees_managed = employees_managed

    def add_employee(self, employee):
        if employee not in self.employees_managed:
            self.employees_managed.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees_managed:
            self.employees_managed.remove(employee)

    def print_emps(self):
        for employee in self.employees_managed:
            print('-->', employee.fullname())


dev_1 = Developer('Soumadiptya', 'Chakraborty', 92000, 'Python')
dev_2 = Developer('Surbhi', 'Welekar', 65000, 'Ruby')
# print(dev_1.email, dev_1.raise_amount)
# help(dev_1)  # Help gives the method resolution order as well as all objects and methods that were inherited
# print(dev_1.email, dev_1.raise_amount, dev_1.prog_lang)

manager_1 = Manager('Sue', 'Smith', 90000, 15, [dev_1])
print(manager_1.email, dev_1.fullname())
manager_1.print_emps()
manager_1.add_employee(dev_2)
manager_1.print_emps()
manager_1.remove_employee(dev_1)
manager_1.print_emps()

# isinstance() and isssubclass() are builtin functions to do what they say they do
