import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    @classmethod
    def tearDownClass(cls):
        print("Tear down class")

    def setUp(self):
        # Annotations- https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
        self.employee1 = Employee('Surbhi', 'Sharma', 90000)
        self.employee2 = Employee('Vandan', 'Pokhariya', 120000)

    def tearDown(self) -> None:
        pass

    def test_Employee(self):
        self.assertEqual(self.employee1.email, 'surbhi.sharma@company.com')
        self.assertEqual(self.employee2.email, 'vandan.pokhariya@company.com')

        self.employee1.fname = 'Crush'
        self.employee2.lname = 'punewala'

        self.assertEqual(self.employee1.email, 'crush.sharma@company.com')
        self.assertEqual(self.employee2.email, 'vandan.punewala@company.com')

    def test_fullname(self):
        self.assertEqual(self.employee1.fullname, 'Surbhi Sharma')
        self.assertEqual(self.employee2.fullname, 'Vandan Pokhariya')

        self.employee1.fname = 'Crush'
        self.employee2.lname = 'punewala'

        self.assertEqual(self.employee1.fullname, 'Crush Sharma')
        self.assertEqual(self.employee2.fullname, 'Vandan punewala')

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.employee2.apply_raise()

        self.assertEqual(self.employee1.salary, 90000 * 1.05)
        self.assertEqual(self.employee2.salary, 120000 * 1.05)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.employee1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.employee2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()
