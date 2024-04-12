from modules.abstract import InventoryItem
import os
import json
import random

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data_folder_path = os.path.join(parent_dir, "data")
json_path = os.path.join(data_folder_path, "inventory.json")

class FinishedMaterials(InventoryItem):
    def __init__ (
        self , 
        name , 
        code , 
        category , 
        description ,
        type ,
        price , 
        quantity):
        super().__init__(
            name , 
            code , 
            category , 
            description ,
            type,
            price , 
            quantity)
    
    @staticmethod    
    def loadData():
        with open(json_path, "r") as file:
            prevData = json.load(file)
        return prevData
    
    def create(self): 
        id = random.randint(1,10000)

        data = {
            "id": id,
            "name" : self.name , 
            "code" : self.code , 
            "category" : self.category , 
            "description" : self.description ,
            "type": self.type,
            "price" : self.price , 
            "quantity" : self.quantity
        }

        try:
            prevData = self.loadData()
            finished_materials = [
                *prevData,
                data,
            ]
        except json.JSONDecodeError:
            finished_materials = [
                data,
            ]
        with open(json_path, "w") as file:
            json.dump(finished_materials,file)

        return data
    

    def read_all(self):
        try:
            data = self.loadData()
            dataFiltered = list(filter(lambda x: x['type'] == 'finished', data))
            return dataFiltered
        except json.JSONDecodeError:
            return 0

    def read_sorted(self): 
        try:
            dataFiltered = self.read_all()
            sorted_data = sorted(dataFiltered, key=lambda x: x['id'])
            dataSorted =  sorted_data
            return dataSorted
        except json.JSONDecodeError:
            return 0


    def update(self , pick):
        data = self.read_sorted()
        dataPicked = data[pick]['id']

        data_material = self.loadData()
        
        for data in data_material:
            if(data['id'] == dataPicked): 
                data['name'] = self.name
                data['code'] = self.code  
                data['category'] = self.category  
                data['description'] = self.description
                data['type'] = self.type
                data['price'] = self.price
                data['quantity'] = self.quantity

            with open(json_path, "w") as file:
                json.dump(data_material,file)

    def delete(self , pick ):
        data = self.read_sorted()
        dataPicked = data[pick - 1 ]['id']
        prevData = self.loadData()
        dataFiltered = list(filter(lambda x: x['type'] == 'finished',prevData))
        dataFilteredPrev = list(filter(lambda x: x['type'] == 'raw',prevData))
        for data in dataFiltered: 
            if(data['id'] == dataPicked):
                if(len(dataFiltered) == 1):
                    newData = []
                else:
                    dataFiltered.remove(data)
                    newData = dataFiltered + dataFilteredPrev
                with open(json_path, "w") as file:
                    json.dump(newData,file)