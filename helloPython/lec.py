
#something = None
#print (type(something))

#a= 123
#b = 1.23
#print(type(a))
#print(type(b))

#something = 56123
#print (type(something))

#s = 'qwerty'
#print (type(s)) # вывод строки

#print (a,'-',b, '-', s) # форматирование 1 для вывода нескольких переменных сразу с дефисами между ними
#print ('{1} - {0} - {2}'.format(a,b,s)) # форматирование 2, которое позволяет менять местами переменные
#print (f'{a} - {b} - {s}') # форматирование 3 - интерполяция

#f = False
#print(f)

#list = ['1','2','5', 'hello', 6, 7, 9, 4.5] # можно миксовать разные типы данных в списке, но лучше не надо

#print(list)

#print ('enter g')
#g = int(input()) # если хочешь получить при вводе целое число
#print ('enter t')
#t= float(input())  # если хочешь получить при вводе вещественное число

#print (g, '+', t, '=', g+t)

#d = 6
#h = 8
#l = d+h
#print(l)

#a = [1,2,3,4]
#print(a)
#print (2 in a)  #показывает, является ли истиной то, что число 2 присутствует в листе а

#is_odd = a[3] % 2 == 0 #показывает, является ли истиной то, что третий элемент листа четный
#print(is_odd)

#a = int(input())
#b = int(input())
#if a > b:
    #print(a)           #отступы важны
#else:
    #print(b)

list = [1,2,5,4]
for i in list:
    print(i**2)         # показал результат возведения в степень счетчика внутри листа

# r = range(2,10)           # сформировали список от 2 до 9
# for i in r:
#     print(i)            # показал итератор внутри списка