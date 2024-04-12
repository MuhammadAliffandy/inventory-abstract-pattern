from modules.raw_material import RawMaterials
from modules.finished_material import FinishedMaterials
from tabulate import tabulate
import os

def render_table_list(): 
    data = Inventory(name='',code='',category='',description='',type='',price='',quantity='').read_sorted()
    headers = list(data[0].keys())
    rows = [list(item.values()) for item in data]

    rows_with_numbers = [[i+1] + row for i, row in enumerate(rows)]
    headers_with_number = ['No'] + headers
    
    print(tabulate(rows_with_numbers, headers=headers_with_number, tablefmt="grid"))

def input_data_material():
    print('---------------------------------')
    name = input('Name : ')
    print('---------------------------------')
    code = input('Code : ')
    print('---------------------------------')
    category = input('Category : ')
    print('---------------------------------')
    description = input('Description : ')
    print('---------------------------------')
    type = input('Type : ')
    print('---------------------------------')
    price = int(input('Price : '))
    print('---------------------------------')
    quantity = int(input('Quantity : '))
    print('---------------------------------')

    data = {
        "name" : name , "code" : code , "category" : category , 'description' : description , 'type' : type , 'price' : price , 'quantity' : quantity, 
    }

    return data

home = 'y'
program = False

while(program == False and home == 'y'):
    os.system('cls')
    print('\n= = = = Welcome To Inventory CENTER = = = = \n')
    print('1. Raw Material\n2. Finished Material\n')
    type_material = int(input('Choose your material to next (number) . . . : '))

    if(type_material == 1):
        Inventory = RawMaterials
        program = True
    elif(type_material == 2):
        Inventory = FinishedMaterials
        program = True


    while(program):

        os.system('cls')
        print('\n= = = = Inventory CENTER = = = = \n')
        print('1. Read Material\n2. Added Material\n3. Update Material\n4. Delete Material\n5. Back')

        action = int(input('Input the Number to next . . . : '))

        if(action == 1):
            os.system('cls')
            print('\n= = = = LIST DATA MATERIAL = = = = \n')
            render_table_list()
            input('\nEnter To BACK. . .')
            program = True

        elif(action == 2):
            os.system('cls')
            print('\n= = = = ADDED NEW MATERIAL = = = = \n')

            data = input_data_material()

            response = Inventory(name= data['name'],code=data['code'],category=data['category'],description=data['description'],type=data['type'],price=data['price'],quantity=data['quantity']).create()

            if(response == 0):
                print('\nADDED FAILED PLEASE REPEAT AGAIN')
                input('Enter To Next . . .')
            else:
                print('\nADDED SUCCESS')
                input('Enter To BACK. . .')
            program = True


        elif(action == 3):
            os.system('cls')
            print('\n= = = = UPDATE DATA MATERIAL = = = = \n')
            render_table_list()

            pick = int(input('Pick your number Data to update : '))

            os.system('cls')
            data = input_data_material()
            
            response = Inventory(name= data['name'],code=data['code'],category=data['category'],description=data['description'],type=data['type'],price=data['price'],quantity=data['quantity']).update(pick)

            if(response == 0):
                print('\nUPDATE FAILED PLEASE REPEAT AGAIN')
                input('Enter To Next . . .')
            else:
                print('\nUPDATE SUCCESS')
                input('Enter To BACK. . .')
                program = True

        elif(action == 4):
            os.system('cls')

            render_table_list()

            pick = int(input('Pick your number Data to delete : '))
            data = Inventory(name='',code='',category='',description='',type='',price='',quantity='').delete(pick)
            print('\nDELETED SUCCESS')
            input('Enter To BACK. . .')
            program = True
        elif(action == 5):
            os.system('cls')
            program = False
            home = 'y'
        else:
            os.system('cls')
            print('==== YOUR KEYWORD IS WRONG ====')
            input('Press ENTER to Repeat...')
            program = True