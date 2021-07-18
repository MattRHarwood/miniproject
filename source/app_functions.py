
def load_data():
    with open("./products.txt", "r") as prod_file:
        raw_products = [prod.rstrip("\n") for prod in prod_file.readlines()]
        print("Products loaded successfully!")

    with open("./couriers.txt", "r") as cour_file:
        raw_couriers = [cour.rstrip("\n") for cour in cour_file.readlines()]
        print("Couriers loaded successfully!")

    return raw_products, raw_couriers

def save_data(new_prods, new_cours):
    with open("./products.txt", "w") as prod_file:
        for i in range(len(new_prods)):
            prod_file.write(new_prods[i] + "\n")
        print("Products saved successfully!")

    with open("./couriers.txt", "w") as cour_file:
        for i in range(len(new_cours)):
            cour_file.write(new_cours[i] + "\n")
        print("Couriers saved successfully!")


def get_menu_input(type):
    main_options = {0 : "Save and Exit", 
                1 : "Product Options", 
                2 : "Courier Options", 
                3 : "Order Options"}
    sub_options = {0 : "Return to main menu", 
                1 : "Print current items", 
                2 : "Add item",   
                3 : "Update item", 
                4 : "Delete item"} 
    
    if type == "main":
        print("\nMain Menu\n")
        for key, value in main_options.items():
            print(f"\n{key} - {value}")
        print("\n\n")
    
    elif type == "sub":
        print("\nList Menu\n")
        for key, value in sub_options.items():
            print(f"\n{key} - {value}")
        print("\n\n")
    
    else:
        print("error taking input")
            
    inp = input("enter menu option no.: ")
    return inp

def print_applist(app_list):
    for key, value in enumerate(app_list):
        key += 1
        print(f"\n{key} - {value}")
    print("\n")

def delete_appelement(app_list):
    target = int(input("Please enter the No. you want to delete: "))
    app_list.pop(target - 1)

def update_appelement(app_list):
    old = int(input("Please enter the No. you want to update: "))
    new = input("Now enter what you want to change it to:  ")
    app_list[old - 1] = new
    
def add_appelement(app_list):
    new_prod = input("Enter new entry: ")
    app_list.append(new_prod)

def print_dictlist(dict_list):
    for i in range(len(dict_list)):
        print(f"ORDER {i+1}")
        for key, value in dict_list[i].items():
            print(f"{key} : {value}")
    print("\n")

def update_dict(dict_list):
    None

def delete_dict(dict_list):
    None

def add_dict_input(cour_list):
    name = input("enter customer name: ")
    address = input("enter customer address: ")
    phone_number = input("enter customer phone number: ")
    
    print_applist(cour_list)
    courier = int(input("enter desired courier: "))
    return name, address, phone_number, courier

def add_ord_dict(dict_list, name, address, phone_number, courier):
    new_ord = {"customer_name": name,
    "customer_address": address,
    "customer_phone": phone_number,
    "courier": courier,
    "status": "preparing"}
    dict_list.append(new_ord)