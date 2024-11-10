#
# Задача 4. Функция максимума
# Юра пишет различные полезные функции для Python, чтобы остальным
# программистам стало проще работать. Он захотел написать функцию, которая
# будет находить максимум из перечисленных чисел. Функция для нахождения
# максимума из двух чисел у него уже есть. Юра задумался: может быть, её
# можно как-то использовать для нахождения максимума уже от трёх чисел?
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# 1. maximum_of_two — функция принимает два числа и возвращает одно
# (наибольшее из двух);
# 2. maximum_of_three — функция принимает три числа и возвращает одно
# (наибольшее из трёх); при этом она должна использовать для сравнений
# первую функцию maximum_of_two.

def max_of_2(number_1, number_2):
# Подсказка №2
# Возвращает большее из двух чисел
    if number_1 > number_2:
        return number_1
    return number_2

def max_of_3(number_1, number_2, number_3):
# Подсказка №3 и №4
# Использует max_of_2 для нахождения максимума из трёх чисел
# Сначала находит максимум из первых двух чисел
# Затем находит максимум между результатом и третьим числом
    return max_of_2(max_of_2(number_1, number_2), number_3)
# Подсказка №5
# Ввод трёх чисел от пользователя
digit_1 = int(input('Введите первое число: '))
digit_2 = int(input('Введите второе число: '))
digit_3 = int(input('Введите третье число: '))
# Вывод самого большого числа
print('Самое большое число:', max_of_3(digit_1, digit_2, digit_3))