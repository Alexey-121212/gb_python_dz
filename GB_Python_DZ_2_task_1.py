# Задача 1. Нахождение наибольшего общего делителя (НОД) двух
# чисел
# Программа принимает два целых числа и находит их наибольший общий
# делитель (НОД).

# Запрашиваем у пользователя ввод первого числа
a = int(input("Введите первое число: "))
# Запрашиваем у пользователя ввод второго числа
b = int(input("Введите второе число: "))

# Используем цикл while для реализации алгоритма Евклида
while b: # Пока значение b не равно нулю
    temp = b
    b = a % temp
    a = temp

#    a, b = b, a % b # Присваиваем a значение b, а b значение
#остатка от деления a на b

# Выводим результат - наибольший общий делитель
print("НОД:", a)
