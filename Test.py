#
# #  ****** FACTORIAL ********
#
# n = int(input())
# print(n)
# i = 1
# fact = 1
# while i <= n:
#     fact = fact*i
#     i += 1
# print('while', fact)
# # ===============================
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print('for  ', fact)
# # ===============================
#
# import math
# fact =  math.factorial(n)
# print('Lib  ', fact)
# # ===============================

#  ****** Ряд и числа FIBONACCI ********
#  =========================
# n = int(input())
# print(n)
# fib=[0]*n
# fib[0] = 1
# fib[1] = 1
# for i in range(2,n):
#     fib[i] = fib[i-1]+fib[i-2]
# print(fib)
# #  =========================
# #  Рекурсивное вычисление n-го числа ряда Фибоначчи
# def fibonacci(i):
#     if i in (1, 2):
#         return 1
#     return fibonacci(i - 1) + fibonacci(i - 2)
#
# print(fibonacci(n))

# # ===============================

#  ****** Нахождение максимума в списке ********
#  =========================
# def maximum1(x):
#     max_ = 0
#     for i in range(0,len(x)):
#         if x[i] > max_:
#             max_ = x[i]
#     return(max_)
# #  =========================
# def maximum2(x):
#     x.sort(reverse=True)
#     return(x[0])
#
# #  =========================
#
# list_ = [1,2,14,88,3,16,19,411,55,72,44,96,88,452,846]
# print(len(list_))
#
# print('Maximum number1 = ',maximum1(list_))
# print('Maximum number2 = ',maximum2(list_))

#  ===============================
#  ******  Вывод чисел с заданным кол-вом знаков после запятой ********
#  ===============================
# a = 100
# b = 26
# print(a/b)
# print(round(a/b,3))
# print(f"{(a/b):.3f}")
#  ===============================
#  ****** lst_ = [['*','*'],[],[]]  ********
#  ===============================
# lst_ = [['*','*'],[],[]]
# print(lst_)
# #print(lst_[0])
# lst_[0].append('*')
# lst_[1] = lst_[0]
# lst_[2] = lst_[0]
# #print(lst_[0])
# print(lst_)
# #  [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
#  ===============================
# def test():
#     a = 5
#     b = 8
#     print(a,b)
# # -----------------------
# def test2(a,b,c):
#     print(a,b,c)
# # -----------------------
# def test3(a,b,c):
#     print(a,b,c)
#     c = 'String'
#     b = True
#     print(a, b, c)
# # -----------------------
# a = 10
# b = 15
# c = 20
# test()
# test2(a,b,c)
# test3(4,b,c)

#  ===============================
#  ===============================

#       ++++++++++++ 03.04.2024 ++++++++++++++++

# def test_1(a,b=25,*args,**kwargs):
#     print('a = ',a,'b = ',b)
#     print('type args = ',type(args))
#     print('args = ',args)
#     for i, arg in enumerate(args):
#         print('позиционный параметр:  i = ',i, 'arg = ',arg)
#
#     print('type args = ',type(kwargs))
#     print(kwargs)
#     for key, value in kwargs.items():
#         print('именованный параметр:  key = ',key, 'value = ',value)
#
# test_1(3,4,6,8,9,dog='gav gav',cat='мяу мяу')
# print('-----------------------------------------------')
# test_1(3,5,77,88,99,dog='gav gav',cat='мяу мяу')
# print('-----------------------------------------------')
# test_1(a=3,dog='gav gav',cat='мяу мяу')
#
# #  *****************************************************************************
# #  ****** FACTORIAL ********
#
# print( '****** FACTORIAL - 4 варианта  ********' )
# print('Введите  число')
# n = int(input())
# print(n)
# #  ----------------------------------------
# def fact(n):
#     if n ==1:
# #        result = 1
#         return 1
#     result = fact(n-1)
#     return n * result
#
# print('рекурсия', fact(n))
# # ==============================
# i = 1
# fact = 1
# while i <= n:
#     fact = fact*i
#     i += 1
# print('while', fact)
# # ===============================
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print('for  ', fact)
# # ===============================
# import math
# fact =  math.factorial(n)
# print('Lib  ', fact)
# # ===============================

#       ++++++++++++ 04.04.2024 ++++++++++++++++

# help(dir)
# list_ = [1,2,14,88,3,16,19,411,55,72,44,96,88,452,846]
# #print(dir(list_))
# print(id(list_))

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list1)
# print (filter(lambda x: x % 2 == 0, list1))
# print(list(filter(lambda x: x % 2 == 0, list1)))
# print(list(map(lambda x: pow(x, 2), list1)))

#       ++++++++++++ 05-06.04.2024 ++++++++++++++++
# 1.
# a = [1,2,3]
# b = a
# print(a)
# print(b)
# b.append(4)
# print(a)
# print(b)

# 2. - list comprehension
# ===============================

# list = [i**2 for i in range(1,11)]
# print(list)

# 3. Слайсинг.
# ===============================

# list = [1,2,3,4,5,6,7,8,9]
# print(list)
# print(list[0:9])
# list1 = [list[-i] for i in range(1,10)]
# print(list1)
# print(list1[0:9:2])
# print(list1[::2])

# 4. Bool.
## ===============================


# print(bool(''))     # - отсутствует параметр - False
# print(bool(None))   # - отсутствует параметр - False
# print(bool(0))      # - отсутствует параметр - False
# print(bool('0'))    # - параметр = 0  -> True

# 4. Параметры и аргументы функции.
# ===============================

# ПАРАМЕТРЫ (переменные, которые используются при создании  функции)
#   -  Обязательные
#   -  Необязтельные (по умолчанию)
# АРГУМЕНТЫ (данные, которые  передаются функции  при вызове)
#   - Позиционные ( sum(1,2))
#   - Ключевые(именованные)  (sum(a=1,b=2))
#   - Позиционные  Переменной длины (*args)
#   - Ключевые(именованные)  Переменной длины (**kwargs)

# 5. Бинарный поиск.
# ===============================

# import random
# def compare(a,x,i):
#     if a < x:
#         print('i=',i, 'загаданное  число меньше', a, '<',x)
#     if a > x:
#         print('i=',i,'загаданное  число больше', a, '>',x)
#     if a == x:
#         print('i=',i,'УРА!,  вы угадали число', a, '=',x)
#
# n = int(input())
# print(n)
# i=1
# x = random.randrange(1, 100)
# while (n != x):
#     x = random.randrange(1, 100)
# #    print(x)
#     compare(n,x,i)
#     i += 1
#
# 6. Sum_range.
# ===============================

# import time
# def sum_range(a,b):
#     sum = 0
#     for i in range(a,b+1):
#         sum += i
#     return(sum)
#
# a = int(input())
# b = int(input())
# start = time.time()
# print('Сумма чисел от',a,'до',b,' = ',sum_range(a,b))
# end = time.time()
# print(start, end, end-start)

# 7. Треугольник. -- (условие существования: |a - b| < c < a + b )
# ===============================

# def triangle(x,y,z):
#     if abs(x-y) < z and x+y >z:
#         print ('OK')
#     else:
#         print ('NA')
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(a,b,c)
# triangle(a,b,c)

# 8. Счастливый билет. -- ( abcdef:  a+b+c = d+e+f)
# ===============================

# import random
#
# lst=[]
# for i in range(0,6):
#     lst.append(random.randrange(0, 9))
# print(lst)
# if (lst[0]+lst[1]+lst[2]) == (lst[3]+lst[4]+lst[5]):
#     print('УРА!!!  СЧАСТЛИВыЙ')
# else:
#     print('УВЫ!!!')

# 9. Len для строк
# ===============================
# import random
# def len_(args):
#     j = 0
#     for i in lst:
#         j += 1
#     return(j)
#
# lst=[]
# x = random.randrange(5, 25)
# print(x)
# for i in range(0,x):
#     lst.append(random.randrange(0, 9))
# print(lst)
#
# print(len_(lst))

# 10. Шифр  Цезаря
# ===============================

# print( 'Введите  индекс кодирования (+)/декодирования (-)')
# k = int(input())
#
# lst_in = []
# lst_out = []
# lst = []
# str_in = 'значения по умолчанию' # - строка для кодирования
# #str_in = 'пхзямхрёжчцжыфцуязхре' # - строка для декодирования
# str_out =''
# # ----- формирование списков из строк --------
# j=0
# for i in str_in:
#     lst_in.append(str_in[j])
#     lst_out.append(str_in[j])
#     j += 1
# #print(lst_in)
# #print(lst_out)
#
# str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ' # - строка для ключа кодирования
#
# for i in range (0,34):
# #     print(i, str[i])
#      lst.append(str[i])
# #print(lst)
# # - кодирование списков
# print('________________________________')
# for i in range(0,len(lst_in)):
#     x = lst_in[i]
#     ind = lst.index(x)
#     ind1=(ind+k) % 34
#     lst_out[i] = lst[ind1]
#
# print(lst_in)   # - исходный  список
# print(lst_out)  # - закодированный  список
# print('________________________________')
# # --- преобразование списков в строки и печать
# print(''.join(lst_in))
# str_out = str_out.join(lst_out)
# print(str_out)

# 11. Определение  високосного  года.
# ===================================
#
# print( 'Введите  год')
# a = int(input())
# if (a % 400 == 0)  or (a % 4 == 0 and a % 100 != 0):
#     print (a,' - ','ВИСОКОСНЫЙ')
# else:
#     print(a, ' - ', 'ОБЫЧНЫЙ')
#
# 12. Расчет стоимости доставки ( оператор if).
# =============================================
#
# print( 'Введите  вес  посылки')
# a = int(input())
# if a <= 2:
#     price = 50
# if 10 > a > 2:
#     price = 50 + (a-2)*20
# if a >= 10:
#     price = 200
# print(price)

# 13. Поиск  простых  чисел  ( цикл  while).
# =============================================

# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
# print( 'Введите  число ( 1....N)')
# n = int(input())
# lst = [1]
# i = 2
# while i < n:
#     x = IsPrime(i)
#     if x == True:
#         lst.append(i)
#     i +=1
# print(lst)
# print(len(lst))

# 14. Угадай  число  ( цикл  while).
# =============================================
#
# import random
# def compare(a,x,i):
#     if a < x:
#         print('i=',i, 'загаданное  число меньше', a, '<',x)
#     if a > x:
#         print('i=',i,'загаданное  число больше', a, '>',x)
#     if a == x:
#         print('i=',i,'УРА!,  вы угадали число', a, '=',x)
#
# n = int(input())
# print(n)
# i=1
# x = random.randrange(1, 100)
# while (n != x):
#     x = random.randrange(1, 100)
# #    print(x)
#     compare(n,x,i)
#     i += 1

# 14. Таблица умножения  ( цикл  for).
# =============================================
#
# tbl=[0]*10
# for i in range(0,10):
#     tbl[i]=[0]*10
# for i in range(0,10):
#     for j in range (0,10):
#         tbl[i][j]=(i+1)*(j+1)
# for i in range(0,10):
#     print(tbl[i])
#
# s='0'
# for i in range(0,10):
#     s = s + ' '+str(tbl[1][i])
# print(s)

# 15. Сумма  ряда  ( цикл  for).
# =============================================

# import random
#
# print( 'Введите  длину  строки ( 1....N)')
# n = int(input())
#
# lst=[]
# for i in range(0,n):
#     lst.append(random.randrange(0, 100))
# print(lst)
#
# sum = 0
# for i in range(0,len(lst)):
#     sum = sum + lst[i]
# print(sum)