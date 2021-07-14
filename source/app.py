#based on week 1 and week 2 pdf - using what has been taught on the course

import app_functions as appfs

print("\n\nwelcome to app!\n\nloading data...")

raw_products, raw_couriers = appfs.load_data()

def main_menu():
    prod_list = raw_products
    cour_list = raw_couriers
    
    inp = appfs.get_menu_input("main")
    
    try:
        inp = int(inp)
    except:
        print("\nplease select 0 to 2\n")
        product_options(prod_list)
    
    if inp in list(range(3)):
        if inp== 0:
            appfs.save_data(prod_list, cour_list)
            print("Exiting App")
            exit()
        elif inp == 1:
            product_options(prod_list)
        elif inp == 2:
            courier_options(cour_list)
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
            appfs.print__applist(prod_list)
        elif inp2 == 2:
            appfs.add_appelement(prod_list)
            print("New Product List: ")
            appfs.print__applist(prod_list)
        elif inp2 == 3:
            appfs.update_appelement(prod_list)
            print("New Product List: ")
            appfs.print__applist(prod_list)
        elif inp2 == 4:
            appfs.delete_appelement(prod_list)
            print("New Product List: ")
            appfs.print__applist(prod_list)
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
        product_options(prod_list)
    
    if inp3 in list(range(5)):
        if inp3 == 0:
            main_menu()
        elif inp3 == 1:
            appfs.print__applist(cour_list)
        elif inp3 == 2:
            appfs.add_appelement(cour_list)
            print("New courier List: ")
            appfs.print__applist(cour_list)
        elif inp3 == 3:
            appfs.update_appelement(cour_list)
            print("New courier List: ")
            appfs.print__applist(cour_list)
        elif inp3 == 4:
            appfs.delete_appelement(cour_list)
            print("New courier List: ")
            appfs.print__applist(cour_list)
    else:
        print("\nplease select 0 to 5\n")
        courier_options(cour_list)
    courier_options(cour_list)

main_menu()
