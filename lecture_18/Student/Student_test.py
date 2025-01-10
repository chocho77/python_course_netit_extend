import unittest
from Student.Student import Student


class StudentTest(unittest.TestCase):
    def test_init_default_values(self):  # add assertion here
        student = Student()
        self.assertEqual(student.first_name, "")
        self.assertEqual(student.middle_name, "")
        self.assertEqual(student.last_name, "")
        self.assertEqual(student.degree, "")
        pass



if __name__ == '__main__':
    unittest.main()


# s Student:
#    def __init__(self,
#                 first_name="",
#                 middle_name="",
#                 last_name="",
#                 degree="",
#                 year = 0,
#                 university=None,
#                 email="",
#                 tel=None):