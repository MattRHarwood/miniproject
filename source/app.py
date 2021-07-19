#based on week 1 and week 2 pdf - using what has been taught on the course

import app_functions as appfs

print("\n\nwelcome to app!\n\nloading data...")

try:
    raw_products, raw_couriers = appfs.load_data()
except:
    print("could not load data!")

ord1 = {"customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "courier": 2,
    "status": "preparing"}
ord2 = {"customer_name": "Matt",
    "customer_address": "55 Colmore Row, BIRMINGHAM, B3 2AA",
    "customer_phone": "07860830555",
    "courier": 1,
    "status": "preparing"}
raw_orders = [ord1, ord2]

def main_menu():
    prod_list = raw_products
    cour_list = raw_couriers
    ord_list = raw_orders
    
    inp = appfs.get_menu_input("main")
    
    try:
        inp = int(inp)
    except:
        print("\nplease select 0 to 3\n")
        product_options(prod_list)
    
    if inp in list(range(4)):
        if inp == 0:
            try:
                appfs.save_data(prod_list, cour_list)
            except:
                print("could not save product data!")
            print("Exiting App")
            exit()
        elif inp == 1:
            product_options(prod_list)
        elif inp == 2:
            courier_options(cour_list)
        elif inp == 3:
            order_options(ord_list, cour_list)
    else:
        print("\nplease select valid input\n")
        main_menu()

def product_options(prod_list):
    inp2 = appfs.get_menu_input("sub")
    
    try:
        inp2 = int(inp2)
    except:
        print("\nplease select 0 to 5\n")
        product_options(prod_list)
        

    if inp2 in list(range(5)):
        if inp2 == 0:
            main_menu()
        elif inp2 == 1:
            appfs.print_applist(prod_list)
        elif inp2 == 2:
            appfs.add_appelement(prod_list)
            print("New Product List: ")
            appfs.print_applist(prod_list)
        elif inp2 == 3:
            appfs.update_appelement(prod_list)
            print("New Product List: ")
            appfs.print_applist(prod_list)
        elif inp2 == 4:
            appfs.delete_appelement(prod_list)
            print("New Product List: ")
            appfs.print_applist(prod_list)
    else:
        print("\nplease select 0 to 5\n")
        product_options(prod_list)
    product_options(prod_list)

def courier_options(cour_list):
    inp3 = appfs.get_menu_input("sub")
    
    try:
        inp3 = int(inp3)
    except:
        print("\nplease select 0 to 5\n")
        order_options(cour_list)
    
    if inp3 in list(range(5)):
        if inp3 == 0:
            main_menu()
        elif inp3 == 1:
            appfs.print_applist(cour_list)
        elif inp3 == 2:
            appfs.add_appelement(cour_list)
            print("New courier List: ")
            appfs.print_applist(cour_list)
        elif inp3 == 3:
            appfs.update_appelement(cour_list)
            print("New courier List: ")
            appfs.print_applist(cour_list)
        elif inp3 == 4:
            appfs.delete_appelement(cour_list)
            print("New courier List: ")
            appfs.print_applist(cour_list)
    else:
        print("\nplease select 0 to 5\n")
        courier_options(cour_list)
    courier_options(cour_list)

def order_options(ord_list, cour_list):
    inp4 = appfs.get_menu_input("sub")
    
    try:
        inp4 = int(inp4)
    except:
        print("\nplease select 0 to 5\n")
        order_options(ord_list, cour_list)
    
    if inp4 in list(range(6)):
        if inp4 == 0:
            main_menu()
        elif inp4 == 1:
            appfs.print_dictlist(ord_list)
        elif inp4 == 2:
            name, address, phone_number, courier = appfs.add_dict_input(cour_list)
            appfs.add_ord_dict(ord_list, name, address, phone_number, courier)
            print("New order List: ")
            appfs.print_dictlist(ord_list)
        elif inp4 == 3:
            appfs.print_dictlist(ord_list)
            to_update = int(input("enter which order no you want to update")) - 1
            appfs.update_dict(ord_list[to_update])
            print("New order List: ")
            appfs.print_dictlist(ord_list)
        elif inp4 == 4:
            appfs.delete_dict(ord_list)
            print("New order List: ")
            appfs.print_dictlist(ord_list)
        elif inp4 == 5:
            appfs.update_ord_status(ord_list)
    else:
        print("\nplease select 0 to 5\n")
        order_options(ord_list)
    order_options(ord_list, cour_list)

main_menu()
