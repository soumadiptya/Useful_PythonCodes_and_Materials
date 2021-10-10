import requests


class Employee:
    raise_amt = 1.05

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @property
    def email(self):
        email = self.fname.lower() + "." + self.lname.lower() + "@company.com"
        return email

    @property
    def fullname(self):
        return self.fname + " " + self.lname

    def apply_raise(self):
        self.salary = self.salary * Employee.raise_amt

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.lname}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response'
