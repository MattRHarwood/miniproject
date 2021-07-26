from app_functions import print_dict_list, add_to_dict_list, update_dict_list
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
    mock_input.side_effect = ["test_add", 42]
    
    add_to_dict_list(test_dict_list, mock_input)
    
    assert test_dict_list[2] == {"name": "test_add",
    "price": 42}
    mock_input.assert_called == 2

def test_update_dict_list():
    test_dict_list = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    index = 1
    mock_input = Mock()
    mock_input.side_effect = ["test_update", 42, "", ""]
    
    update_dict_list(test_dict_list, 0, mock_input)
    update_dict_list(test_dict_list, 0, mock_input)
    
    assert test_dict_list[0] == {"name": "test_update",
    "price": 42}