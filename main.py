def test_1(a,b=25,*args,**kwargs):
    print('a = ',a,'b = ',b)
    print('type args = ',type(args))
    print('args = ',args)
    for i, arg in enumerate(args):
        print('позиционный параметр:  i = ',i, 'arg = ',arg)

    print('type args = ',type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный параметр:  key = ',key, 'value = ',value)

test_1(3,4,6,8,9,dog='gav gav',cat='мяу мяу')
print('-----------------------------------------------')
test_1(3,5,77,88,99,dog='gav gav',cat='мяу мяу')
print('-----------------------------------------------')
test_1(a=3,dog='gav gav',cat='мяу мяу')

#  *****************************************************************************
#  ****** FACTORIAL ********

print( '****** FACTORIAL - 4 варианта  ********' )
print('Введите  число')
n = int(input())
print(n)
#  ----------------------------------------
def fact(n):
    if n ==1:
#        result = 1
        return 1
    result = fact(n-1)
    return n * result

print('рекурсия', fact(n))
# ==============================
i = 1
fact = 1
while i <= n:
    fact = fact*i
    i += 1
print('while', fact)
# ===============================
fact = 1
for i in range(1,n+1):
    fact = fact*i
print('for  ', fact)
# ===============================
import math
fact =  math.factorial(n)
print('Lib  ', fact)
# ===============================