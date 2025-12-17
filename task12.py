# ЗАДАНИЕ 12. КОРТЕЖИ (15 задач)

def task12_1():
    print("\n=== ЗАДАНИЕ 12.1 ===")
    # a) создает кортеж из строк, введенных пользователем
    print("Введите строки через запятую:")
    text = input()
    words = [word.strip() for word in text.split(',')]
    my_tuple = tuple(words)
    print("Кортеж:", my_tuple)
    
    # b) преобразует в словарь {строка: длина_строки}
    result_dict = {word: len(word) for word in my_tuple}
    print("Словарь:", result_dict)
    return my_tuple, result_dict

def task12_2():
    print("\n=== ЗАДАНИЕ 12.2 ===")
    # Разные типы данных -> сортировка по типам
    mixed_tuple = ("hello", 123, 45.6, [1, 2], {"a": 1}, (7, 8))
    print("Смешанный кортеж:", mixed_tuple)
    
    tuple_list = [("text", 1), (2.5, "word"), ([1], 3)]
    
    strings = []
    numbers = []
    lists = []
    dicts = []
    tuples = []
    
    for tup in tuple_list:
        for item in tup:
            if type(item) == str:
                strings.append(item)
            elif type(item) == int or type(item) == float:
                numbers.append(item)
            elif type(item) == list:
                lists.append(item)
            elif type(item) == dict:
                dicts.append(item)
            elif type(item) == tuple:
                tuples.append(item)
    
    print("Строки:", strings)
    print("Числа:", numbers)
    print("Списки:", lists)
    return mixed_tuple, strings

def task12_3():
    print("\n=== ЗАДАНИЕ 12.3 ===")
    # Кортеж чисел -> перевернуть и удалить кратные 3
    text = input("Введите числа через пробел: ")
    numbers = [int(x) for x in text.split()]
    my_tuple = tuple(numbers)
    
    print("Кортеж:", my_tuple)
    print("Первый элемент:", my_tuple[0])
    
    reversed_list = list(my_tuple)
    reversed_list.reverse()
    
    filtered = []
    for num in reversed_list:
        if num % 3 != 0:
            filtered.append(num)
    
    result = tuple(filtered)
    print("Результат:", result)
    return my_tuple, result

def task12_4():
    print("\n=== ЗАДАНИЕ 12.4 ===")
    # Распаковка кортежа -> словарь
    person = ("Иван", 25, "Москва", "инженер")
    name, age, city, job = person
    
    print(f"Имя: {name}, Возраст: {age}, Город: {city}, Работа: {job}")
    
    pairs = [("яблоко", 50), ("банан", 30), ("апельсин", 40)]
    my_dict = dict(pairs)
    
    sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
    sorted_dict = dict(sorted_items)
    
    print("Отсортированный словарь:", sorted_dict)
    return person, sorted_dict

def task12_5():
    print("\n=== ЗАДАНИЕ 12.5 ===")
    # Добавить элемент -> обратные строки
    old_tuple = (1, 2, 3, 4)
    print("Исходный кортеж:", old_tuple)
    
    new_element = input("Введите новый элемент: ")
    new_tuple = old_tuple + (new_element,)
    print("Новый кортеж:", new_tuple)
    
    reversed_strings = []
    for item in new_tuple:
        reversed_str = str(item)[::-1]
        reversed_strings.append(reversed_str)
    
    result = tuple(reversed_strings)
    print("С обратными строками:", result)
    return new_tuple, result

def task12_6():
    print("\n=== ЗАДАНИЕ 12.6 ===")
    # Кортеж в строку -> замена последнего элемента
    my_tuple = ("яблоко", "банан", "апельсин")
    separator = input("Введите разделитель: ")
    result_string = separator.join(my_tuple)
    print("Строка:", result_string)
    
    tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, "текст")]
    new_value = input("Введите новое значение: ")
    
    new_list = []
    for tup in tuple_list:
        temp_list = list(tup)
        if isinstance(temp_list[-1], (int, float)):
            temp_list[-1] = new_value
        new_list.append(tuple(temp_list))
    
    print("Обновленные кортежи:", new_list)
    return result_string, new_list

def task12_7():
    print("\n=== ЗАДАНИЕ 12.7 ===")
    # Четвертый элемент -> замена пустых кортежей
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
    
    if len(my_tuple) >= 4:
        print("4-й с начала:", my_tuple[3])
        print("4-й с конца:", my_tuple[-4])
    
    tuple_list = [(1, 2), (), (3, 4), (), (5, 6)]
    print("Исходный список:", tuple_list)
    
    import random
    new_list = []
    for tup in tuple_list:
        if len(tup) == 0:
            new_list.append((random.randint(1, 10), random.randint(1, 10)))
        else:
            new_list.append(tup)
    
    print("После замены:", new_list)
    return my_tuple, new_list

def task12_8():
    print("\n=== ЗАДАНИЕ 12.8 ===")
    # Кортеж словарей -> сортировка по float
    dict1 = {"name": "Анна", "score": 85.5}
    dict2 = {"name": "Борис", "score": 92.3}
    dict3 = {"name": "Виктор", "score": 78.9}
    
    dict_tuple = (dict1, dict2, dict3)
    print("Кортеж словарей:", dict_tuple)
    
    sorted_list = sorted(dict_tuple, key=lambda x: x["score"], reverse=True)
    sorted_tuple = tuple(sorted_list)
    
    print("После сортировки:", sorted_tuple)
    return dict_tuple, sorted_tuple

def task12_9():
    print("\n=== ЗАДАНИЕ 12.9 ===")
    # Повторяющиеся элементы -> подсчет до кортежа
    my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 3)
    
    duplicates = []
    for i in range(len(my_tuple)):
        for j in range(i + 1, len(my_tuple)):
            if my_tuple[i] == my_tuple[j] and my_tuple[i] not in duplicates:
                duplicates.append(my_tuple[i])
    
    print("Повторяющиеся элементы:", duplicates)
    
    mixed_list = [1, 2, "hello", 3.14, (4, 5), 6, 7]
    count = 0
    total = 0
    
    for item in mixed_list:
        if type(item) == tuple:
            break
        count += 1
        if isinstance(item, (int, float)):
            total += item
    
    print(f"Элементов до кортежа: {count}, Сумма: {total}")
    return duplicates, total

def task12_10():
    print("\n=== ЗАДАНИЕ 12.10 ===")
    # Поиск элемента -> удаление повторов
    my_tuple = (1, 2, 3, 4, 2, 5, 2, 6)
    
    element = input("Введите элемент для поиска: ")
    try:
        element = int(element)
    except:
        pass
    
    count = my_tuple.count(element)
    print(f"Элемент '{element}' встречается {count} раз")
    
    text = input("Введите строки через запятую: ")
    strings = [s.strip() for s in text.split(',')]
    unique_strings = []
    
    for s in strings:
        if s not in unique_strings:
            unique_strings.append(s)
    
    result = tuple(unique_strings)
    print("Без повторов:", result)
    return count, result

def task12_11():
    print("\n=== ЗАДАНИЕ 12.11 ===")
    # a) преобразует список в кортеж
    print("Введите элементы через пробел:")
    text = input()
    my_list = text.split()
    my_tuple = tuple(my_list)
    print("Кортеж:", my_tuple)
    
    # b) перемножает четные числа из кортежа
    product = 1
    has_even = False
    
    for item in my_tuple:
        if item.isdigit():  # проверяем, что это число
            num = int(item)
            if num % 2 == 0:
                product *= num
                has_even = True
    
    if has_even:
        print("Произведение четных:", product)
    else:
        print("Четных чисел нет")
    return my_tuple, product

def task12_12():
    print("\n=== ЗАДАНИЕ 12.12 ===")
    # Удаление элемента -> среднее в кортежах
    my_tuple = (10, 20, 30, 40, 50)
    print("Исходный кортеж:", my_tuple)
    
    element = input("Введите элемент для удаления: ")
    try:
        element = int(element)
    except:
        pass
    
    new_list = [x for x in my_tuple if x != element]
    new_tuple = tuple(new_list)
    print("После удаления:", new_tuple)
    
    tuple_of_tuples = ((1, 6, 7), (2, 8, 3), (9, 4, 10))
    averages = []
    
    for tup in tuple_of_tuples:
        nums = [x for x in tup if isinstance(x, (int, float)) and x > 5]
        if nums:
            averages.append(sum(nums) / len(nums))
        else:
            averages.append(0)
    
    print("Средние значения:", averages)
    return new_tuple, averages

def task12_13():
    print("\n=== ЗАДАНИЕ 12.13 ===")
    # Срез кортежа -> строки в числа
    my_tuple = (1, "hello", 2, "world", 3, 4, "test")
    print("Исходный кортеж:", my_tuple)
    
    start = int(input("Начало среза: "))
    end = int(input("Конец среза: "))
    
    slice_part = my_tuple[start:end]
    numbers_only = [x for x in slice_part if not isinstance(x, str)]
    print("Срез без строк:", numbers_only)
    
    str_tuple = ("12", "-5", "8", "-3", "15")
    numbers = []
    
    for s in str_tuple:
        num = int(s)
        if num >= 0:
            numbers.append(num)
    
    result = tuple(numbers)
    print("Без отрицательных:", result)
    return numbers_only, result

def task12_14():
    print("\n=== ЗАДАНИЕ 12.14 ===")
    # a) поиск порядкового номера элемента (только числа)
    print("Введите элементы кортежа через пробел:")
    data = input().split()
    my_tuple = tuple(data)
    
    print("Введите элемент для поиска:")
    element = input()
    
    found_index = -1
    for i, item in enumerate(my_tuple):
        if item.isdigit() and item == element:
            found_index = i
            break
    
    if found_index != -1:
        print(f"Найден на позиции {found_index + 1}")
    else:
        print("Не найден")
    
    # b) преобразование в одно число (только кратные 3)
    numbers = []
    for item in my_tuple:
        if item.isdigit():
            num = int(item)
            if num % 3 == 0:
                numbers.append(num)
    
    if numbers:
        big_num_str = ''.join(str(x) for x in numbers)
        result = int(big_num_str)
        print("Объединенное число:", result)
    else:
        print("Нет чисел кратных 3")
        result = 0
    return found_index, result

def task12_15():
    print("\n=== ЗАДАНИЕ 12.15 ===")
    # a) длина кортежа (количество строковых элементов)
    print("Введите элементы кортежа через пробел:")
    data = input().split()
    my_tuple = tuple(data)
    
    string_elements = [x for x in my_tuple if not x.isdigit()]
    string_count = len(string_elements)
    print(f"Количество строковых элементов: {string_count}")
    
    # b) поиск в кортеже кортежей
    print("Введите элементы для вложенных кортежей через пробел:")
    nested_data = input().split()
    print("Введите количество элементов в каждом кортеже:")
    chunk_size = int(input())
    
    tuple_of_tuples = []
    for i in range(0, len(nested_data), chunk_size):
        chunk = tuple(nested_data[i:i + chunk_size])
        tuple_of_tuples.append(chunk)
    
    tuple_of_tuples = tuple(tuple_of_tuples)
    print("Кортеж кортежей:", tuple_of_tuples)
    
    print("Введите элемент для поиска:")
    element = input()
    
    count = 0
    for tup in tuple_of_tuples:
        count += tup.count(element)
    
    print(f"Элемент встречается {count} раз")
    return string_count, count

# Главная программа
def main():
    print("Выберите задание (12.1-12.15):")
    choice = input()
    
    if choice == '12.1':
        result = task12_1()
    elif choice == '12.2':
        result = task12_2()
    elif choice == '12.3':
        result = task12_3()
    elif choice == '12.4':
        result = task12_4()
    elif choice == '12.5':
        result = task12_5()
    elif choice == '12.6':
        result = task12_6()
    elif choice == '12.7':
        result = task12_7()
    elif choice == '12.8':
        result = task12_8()
    elif choice == '12.9':
        result = task12_9()
    elif choice == '12.10':
        result = task12_10()
    elif choice == '12.11':
        result = task12_11()
    elif choice == '12.12':
        result = task12_12()
    elif choice == '12.13':
        result = task12_13()
    elif choice == '12.14':
        result = task12_14()
    elif choice == '12.15':
        result = task12_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()