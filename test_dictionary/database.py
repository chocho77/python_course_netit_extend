from typing import Dict,List

d = {}

def insert_data_in_db(key:str, my_list: List) -> None:
    d.update({key:my_list})


def read_db() -> Dict:
    return d




