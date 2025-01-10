def sol(text:str) -> int:
    return len(text)

def find_greater(num1:int, num2:int) -> int:
    return max(num1, num2)



if __name__ == '__main__':
    text = "chavdar"
    text_one = "something"
    num_symbols = sol(text)
    num_symbols_one = sol(text_one)
    greater = find_greater(num_symbols, num_symbols_one)
    print(f"Greater betwwen {num_symbols} and {num_symbols_one} is {greater}.")
    
    
