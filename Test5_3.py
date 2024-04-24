class Building:
    total = 0
    def __init__(self):
        Building.total += 1

result = []
n = 40
while len(result) < n:
    new_building_No = Building()
    result.append(new_building_No)

for i in range (0,n):
    print('new_building_No=',i,result[i])

