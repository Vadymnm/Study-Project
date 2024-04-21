# class House:
#
#     def __init__(self):
#         self.numberOfFloors = 10
#         self.FloorNo = 0
#
#     def printFloor(self):
#         print('Текущий Этаж № ', self.FloorNo)
#
#
# my_house = House()
#
# print('==================================')
# print(' --- UP ---')
# my_house.FloorNo = 0
# while my_house.FloorNo < my_house.numberOfFloors:
#     my_house.FloorNo += 1
#     my_house.printFloor()
#
# print('==================================')
# print(' --- DOWN ---')
# while my_house.FloorNo >= 1:
#     my_house.printFloor()
#     my_house.FloorNo -= 1

class House:

    def __init__(self):
        self.numberOfFloors = 10
        self.FloorNo = 0

    def printFloor(self):
        print('Текущий Этаж № ', self.FloorNo)

    def setNewNumberOfFloors(self, floors):
        self.comtent = floors
        print(self.numberOfFloors)



my_house = House()

print('==================================')
my_house.setNewNumberOfFloors(10)

# print('==================================')
# print(' --- DOWN ---')
# while my_house.FloorNo >= 1:
#     my_house.printFloor()
#     my_house.FloorNo -= 1