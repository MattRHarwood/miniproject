from app_functions import print_dict_list, add_to_dict_list
from abc import abstractproperty
from unittest.mock import Mock, patch

# def test_load_csv_to_dict_list():
#     test_reader = Mock()
#     test_reader.DictReader.return_value

# def test_save_dict_list_to_csv():
#     None

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

def test_add_to_dict_list():
    test_dict_list = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    mock_input = Mock()
    mock_input.side_effect = ["test_zero", 42]
    
    add_to_dict_list(test_dict_list, mock_input)
    
    assert test_dict_list[2] == {"name": "test_zero",
    "price": 42}