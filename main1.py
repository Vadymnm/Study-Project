# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# -----------------------
def test():
    a = 5
    b = 8
    print(a,b)
# -----------------------
def test2(a,b,c):
    print(a,b,c)
# -----------------------
def test3(a,b,c):
    print(a,b,c)
    c = 'String'
    b = True
    print(a, b, c)
# -----------------------
def test4():
    global b, c
    print(a, b, c)
    c = 'String'
    b = True
    print(a, b, c)

a = 10
b = 15
c = 20
test()
test2(a,b,c)
test3(4,b,c)
test4()
print(a, b, c)
