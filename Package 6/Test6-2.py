class Vehicle:
    vehicle_type = None

class Car:
    price = 1000000
    def __init__(self,name):
        self.name = name
    def horse_powers(self):
        self.horse_power = 88
        print(self.__class__.__name__, self.name,':','horse power =',self.horse_power )
        return(self.horse_power)

class Nissan(Car,Vehicle):
    price = 1500000
    vehicle_type = 'Crossover'
    def horse_powers(self):
        self.horse_power = 111
        print(self.__class__.__name__, self.name,':','Horse power =',self.horse_power )
        return(self.horse_power)

class KIA(Car,Vehicle):
#    price = 500000
    vehicle_type = 'Hachback'

my_patrol = Nissan(name='Patrol')

print('===============================================')
print()
my_patrol.horse_powers()
print('Vehicle_type: ',my_patrol.vehicle_type,';','Price = ',my_patrol.price,';')
print()
print('===============================================')

my_rio = KIA(name='Rio')
print()
my_rio.horse_powers()
print('Vehicle_type: ',my_rio.vehicle_type,';','Price = ',my_rio.price,';')
print()
print('===============================================')