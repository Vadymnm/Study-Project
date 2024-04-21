
class House:

    def __init__(self):
        self.numberOfFloors = 0
    #    self.FloorNo = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('New number of Floors = ',self.numberOfFloors)



my_house = House()

print('Initial number of Floors = ',my_house.numberOfFloors)
print('==================================')
floors = 18
my_house.setNewNumberOfFloors(floors)

