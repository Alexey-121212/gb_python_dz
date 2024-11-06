# Задача 3. Проверка палиндрома
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).

# Принимаем строку от пользователя и приводим её к нижнему регистру
# для унификации
string = input("Введите строку: ").lower()
# Создаем множество для символов с нечетным количеством вхождений
odd_chars = set()
# Проходим по каждому символу в строке
for char in string:
# Если символ уже есть в множестве, убираем его
    if char in odd_chars:
        odd_chars.remove(char)
# Если символа нет в множестве, добавляем его
    else:
        odd_chars.add(char)
# Если количество символов с нечетным количеством вхождений <= 1,
# строка является палиндромом
if len(odd_chars) <= 1:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")