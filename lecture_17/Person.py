class Person:
    def __str__(self) -> str:
        return f"Hi, I am {self._name} !"

    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError
        
        self._name = value

 
def main():
    person = Person("John")
    print(person)
    person.name = "Dimo"
    print(person)
    person.name = "Kiro"
    print(person)
    

if __name__ == '__main__':
    main()


