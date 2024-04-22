class Building:

    def __init__(self):
        self.numberOfFloors = 2
        self.buildingType = 'Industrial'

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors

    def setNewType(self,type):
        self.buildingType = type

    def __eq__(self,other):
        return (self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType)

print('==================================')

my_building = Building()
other_building = Building()

print('my_building :    ', my_building.numberOfFloors,'Floors;', 'Type =', my_building.buildingType)
print('other_building : ', other_building.numberOfFloors,'Floors;', 'Type =', other_building.buildingType)

if Building.__eq__(self=my_building, other=other_building):
    print('Equal !')
else:
    print('N/Equal !')

print('==================================')

floors = 5
type = 'Trading'

other_building.setNewNumberOfFloors(floors)
other_building.setNewType(type)

print('my_building :    ', my_building.numberOfFloors,'Floors;', 'Type =', my_building.buildingType)
print('other_building : ', other_building.numberOfFloors,'Floors;', 'Type =', other_building.buildingType)

if Building.__eq__(self=my_building, other=other_building):
    print('Equal !')
else:
    print('N/Equal !')

print('==================================')

