# ЗАДАНИЕ 20. РАБОТА С ФАЙЛАМИ (15 задач)

import os

def task1():
    print("\n=== ЗАДАНИЕ 1 ===")
    print("Найти произведение компонент файла с действительными числами")
    
    # Создаем тестовый файл
    with open('file1.txt', 'w') as f:
        f.write("2.5\n")
        f.write("3.0\n")
        f.write("1.5\n")
        f.write("4.0\n")
    
    print("Создан файл с числами: 2.5, 3.0, 1.5, 4.0")
    
    # Читаем файл и вычисляем произведение
    product = 1.0  # начальное значение для умножения
    
    with open('file1.txt', 'r') as f:
        for line in f:
            number = float(line.strip())  # читаем число
            product *= number  # умножаем
    
    print(f"Произведение всех чисел: {product}")
    
    # Удаляем временный файл
    os.remove('file1.txt')
    return product

def task2():
    print("\n=== ЗАДАНИЕ 2 ===")
    print("Разделить числа на положительные и отрицательные")
    
    # Создаем тестовый файл с равным числом положительных и отрицательных чисел
    with open('file2.txt', 'w') as f:
        f.write("5\n")
        f.write("-3\n")
        f.write("2\n")
        f.write("-8\n")
        f.write("7\n")
        f.write("-1\n")
    
    print("Создан файл с числами: 5, -3, 2, -8, 7, -1")
    
    # Читаем файл
    positive = []
    negative = []
    
    with open('file2.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            if number > 0:
                positive.append(number)
            else:
                negative.append(number)
    
    # Записываем в новый файл: сначала положительные, потом отрицательные
    with open('result2.txt', 'w') as f:
        # Записываем положительные
        for num in positive:
            f.write(f"{num}\n")
        # Записываем отрицательные
        for num in negative:
            f.write(f"{num}\n")
    
    print("Результат записан в файл 'result2.txt'")
    print(f"Положительные: {positive}")
    print(f"Отрицательные: {negative}")
    
    # Удаляем временные файлы
    os.remove('file2.txt')
    os.remove('result2.txt')
    return positive, negative

def task3():
    print("\n=== ЗАДАНИЕ 3 ===")
    print("Найти числа, которые являются точными квадратами")
    
    # Создаем тестовый файл
    with open('file3.txt', 'w') as f:
        f.write("4\n")
        f.write("9\n")
        f.write("15\n")
        f.write("16\n")
        f.write("25\n")
        f.write("30\n")
        f.write("36\n")
    
    print("Создан файл с числами: 4, 9, 15, 16, 25, 30, 36")
    
    squares = []  # список для точных квадратов
    
    with open('file3.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            # Проверяем, является ли число точным квадратом
            root = int(number ** 0.5)  # извлекаем корень
            if root * root == number:  # проверяем точный квадрат
                squares.append(number)
    
    # Записываем результат в новый файл
    with open('squares.txt', 'w') as f:
        for num in squares:
            f.write(f"{num}\n")
    
    print(f"Точные квадраты: {squares}")
    print("Результат записан в файл 'squares.txt'")
    
    # Удаляем временные файлы
    os.remove('file3.txt')
    os.remove('squares.txt')
    return squares

def task4():
    print("\n=== ЗАДАНИЕ 4 ===")
    print("Найти сумму наибольшего и наименьшего чисел")
    
    # Создаем тестовый файл
    with open('file4.txt', 'w') as f:
        f.write("3.5\n")
        f.write("1.2\n")
        f.write("7.8\n")
        f.write("2.1\n")
        f.write("5.4\n")
    
    print("Создан файл с числами: 3.5, 1.2, 7.8, 2.1, 5.4")
    
    # Читаем файл и находим min и max
    numbers = []
    
    with open('file4.txt', 'r') as f:
        for line in f:
            numbers.append(float(line.strip()))
    
    if numbers:  # если файл не пустой
        min_num = min(numbers)
        max_num = max(numbers)
        total = min_num + max_num
        
        print(f"Минимальное число: {min_num}")
        print(f"Максимальное число: {max_num}")
        print(f"Сумма min и max: {total}")
    else:
        print("Файл пустой!")
        total = None
    
    os.remove('file4.txt')
    return total

def task5():
    print("\n=== ЗАДАНИЕ 5 ===")
    print("Найти год с наименьшим номером в списке дат")
    
    # Создаем тестовый файл с датами
    with open('dates.txt', 'w') as f:
        f.write("15 3 2020\n")
        f.write("25 7 2015\n")
        f.write("10 1 2018\n")
        f.write("5 12 2010\n")
        f.write("20 6 2022\n")
    
    print("Создан файл с датами:")
    print("15.03.2020, 25.07.2015, 10.01.2018, 05.12.2010, 20.06.2022")
    
    years = []  # список для хранения годов
    
    with open('dates.txt', 'r') as f:
        for line in f:
            parts = line.strip().split()  # разделяем строку на части
            if len(parts) == 3:  # должно быть 3 числа: день, месяц, год
                day, month, year = parts
                years.append(int(year))  # добавляем год
    
    if years:
        min_year = min(years)
        print(f"Самый ранний год: {min_year}")
    else:
        print("Не удалось прочитать годы")
        min_year = None
    
    os.remove('dates.txt')
    return min_year

def task6():
    print("\n=== ЗАДАНИЕ 6 ===")
    print("Найти количество четных чисел в файле")
    
    # Создаем тестовый файл
    with open('file6.txt', 'w') as f:
        f.write("2\n")
        f.write("3\n")
        f.write("8\n")
        f.write("11\n")
        f.write("14\n")
        f.write("7\n")
        f.write("20\n")
    
    print("Создан файл с числами: 2, 3, 8, 11, 14, 7, 20")
    
    even_count = 0  # счетчик четных чисел
    
    with open('file6.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            if number % 2 == 0:  # проверяем четность
                even_count += 1
    
    print(f"Количество четных чисел: {even_count}")
    
    os.remove('file6.txt')
    return even_count

def task7():
    print("\n=== ЗАДАНИЕ 7 ===")
    print("Проверить, являются ли первые два символа цифрами")
    
    # Создаем тестовый файл
    with open('file7.txt', 'w') as f:
        f.write("25 apples\n")
        f.write("bananas\n")
        f.write("oranges\n")
    
    print("Создан файл с текстом: '25 apples', 'bananas', 'oranges'")
    
    # Читаем первые два символа файла
    with open('file7.txt', 'r') as f:
        first_char = f.read(1)  # читаем первый символ
        second_char = f.read(1)  # читаем второй символ
    
    print(f"Первый символ: '{first_char}'")
    print(f"Второй символ: '{second_char}'")
    
    # Проверяем, являются ли они цифрами
    if first_char.isdigit() and second_char.isdigit():
        print("Оба символа - цифры")
        # Создаем число из двух цифр
        number = int(first_char + second_char)
        print(f"Число: {number}")
        
        # Проверяем четность
        if number % 2 == 0:
            print("Число четное")
            result = "четное"
        else:
            print("Число нечетное")
            result = "нечетное"
    else:
        print("Не оба символа являются цифрами")
        result = "не цифры"
    
    os.remove('file7.txt')
    return result

def task8():
    print("\n=== ЗАДАНИЕ 8 ===")
    print("Получить все четные числа из файла")
    
    # Создаем тестовый файл
    with open('file8.txt', 'w') as f:
        f.write("12\n")
        f.write("5\n")
        f.write("18\n")
        f.write("7\n")
        f.write("24\n")
        f.write("9\n")
        f.write("30\n")
    
    print("Создан файл с числами: 12, 5, 18, 7, 24, 9, 30")
    
    even_numbers = []  # список для четных чисел
    
    with open('file8.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            if number % 2 == 0:  # проверяем четность
                even_numbers.append(number)
    
    # Записываем результат в новый файл
    with open('even_numbers.txt', 'w') as f:
        for num in even_numbers:
            f.write(f"{num}\n")
    
    print(f"Четные числа: {even_numbers}")
    print("Результат записан в файл 'even_numbers.txt'")
    
    os.remove('file8.txt')
    os.remove('even_numbers.txt')
    return even_numbers

def task9():
    print("\n=== ЗАДАНИЕ 9 ===")
    print("Найти наибольшее по модулю среди чисел с нечетными номерами")
    
    # Создаем тестовый файл
    with open('file9.txt', 'w') as f:
        f.write("3.2\n")   # позиция 1 (нечетная)
        f.write("-1.5\n")  # позиция 2 (четная)
        f.write("-7.8\n")  # позиция 3 (нечетная)
        f.write("2.1\n")   # позиция 4 (четная)
        f.write("5.6\n")   # позиция 5 (нечетная)
        f.write("-0.5\n")  # позиция 6 (четная)
    
    print("Создан файл с числами: 3.2, -1.5, -7.8, 2.1, 5.6, -0.5")
    
    numbers = []
    position = 1  # счетчик позиции (начинаем с 1)
    
    with open('file9.txt', 'r') as f:
        for line in f:
            number = float(line.strip())
            numbers.append((position, number, abs(number)))  # (позиция, число, модуль)
            position += 1
    
    # Находим числа с нечетными позициями
    odd_position_numbers = []
    for pos, num, mod in numbers:
        if pos % 2 == 1:  # нечетная позиция
            odd_position_numbers.append((pos, num, mod))
    
    # Находим наибольший модуль
    max_mod = 0
    max_num = None
    max_pos = None
    
    for pos, num, mod in odd_position_numbers:
        if mod > max_mod:
            max_mod = mod
            max_num = num
            max_pos = pos
    
    print(f"Числа с нечетными позициями: {odd_position_numbers}")
    print(f"Наибольший модуль у числа на позиции {max_pos}: {max_num} (модуль = {max_mod})")
    
    os.remove('file9.txt')
    return max_mod

def task10():
    print("\n=== ЗАДАНИЕ 10 ===")
    print("Найти все весенние даты")
    
    # Создаем тестовый файл с датами
    with open('dates2.txt', 'w') as f:
        f.write("15 1 2021\n")   # зима
        f.write("20 3 2021\n")   # весна (март)
        f.write("10 4 2021\n")   # весна (апрель)
        f.write("30 5 2021\n")   # весна (май)
        f.write("15 6 2021\n")   # лето
        f.write("25 12 2021\n")  # зима
    
    print("Создан файл с датами:")
    print("15.01.2021, 20.03.2021, 10.04.2021, 30.05.2021, 15.06.2021, 25.12.2021")
    
    spring_dates = []  # список для весенних дат
    
    with open('dates2.txt', 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                day, month, year = parts
                month = int(month)
                
                # Весенние месяцы: март (3), апрель (4), май (5)
                if 3 <= month <= 5:
                    spring_dates.append(f"{day}.{month}.{year}")
    
    print(f"Весенние даты: {spring_dates}")
    
    os.remove('dates2.txt')
    return spring_dates

def task11():
    print("\n=== ЗАДАНИЕ 11 ===")
    print("Найти числа, делящиеся на 3 и не делящиеся на 7")
    
    # Создаем тестовый файл
    with open('file11.txt', 'w') as f:
        f.write("3\n")
        f.write("6\n")
        f.write("9\n")
        f.write("14\n")
        f.write("21\n")
        f.write("24\n")
        f.write("28\n")
        f.write("30\n")
    
    print("Создан файл с числами: 3, 6, 9, 14, 21, 24, 28, 30")
    
    result_numbers = []  # список для подходящих чисел
    
    with open('file11.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            # Проверяем условия: делится на 3 И НЕ делится на 7
            if number % 3 == 0 and number % 7 != 0:
                result_numbers.append(number)
    
    # Записываем результат
    with open('result11.txt', 'w') as f:
        for num in result_numbers:
            f.write(f"{num}\n")
    
    print(f"Числа, делящиеся на 3 и не делящиеся на 7: {result_numbers}")
    print("Результат записан в файл 'result11.txt'")
    
    os.remove('file11.txt')
    os.remove('result11.txt')
    return result_numbers

def task12():
    print("\n=== ЗАДАНИЕ 12 ===")
    print("Найти наименьшее среди чисел с четными номерами")
    
    # Создаем тестовый файл
    with open('file12.txt', 'w') as f:
        f.write("10.5\n")   # позиция 1 (нечетная)
        f.write("3.2\n")    # позиция 2 (четная)
        f.write("7.8\n")    # позиция 3 (нечетная)
        f.write("1.5\n")    # позиция 4 (четная)
        f.write("9.1\n")    # позиция 5 (нечетная)
        f.write("2.7\n")    # позиция 6 (четная)
    
    print("Создан файл с числами: 10.5, 3.2, 7.8, 1.5, 9.1, 2.7")
    
    numbers = []
    position = 1
    
    with open('file12.txt', 'r') as f:
        for line in f:
            number = float(line.strip())
            numbers.append((position, number))
            position += 1
    
    # Находим числа с четными позициями
    even_position_numbers = []
    for pos, num in numbers:
        if pos % 2 == 0:  # четная позиция
            even_position_numbers.append(num)
    
    if even_position_numbers:
        min_num = min(even_position_numbers)
        print(f"Числа с четными позициями: {even_position_numbers}")
        print(f"Наименьшее из них: {min_num}")
    else:
        print("Нет чисел с четными позициями")
        min_num = None
    
    os.remove('file12.txt')
    return min_num

def task13():
    print("\n=== ЗАДАНИЕ 13 ===")
    print("Разделить числа на четные и нечетные")
    
    # Создаем тестовый файл
    with open('file13.txt', 'w') as f:
        f.write("2\n")
        f.write("5\n")
        f.write("8\n")
        f.write("3\n")
        f.write("10\n")
        f.write("7\n")
        f.write("4\n")
    
    print("Создан файл с числами: 2, 5, 8, 3, 10, 7, 4")
    
    even_numbers = []
    odd_numbers = []
    
    with open('file13.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
    
    # Записываем четные числа в файл g
    with open('file_g.txt', 'w') as f:
        for num in even_numbers:
            f.write(f"{num}\n")
    
    # Записываем нечетные числа в файл h
    with open('file_h.txt', 'w') as f:
        for num in odd_numbers:
            f.write(f"{num}\n")
    
    print(f"Четные числа: {even_numbers}")
    print(f"Нечетные числа: {odd_numbers}")
    print("Четные записаны в 'file_g.txt', нечетные в 'file_h.txt'")
    
    # Удаляем временные файлы
    os.remove('file13.txt')
    os.remove('file_g.txt')
    os.remove('file_h.txt')
    
    return even_numbers, odd_numbers

def task14():
    print("\n=== ЗАДАНИЕ 14 ===")
    print("Расположить числа без соседства одинаковых знаков")
    
    # Создаем тестовый файл с равным числом положительных и отрицательных чисел
    with open('file14.txt', 'w') as f:
        f.write("5\n")
        f.write("-2\n")
        f.write("8\n")
        f.write("-3\n")
        f.write("1\n")
        f.write("-6\n")
    
    print("Создан файл с числами: 5, -2, 8, -3, 1, -6")
    
    # Читаем числа
    positive = []
    negative = []
    
    with open('file14.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            if number > 0:
                positive.append(number)
            else:
                negative.append(number)
    
    # Чередуем положительные и отрицательные
    result = []
    for i in range(len(positive)):
        result.append(positive[i])
        result.append(negative[i])
    
    # Проверяем, что нет двух подряд чисел с одинаковым знаком
    ok = True
    for i in range(len(result) - 1):
        if (result[i] > 0 and result[i+1] > 0) or (result[i] < 0 and result[i+1] < 0):
            ok = False
            break
    
    # Записываем результат
    with open('result14.txt', 'w') as f:
        for num in result:
            f.write(f"{num}\n")
    
    print(f"Результат: {result}")
    print("Нет двух соседних чисел с одинаковым знаком?" + (" Да" if ok else " Нет"))
    print("Результат записан в 'result14.txt'")
    
    os.remove('file14.txt')
    os.remove('result14.txt')
    return result

def task15():
    print("\n=== ЗАДАНИЕ 15 ===")
    print("Расположить числа в порядке: два положительных, два отрицательных")
    
    # Создаем тестовый файл (должно делиться на 4)
    with open('file15.txt', 'w') as f:
        f.write("1\n")
        f.write("2\n")
        f.write("-3\n")
        f.write("-4\n")
        f.write("5\n")
        f.write("6\n")
        f.write("-7\n")
        f.write("-8\n")
    
    print("Создан файл с числами: 1, 2, -3, -4, 5, 6, -7, -8")
    
    # Читаем числа
    positive = []
    negative = []
    
    with open('file15.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            if number > 0:
                positive.append(number)
            else:
                negative.append(number)
    
    # Создаем результат: два положительных, два отрицательных
    result = []
    for i in range(0, len(positive), 2):
        if i+1 < len(positive):
            result.append(positive[i])
            result.append(positive[i+1])
        if i//2*2 < len(negative):
            result.append(negative[i])
            result.append(negative[i+1])
    
    # Записываем результат
    with open('result15.txt', 'w') as f:
        for num in result:
            f.write(f"{num}\n")
    
    print(f"Результат (два положительных, два отрицательных): {result}")
    print("Результат записан в 'result15.txt'")
    
    os.remove('file15.txt')
    os.remove('result15.txt')
    return result

# Главная программа
def main():
    print("ВЫБЕРИТЕ ЗАДАНИЕ (1-15):")
    print("1. Произведение чисел из файла")
    print("2. Разделить положительные и отрицательные")
    print("3. Найти точные квадраты")
    print("4. Сумма min и max")
    print("5. Найти самый ранний год")
    print("6. Количество четных чисел")
    print("7. Проверить первые два символа")
    print("8. Получить все четные числа")
    print("9. Наибольший модуль с нечетных позиций")
    print("10. Найти весенние даты")
    print("11. Числа делящиеся на 3, но не на 7")
    print("12. Наименьшее число с четных позиций")
    print("13. Разделить на четные и нечетные")
    print("14. Чередовать знаки чисел")
    print("15. Два положительных, два отрицательных")
    
    choice = input("\nВведите номер задания (1-15): ")
    
    tasks = {
        '1': task1, '2': task2, '3': task3, '4': task4, '5': task5,
        '6': task6, '7': task7, '8': task8, '9': task9, '10': task10,
        '11': task11, '12': task12, '13': task13, '14': task14, '15': task15
    }
    
    if choice in tasks:
        result = tasks[choice]()
        print(f"\nЗадание {choice} выполнено!")
        return result
    else:
        print("Неверный выбор! Введите число от 1 до 15.")
        return None

if __name__ == "__main__":
    main()