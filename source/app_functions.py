#assorted functions for app
from typing import Callable

def connect_to_mysql_db(db_library : object):
    connection = db_library.connect(host='localhost',
    user='root',
    password='password',
    database='miniproject',
    charset='utf8mb4',
    cursorclass=db_library.cursors.DictCursor)
    return connection

def get_val_int_input(start : int, end : int, input_function : Callable, print_function : Callable) -> int:
    end_inc = end - 1
    input = int(input_function(f"enter a number from {start} to {end_inc}:\n"))
    if input not in range(start, end):
        print_function("please enter a valid input")
        get_val_int_input(start, end, input_function, print_function)
    else:
        return input

def print_dict_list(dict_list : list, print_function : Callable):
    for i in range(len(dict_list)):
        a = i + 1
        print_function(f"\nEntry {a}")
        for key, value in dict_list[i].items():
            print_function(f"{key} = {value}")

def add_to_dict_list(dict_list : list, input_function : Callable):
    new_dict = {}
    for key in dict_list[0].keys():
        new_val = input_function(f"enter a value for {key}:\n")
        try: 
            new_val = int(new_val)
            new_dict[key] = new_val
        except:
            new_dict[key] = new_val
    dict_list.append(new_dict)

def update_dict_list(dict_list : list, index : int, input_function : Callable):
    for key in dict_list[index].keys():
        new_val = input_function(f"enter new value for {key}, or enter to skip:\n")
        if new_val == "":
            continue
        try: 
            new_val = int(new_val)
            dict_list[index][key] = new_val
        except:
            dict_list[index][key] = new_val

def delete_dict_from_dict_list(dict_list : list, index : int):
    del dict_list[index]

def update_order_status(ord_dict_list : list, index : int, input_function : Callable):
    new_status = input_function("what would like to update the order status to?\n")
    ord_dict_list[index]["status"] = new_status