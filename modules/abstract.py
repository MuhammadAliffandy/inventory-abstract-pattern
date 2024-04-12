from abc import ABC, abstractmethod

class InventoryItem(ABC):

    def __init__ (
            self , 
            name = None , 
            code = None , 
            category = None , 
            description = None ,
            type = None,
            price = None , 
            quantity = None):
        self.name = name
        self.code = code
        self.category = category
        self.description = description
        self.type = type
        self.price = price
        self.quantity = quantity
        
    @abstractmethod
    def read_all(self): pass

    @abstractmethod
    def read_sorted(self): pass

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def delete(self): pass