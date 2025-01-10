class Cat:
    NUMBER_OF_PAWS = 4
    number_of_cats = 0
    sound = "Meow"
    
    def __init__(self, _name, _age, _color="red"):
        self.name = _name
        self.age = _age
        self.color = _color
        Cat.number_of_cats += 1
    
    def print_info(self):
        print(f"Cat's name:{self.name}")
        print(f"Cat's age: {self.age}")
        print(f"Cat's color: {self.color}")


def main():
    cat_tom = Cat("Tom", 2, "green")
    cat_tom.print_info()
    cat_sam = Cat("Sam", 2, "green")
    cat_sam.print_info()
    cat_rod = Cat("Rod", 3)
    cat_rod.print_info()
    print(f"Number of paws: {Cat.NUMBER_OF_PAWS}")
    print(f"Number of cat's {Cat.number_of_cats}")
    print(Cat.sound)
    Cat.sound = "Meow meow"
    print(Cat.sound)


if __name__ == '__main__':
    main()