
# def f(x):              
#     return x**2
# print (f(2))        # можно не помещать ф-ю в переменную, а просто напечатать ее результат через принт, подставив число в аргумент

# f = lambda x: x**2
# print (f(2))        # кратко написала то же самое, что выше, через лямбду

# def f(x):              
#     return x**2
# g = f                # вложила в переменную g функцию f 
# print(f(4))
# print(g(5))

# def sum (x,y):           # кратко написала то же самое через лямбду: sum= lambda x,y: x+y
#     return x+y

# mult = lambda x,y: x*y
# print(type(mult))

# def calc (operation, x, y):        # функция calc может принять другую функцию в качестве аргуиента
#     print (operation (x, y))        # вывод результата обращения к этой функции

# calc(mult, 4, 5)       # вместо названия ф-цц в аргументах можно сразу написать: lambda x,y: x*y

# list = []
# for i in range(1,21):
#     if i%2 ==0:
#         list.append(i)
# print(list)                   # создала лист, все элементы к-го четные

# list = [i for i in range(1, 21) if i%2 ==0]
# print(list)                   # создала лист, все элементы к-го четные

# list = [(i,i) for i in range(1, 21) if i%2 ==0]
# print(list)                   # создала список кортежей, все элементы к-го четные

# def f(x):
#     return x**3

# list = [i for i in range(1, 21) if i%2 ==0]  # перебрали все числа от 1 до 20, проверили их на четность, 
#                                                 # возвели четные числа в 3 степень и сформировали из них список 
# print(list) 

# def select (func, coll):                  # ф-я, в аргументах которой другая функция и набор данных
#     return [func(x) for x in coll]        # формирует и возвращает лист, сделанный из элементов набора данных

# def where (func, coll):
#     return [x for x in coll if func(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)                  # первый арг: ф-я int, второй арг - строка data. на выходе получим список из целых чисел
# res = where(lambda x: not x%2, res)      # первый арг: ф-я через лямбду, оставляющая только четные числа, второй арг: предыд список
# res = select(lambda x: (x, x**2),res)    # первый арг: ф-я через лямбду, принимает х и возвращает х в квадрате, второй арг: предыд список
# print (res)


data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)                  
res = filter(lambda x: not x%2, res)      
res = list(map(lambda x: (x, x**2),res))    
print (res)