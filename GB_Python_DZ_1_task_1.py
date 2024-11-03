# Задание 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.

# Пользователь вводит размеры рамки
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
# Внешний цикл отвечает за строки (высота)
for line in range(height + 1):
# Внутренний цикл отвечает за столбцы (ширина)
  for col in range(width + 1):
# Если текущий столбец - первый или последний, рисуем
# вертикальную границу
    if col == width or col == 0:
      print('|', end='')
# Если текущая строка - первая или последняя, рисуем
# горизонтальную границу
    elif line == height or line == 0:
      print('-', end='')
# В остальных случаях оставляем пробелы
    else:
      print(' ', end='')
# Завершаем текущую строку и переходим к следующей
  print()

# 1







