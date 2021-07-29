#Week 4 miniproject
import builtins
from app_functions import *

#stubs for testing main
test_products_list = [  
{"name": "Coke Zero",
"price": 0.8},
{"name": "Coke Zero",
"price": 0.8}]
test_courier_list = [
{"name": "Bob",
"phone": "0789887889"},
{"name": "Bob",
"phone": "0789887889"}]
test_orders_list = [
{"customer_name": "John",
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

print("Welcome to App!\n\n")

def main_menu():
    # raw_products = load_csv_to_dict_list
    # raw_couriers = load_csv_to_dict_list
    # raw_orders = load_csv_to_dict_list
    # prod_list = raw_products
    # cour_list = raw_couriers
    # ord_list = raw_orders
    
    print("Main Menu:\n\n"
        + "0 - Save and Exit\n\n" 
        + "1 - Products Menu\n\n"
        + "2 - Couriers Menu\n\n"
        + "3 - Orders Menu\n\n")
    
    menu_option = get_val_int_input(4, builtins.input, builtins.print)
    
    if menu_option == 0:
        # save_products(prod_list)
        # save_couriers(cour_list)
        # save_orders(ord_list)
        
        exit()
    elif menu_option == 1:
        sub_menu("products", test_products_list)
    elif menu_option == 2:
        sub_menu("couriers", test_courier_list)
    elif menu_option == 3:
        sub_menu("orders", test_orders_list)
    else:
        main_menu()

def sub_menu(type : str, dict_list : list):
    print(f"\n{type.title()} Menu:\n\n"
        + "0 - Return to Main Menu\n\n"
        + f"1 - Print {type.title()} List\n\n"
        + f"2 - Add to {type.title()} List\n\n"
        + f"3 - Update {type.title()} List\n\n"
        + f"4 - Delete from {type.title()} List\n")
    if type == "orders":
        print("5 - Update Order Status\n\n")
        sub_option = get_val_int_input(6, builtins.input, builtins.print)
    else:
        sub_option = get_val_int_input(5, builtins.input, builtins.print)
        
    if sub_option == 0:
        main_menu()
    elif sub_option == 1:
        pass
    elif sub_option == 2:
        add_to_dict_list(dict_list, builtins.input)
    elif sub_option == 3:
        print_dict_list(dict_list, builtins.print)
        print("Which entry do you want to update?")
        index = get_val_int_input(((len(dict_list))), builtins.input, builtins.print, 1)
        update_dict_list(dict_list, index, builtins.input)
    elif sub_option == 4:
        print("Which entry do you want to delete?")
        index2 = get_val_int_input(((len(dict_list))), builtins.input, builtins.print, 1)
        delete_dict_from_dict_list(dict_list, index2)
    elif type == "orders" and sub_option == 5:
        print("Which entry do you want to update the status of?")
        index3 = get_val_int_input(((len(dict_list))), builtins.input, builtins.print, 1)
        update_order_status(dict_list, index3, builtins.input)
    
    print("Current List:")
    print_dict_list(dict_list, builtins.print)
    sub_menu(type, dict_list)

if __name__ == "__main__":
    main_menu()

