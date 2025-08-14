class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self ):
        color = "Red"
        return f"{color}"

class cycle(car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.type = "Cycle"
        
    
    
    
        
        
my_car = car("THAR", "THAR 4X4")

my_cycle = cycle("Hero", "Mountain Bike")
print(my_cycle.brand, my_cycle.model, my_cycle.type, my_cycle.full_name())

print(my_car.brand, my_car.model, my_car.full_name())
    