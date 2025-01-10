from typing import Tuple


def sol_one() -> Tuple:
    input_one = input()
    input_two = input()
    input_three = input()

    return input_one, input_two, input_three


def sol_two(par_one:str, par_two:str, par_three:str):
    print(par_one)
    print(par_two)
    print(par_three)
    print(type(par_one), type(par_two), type(par_three), sep="\n")


if __name__ == '__main__':
    my_tuple:Tuple = sol_one()
    print(my_tuple)
    print(type(my_tuple))
    sol_two(*my_tuple)
