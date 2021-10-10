# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:06:29 2021

@author: souma
"""


# Class variables are variables shared among all instances of a class
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
        self.salary = self.salary * 1.04

    def apply_raise2(self):
        self.salary = self.salary * self.raise_amount  # self.class_var is required you cant directly use it


emp_1 = Employee('Soumadiptya', 'Chakraborty', 92000)
emp_2 = Employee('Surbhi', 'Welekar', 65000)

print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)

print(emp_2.salary)
emp_2.apply_raise2()
print(emp_2.salary)

print(Employee.num_of_emps)
