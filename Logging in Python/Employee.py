import logging

# Create a custom logger and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Add a formatter
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
# Add a file handler
file_handler = logging.FileHandler('employee.log')
# Add the formatter to the handler
file_handler.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(file_handler)
# Basic Config
# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return "{}.{}@email.com".format(self.fullname, self.lname)

    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)


emp_1 = Employee("John", "Doe")
emp_2 = Employee("Corey", "Schafer")
