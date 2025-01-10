# https://www.tutorialspoint.com/software_testing/index.htm
class Student:
    def __init__(self,
                 first_name,
                 middle_name,
                 last_name,
                 year,
                 degree,
                 university,
                 email,
                 tel
                 ):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._year = year
        self._degree = degree
        self._university = university
        self._email = email
        self._tel = tel
    
    def __str__(self):
        return f"""first name : {self._first_name}, middle name : {self._middle_name} last name : {self._last_name} year : {self._year}
                   degree :  {self._degree}  university : {self._university} Email: {self._email} tel: {self._tel}"""


def main():
    print("Main function called.")
    student = Student("Kiro", "Ivanov", "Papazov", 1997, "electrition", "TU-Varna", "kiro@gmail.com", 884344567)
    print(student)


if __name__ == '__main__':
    main()

