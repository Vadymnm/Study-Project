#  ===============================
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(a=5)
print_params(b = 'string')
print_params(c = False)
print_params(a = 8, c = True)
print_params(b = 25 )
d = [1,2,3]
print_params(c = d )
# ---------------------
print('Созданные  последовательности:')
values_list = [3,'Hello',True]
values_dict = {'a': 8, 'b': ' Dict','c': False}
values_list_2 = [1.5,'Привет']
print(values_list)
print(values_dict)
print(values_list_2)
print('Результат')
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)