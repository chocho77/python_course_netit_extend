class Student:
    def __init__(self,
                 first_name="",
                 middle_name="",
                 last_name="",
                 degree="",
                 year = 0,
                 university=None,
                 email="",
                 tel=None):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._degree = degree
        self._year = year
        self._university = university
        self._email = email
        self._tel = tel


    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_name(self):
        return self._middle_name

    @property
    def last_name(self):
        return self._last_name
    
    @property
    def degree(self):
        return self._degree
    
    @property
    def year(self):
        return self._year
    
    @property
    def university(self):
        return self._university
    
    @property
    def email(self):
        return self._email
    
    @property
    def tel(self):
        return self._tel
    

