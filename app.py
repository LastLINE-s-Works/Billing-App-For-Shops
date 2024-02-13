import random
import os,sys,time
from setuplogic import setupcheck

setupcheck()

def create_recipt_logic():
    
    customer_name = input("Customer Name: ")
    customer_mp = input("Customer Phone: ")
    unique_id_charset = input("Unique ID Charset (255): ")
    good_a = input("Item Name With x0: ")
    good_a_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt', 'w') as fp:
        pass
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(" Name - " + customer_name)
            f.write(" Phone - " + customer_mp)
            f.write(" Unique Identification - " + str(unique_id_charset))
            f.write(str(good_a +''+ good_a_mrp))
    good_extra_1 = input("Item Name With x0: ")
    good_extra_1_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
         old = f.read()
         f.write(good_extra_1 +''+ good_extra_1_mrp)
    
    good_extra_2 = input("Item Name With x0: ")
    good_extra_2_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(good_extra_2 +''+ good_extra_2_mrp)
    good_extra_3 = input("Item Name With x0: ")
    good_extra_3_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_3 +''+ good_extra_3_mrp))
    good_extra_4 = input("Item Name With x0: ")
    good_extra_4_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_4 +''+ good_extra_4_mrp))
    good_extra_5 = input("Item Name With x0: ")
    good_extra_5_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_5+''+good_extra_5_mrp))
    good_extra_6 = input("Item Name With x0: ")
    good_extra_6_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_6+''+good_extra_6_mrp))
    good_extra_7 = input("Item Name With x0: ")
    good_extra_7_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read() 
            f.write(str(good_extra_7+''+good_extra_7_mrp))
    good_extra_8 = input("Item Name With x0: ")
    good_extra_8_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_8+''+good_extra_8_mrp))
    good_extra_9 = input("Item Name With x0: ")
    good_extra_9_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_9+''+good_extra_9_mrp))
    good_extra_10 = input("Item Name With x0: ")
    good_extra_10_mrp = input('MRP: ')
    with open(f'data/{unique_id_charset}-data.txt' ,'r+') as f:
            old = f.read()
            f.write(str(good_extra_10+''+good_extra_10_mrp))
    total_mrp = input("Total: ")
    with open(f'data/{unique_id_charset}-data.txt','r+') as f:
           old = f.read()
           f.write('Total MRP - ','',str(total_mrp))
    #Allowance For Printing Recipt
    ask_print = input("Print Recipt (Y/N): ")
    if ask_print == 'y'or'Y'or'Yes'or'yes':
           print("--------------------------")
           print("")
           print("Shop Name     &      Whole Recipt")
           print('')
           print('Name - '+customer_name)
           print('')
           print('Unique Identity Code - '+unique_id_charset)
           print('')
           print("--------------------------")
           print('')
           print('Made By Lamgerr !')
           print('')
           print("Items -              MRP -")
           print("")
           print(good_a        ,       'INR'+good_a_mrp+'/-')
           print(good_extra_1  ,       'INR'+good_extra_1_mrp+'/-')
           print(good_extra_2  ,       'INR'+good_extra_2_mrp+'/-')
           print(good_extra_3  ,       'INR'+good_extra_3_mrp+'/-')
           print(good_extra_4  ,       'INR'+good_extra_4_mrp+'/-')
           print(good_extra_5  ,       'INR'+good_extra_5_mrp+'/-')
           print(good_extra_6  ,       'INR'+good_extra_6_mrp+'/-')
           print(good_extra_7  ,       'INR'+good_extra_7_mrp+'/-')
           print(good_extra_8  ,       'INR'+good_extra_8_mrp+'/-')
           print(good_extra_9  ,       'INR'+good_extra_9_mrp+'/-')
           print(good_extra_10 ,       'INR'+good_extra_10_mrp+'/-')
           print('Total - '    ,       str(total_mrp))
    else:
           quit()
print("Welcome, To BAFS System")
time.sleep(2)

create_recpit = print("a. Create Recipt")
read_data = print("b. Read Data")
delete_data = print("c. Delete Data")
print("")
print("")
greet = input("Select B/w ?: ")

if greet == "a":
    create_recipt_logic()

#if greet == "b":
   # read_data_logic()