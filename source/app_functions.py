
def load_data():
    try:
        with open("./products.txt", "r") as prod_file:
            raw_products = [prod.rstrip("\n") for prod in prod_file.readlines()]
            print("Products loaded successfully!")
    except:
        print("could not load product data!")

    try:
        with open("./couriers.txt", "r") as cour_file:
            raw_couriers = [cour.rstrip("\n") for cour in cour_file.readlines()]
            print("Couriers loaded successfully!")
    except:
        print("could not load courier data!")
    return raw_products, raw_couriers

def save_data(new_prods, new_cours):
    try:
        with open("./products.txt", "w") as prod_file:
            for i in range(len(new_prods)):
                prod_file.write(new_prods[i] + "\n")
            print("Products saved successfully!")
    except:
        print("could not save product data!")
        
    try:
        with open("./couriers.txt", "w") as cour_file:
            for i in range(len(new_cours)):
                cour_file.write(new_cours[i] + "\n")
            print("Couriers saved successfully!")
    except:
        print("could not save courier data!")  

def get_menu_input(type):
    main_options = {0 : "Save and Exit", 1 : "Product Options", 2 : "Courier Options"}
    sub_options = {0 : "Return to main menu", 1 : "Print current items", 2 : "Add item", 3 : "Update item", 4 : "Delete item"}
    
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

def print__applist(app_list):
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