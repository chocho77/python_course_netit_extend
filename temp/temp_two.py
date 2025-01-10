def sol():
    width = 80
    name = "Chavdar"
    print("*" * width)
    width_calc_one = width - (10 * len(name) + 1)
    space_between_one = " " * width_calc_one
    width_calc = width - 2 * (len(name) + len(name) + 3)
    space_between = " " * width_calc 
    print(f"{name} {space_between_one} {name} {space_between} {name}")
    

def sol_one():
    width = 80
    name = "KokoSveti"
    space_between_one = (len(name) - 4) * " "
    width_calc = width - 4 * len(name) 
    space_between = " " * width_calc 
    print(f"{name} {space_between_one} {name} {space_between} {name}")


def sol_two():
    width = 80
    name = "Koko"
    space_between_one = (len(name) + 6) * " "
    width_calc = width - 6 * len(name) 
    space_between = " " * width_calc 
    print(f"{name} {space_between_one} {name} {space_between} {name}")
    pass


if __name__ == '__main__':
    sol()
    sol_one()
    sol_two()


    
