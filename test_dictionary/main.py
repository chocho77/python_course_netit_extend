from input_data import user_input_order, user_input_data
from database import insert_data_in_db, read_db

key = ""
d = {}
my_l_one = []
my_l_two = []

def main():
    for _ in range(4):
          u_i = user_input_data()
          u_y = user_input_data()
          my_l_one.append(u_i)
          my_l_two.append(u_y)
    key = user_input_order()
    insert_data_in_db(key,my_l_one)
    key = user_input_order()
    insert_data_in_db(key, my_l_two)
    d = read_db()
    print(d)
    my_l_one.clear()
    my_l_two.clear()


if __name__ == '__main__':
        for _ in range(2):
            main()