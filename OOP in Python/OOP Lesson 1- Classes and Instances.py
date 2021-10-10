# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:10:01 2021

@author: souma
"""


# Creating a basic class
class Employee:
    # Classes need an init method
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = self.fname.lower() + '.' + self.lname.lower() + "@company.com"

    def fullname(self):
        return self.fname + " " + self.lname
    # Instantiate the class


emp_1 = Employee('Soumadiptya', 'Chakraborty', 92000)
emp_2 = Employee('Surbhi', 'Welekar', 65000)
print(emp_1.email)
print(emp_1.fullname())
# Running class method with Instance
print(Employee.fullname(emp_2))
