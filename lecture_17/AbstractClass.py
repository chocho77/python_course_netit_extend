from abc import ABC, abstractmethod


# Define an abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
    
    def sound(self):
        return "Bark"  # Providing the implementation of the abstract method

class Cat(Animal):

    def sound(self):
        return "Meow" # Providing the implemention of the abstract method

def main():
    # Create an instance of Dog
    dog = Dog()
    print(dog.sound())  # Output: Bark
    cat = Cat()
    print(cat.sound()) # Output: Meow

if __name__ == '__main__':
    main()

