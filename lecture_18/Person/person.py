class Person:
    def __init__(self,
                 first_name,
                 middle_name,
                 last_name,
                 email_id):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._email_id = email_id
    
    @property
    def first_name(self):
        return self._first_name
    
    