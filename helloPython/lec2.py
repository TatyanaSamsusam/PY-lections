# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'w') # w - rewrite, a - create, r - read
# data.writelines(colors) # without tabs
# data.write('\nline1\n')
# data.write('line45')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# def new_string (symbol, count = 3):    # функция с возвратом значения
#     return symbol * count
# print (new_string('!',5))              # распечатать воскл знак 5 раз 
# print (new_string('!'))                # распечатать воскл знак 3 раза по умолчанию
# print (new_string(3))                   # распечатать результат умножения 3 на 3


# def concatenatio (*params):        
#     res: int = 0                   
#     for i in params:
#         res += i               
#     return res                      

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))
# print(concatenatio(1, 2, 3, 4))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range (1, 10):
#     list.append(fib(e))
# print(list)

# a = (1,2,56,4)   # кортеж, т.е. неизменяемый список
# print(a[-1])

# t = tuple(['red', 'green', 'yellow']) 
#  print(t[0])      #red
#  print(t[-2])    #green

# for e in t:
#     print(e)

# t = tuple(['red', 'green', 'blue'])  # создали список и конвертировали его в кортеж 
# red, green, blue = t                 # распаковала кортеж и превратила его в три независимые переменные
# print ('r:{} g:{} b:{}'.format(red, green, blue))

dictionary = {}                  # словарь: 
dictionary = \
    {
        'up': 1,
        'left': 2,
        'right': 3,
        'down': 4
    }
print (dictionary)
print(dictionary['down'])

for k in dictionary.keys(): # распечатать ключи
    print(k)

for k in dictionary.values(): # распечатать значения
    print(k)