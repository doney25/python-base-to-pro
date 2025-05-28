class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
     
    def __str__(self):
        return (f'{self.brand},{self.model},{self.year}')
    
    def mode(self):
        print('Driving through road')    

class Boat: 
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def __str__(self):
        return (f'{self.brand},{self.model},{self.year}')
    
    def mode(self):
        print('Sailing through sea')    
        
class Plane: 
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def __str__(self):
        return (f'{self.brand},{self.model},{self.year}')
    
    def mode(self):
        print('Flying through air')          
        
c=Car("Toyota",'Innova',2020) 
print(c)      
c.mode()
b=Boat("Yamaha",'242X',2021)
print(b)    
b.mode()
p=Plane("Boeing",'747',2019)
print(p)
p.mode()
     