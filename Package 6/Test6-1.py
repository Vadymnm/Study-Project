
class Car:
    price = 1000000
    horse_power = 99
    def __init__(self,name):
        self.name = name

    def horse_powers(self):
        self.horse_power = 88
        print(self.__class__.__name__, self.name,':','horse power =',self.horse_power )
        return(self.horse_power)
    def __str__(self):
        return '{} {} цена =  {}, horse_power = {}'.format(
            self.__class__.__name__, self.name, self.price, self.horse_power)

class Nissan(Car):
    horse_power = 125
    price = 500000
    def horse_powers(self):
        self.horse_power = 77
        print(self.__class__.__name__, self.name,':','horse power =',self.horse_power )
        return(self.horse_power)

class KIA (Car):
#    horse_power = 110
#    price = 2500000
    pass
    def horse_powers(self):
        print(self.__class__.__name__, self.name, ':', 'horse power =', self.horse_power)


my_patrol = Nissan(name='Patrol')
my_rio = KIA(name='Rio')

print('===============================================')
print('-----параметр horse_power выбирается из атрибутов  наследника класса Car - Nissan')
print()
print(my_patrol)
print('===============================================')
print('----параметр horse_power определяется  функцией horse_powers() из наследника класса Car - Nissan')
print()
my_patrol.horse_powers()
print(my_patrol)

print('***********************************************')
print('----параметр horse_power выбирается из атрибутов  родительского класса Car')
print()

print(my_rio)
my_rio.horse_powers()

print('===============================================')