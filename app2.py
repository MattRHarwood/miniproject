#Week 4 miniproject

print("Welcome to App!\n\n")

def main_menu():
    prod_list = raw_products
    cour_list = raw_products
    ord_list = raw_products
    
    print("Main Menu:\n\n"
        + "0 - Save and Exit\n\n" 
        + "1 - Products Menu\n\n"
        + "2 - Couriers Menu\n\n"
        + "3 - Orders Menu\n\n")
    
    menu_option = get_val_int_input(4)
    
    if menu_option == 0:
        save_products(prod_list)
        save_couriers(cour_list)
        save_orders(ord_list)
        
        exit()
    elif menu_option == 1:
        sub_menu("products", prod_list)
    elif menu_option == 2:
        sub_menu("couriers", cour_list)
    elif menu_option == 3:
        sub_menu("orders", ord_list)
    else:
        main_menu()

def sub_menu(type : str, dict_list : list):
    print(f"{type.title()} Menu:\n\n"
        + "0 - Return to Main Menu\n\n"
        + f"1 - Print {type.title()} List\n\n"
        + f"2 - Add to {type.title()} List\n\n"
        + f"3 - Update {type.title()} List\n\n"
        + f"4 - Delete from {type.title()} List\n\n")
    if type == "orders":
        print("5 - Update Order Status\n\n")
        sub_option = get_val_int_input(6)
    else:
        sub_option = get_val_int_input(5)
    
    if sub_option == 0:
        main_menu()
    elif sub_option == 1:
        print_dict_list(dict_list)
    elif sub_option == 2:
        add_to_dict_list(dict_list)
    elif sub_option == 3:
        None
    elif sub_option == 4:
        None
    elif type == "orders" and sub_option == 5:
        None
    else:
        sub_menu(type, dict_list)

raw_products = load_product_csv()
raw_couriers = load_couriers_csv()
raw_orders = load_orders_csv()
main_menu()

