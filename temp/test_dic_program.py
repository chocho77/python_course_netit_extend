from typing import Dict

d = {}

def insert_data_into_dic(key:str, data_one:str, data_two:str) -> None:
    list_data = []
    insert_tuple = (data_one, data_two)
    list_data.append(insert_tuple)
    d[key] = list_data

def extract_all_dictionary() -> Dict:
    return d

def print_all_dictionary() ->  None:
    dic = {}
    dic = extract_all_dictionary()
    print(dic)


def sol() -> None:
    insert_data_into_dic("key_one", "data_one", "data_two")
    insert_data_into_dic("key_two", "data_one", "data_two")
    insert_data_into_dic("key_three", "data_one", "data_two")
    print_all_dictionary()


def main() -> None:
    sol()


if __name__ == '__main__':
    main()



