from app_functions import print_dict_list, add_to_dict_list, update_dict_list, get_val_int_input, delete_dict_from_dict_list
from abc import abstractproperty
from unittest.mock import Mock, patch, mock_open

# @patch("builtins.open" , callable = mock_open)
# @patch("csv.DictReader")
# def test_load_csv_to_dict_list(mock_dict_reader, mock_file_opener):
#     mock_dict_reader.return_value = {"name": "Coke Zero",
#     "price": 0.8},
#     {"name": "Lemon Fanta",
#     "price": 1.2}]
    
#     assert

def test_save_dict_list_to_csv():
    None

def test_get_val_int_input():
    list_sizes = [2, 4]
    mock_input = Mock()
    mock_input.side_effect = ["1", "-1", "1", "10", "1", "1", "1"]
    mock_print = Mock()
    
    for size in list_sizes:
        result = get_val_int_input(size, mock_input, mock_print)
        assert (result in range(size)) or result == None

def test_print_dict_list():
    test_print = Mock()
    test_dict_list = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    
    print_dict_list(test_dict_list, test_print)
    
    test_print.assert_any_call("Entry 1")
    test_print.assert_any_call("name = Coke Zero")
    assert test_print.call_count == 6

def test_add_to_dict_list():
    test_dict_list = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    mock_input = Mock()
    mock_input.side_effect = ["test_add", "42"]
    
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
    index = 0
    mock_input = Mock()
    mock_input.side_effect = ["test_update", "42", "", ""]
    update_dict_list(test_dict_list, index, mock_input)
    update_dict_list(test_dict_list, index, mock_input)
    
    assert test_dict_list[0] == {"name": "test_update",
    "price": 42}

def test_delete_dict_from_dict_list():
    test_dict_list = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    test_dict_list2 = [
    {"name": "Coke Zero",
    "price": 0.8},
    {"name": "Lemon Fanta",
    "price": 1.2}]
    index = 1
    
    
    delete_dict_from_dict_list(test_dict_list, index)
    
    assert len(test_dict_list) == len(test_dict_list2) - 1

def test_update_order_status():
    test_ord_dict_list = [{
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "courier": 2, 
    "status": "preparing",
    "items": [1, 3, 4]},
    {"customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "courier": 2, 
    "status": "preparing",
    "items": [1, 3, 4]}]
    index = 1
    mock_input = Mock()
    mock_input.return_value = "being delivered"
    
    update_dict_list(test_ord_dict_list, index, mock_input)
    
    assert test_ord_dict_list[1]["status"] == "being delivered"
