from source.app_functions import \
load_csv_to_dict_list, save_dict_list_to_csv, print_dict_list \

from abc import abstractproperty
from unittest.mock import Mock

def test_load_csv_to_dict_list():
    test_reader = Mock()
    test_reader.DictReader.return_value

def test_save_dict_list_to_csv():
    None

def test_print_dict_list():
    test_print = Mock()
    test_dict_list = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    
    print_dict_list(test_dict_list, test_print)
    test_print.assert_called_with("name = Coke Zero")
    assert test_print.call_count == 6