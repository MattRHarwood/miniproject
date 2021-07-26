#assorted functions for app
from typing import Callable

def load_csv_into_dict_list(filename_csv : str, csv_reader : object) -> list:
    dict_list = []
    with open(filename_csv, "r") as file:
        reader = csv_reader.DictReader(file)
        for row in reader:
            dict_list.append(dict(row))
    return dict_list

def save_dict_list_to_csv(dict_list : list, csv_writer : object, filename_csv : str):
    with open(filename_csv, "w") as file:
        keys = dict_list[0].keys()
        writer = csv_writer.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(dict_list)

def print_dict_list(dict_list : list, print_function : Callable):
    for i in range(len(dict_list)):
        a = i + 1
        print_function(f"Entry {a}")
        for key, value in dict_list[i]:
            print_function(f"{key} = {value}")

def add_to_dict_list(dict_list : list, input_function : Callable):
    new_dict = {}
    for key in dict_list[0].keys():
        new_val = input_function({f"enter new value for {key}: "})
        new_dict[key] = new_val
    dict_list.append(new_dict)

def update_dict_list(dict_list : list, index : int, input_function : Callable):
    for key in dict_list[index].keys():
        new_val = input_function(f"enter new value for {key}, or enter to skip: ")
        if new_val == "":
            continue
        else:
            dict_list[index][key] = new_val
