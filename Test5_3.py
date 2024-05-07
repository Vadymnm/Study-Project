# class Building:
#     total = 0
#     def __init__(self):
#         Building.total += 1
#
# result = []
# n = 5
# while len(result) < n:
#     new_building_No = Building()
#     result.append(new_building_No)
#
# for i in range (0,n):
#     print('new_building_No=',i,result[i])


import sys
from termcolor import colored, cprint


text = colored('Hello, My World!', 'red', attrs=['reverse', 'blink'])
cprint('Hello, Our World!', 'green', 'on_red')
cprint(text, 'green', 'on_red')


def print_red_on_cyan(x):
    return cprint(x, 'red', 'on_cyan')


print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'red', end=' ')
print()
print('===================')

cprint("Attention!  !!!!", 'red', attrs=['bold'], file=sys.stderr)
