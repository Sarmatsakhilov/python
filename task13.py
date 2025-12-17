
# ЗАДАНИЕ 13. МНОЖЕСТВА (15 задач)

def task13_1():
    print("\n=== ЗАДАНИЕ 13.1 ===")
    # а) Создать множества символов
    print("Введите последовательность символов:")
    sequence = input()
    
    digits = set()
    operators = set()
    letters_AF = set()
    letters_XYZ = set()
    
    for char in sequence:
        if char.isdigit():
            digits.add(char)
        elif char in '+-*/':
            operators.add(char)
        elif char.upper() in 'ABCDEF':
            letters_AF.add(char)
        elif char.upper() in 'XYZ':
            letters_XYZ.add(char)
    
    print("Цифры:", digits)
    print("Операторы:", operators)
    print("Буквы A-F:", letters_AF)
    print("Буквы X-Z:", letters_XYZ)
    
    # б) Отсутствующие товары
    print("Введите коды доступных товаров через пробел (1-20):")
    available_input = input().split()
    available = set(int(x) for x in available_input)
    
    all_products = set(range(1, 21))
    missing = all_products - available
    
    print("Отсутствующие товары:", missing)
    return digits, missing

def task13_2():
    print("\n=== ЗАДАНИЕ 13.2 ===")
    # а) Подсчет цифр и операторов
    print("Введите текст:")
    text = input()
    
    digit_count = sum(1 for char in text if char.isdigit())
    operator_count = sum(1 for char in text if char in '+-*/')
    
    print(f"Цифр: {digit_count}, Операторов: {operator_count}")
    
    # б) Общие элементы двух списков
    print("Введите первый список чисел через пробел:")
    list1 = [int(x) for x in input().split()]
    
    print("Введите второй список чисел через пробел:")
    list2 = [int(x) for x in input().split()]
    
    common = set(list1) & set(list2)
    print("Общие элементы:", common)
    return digit_count, common

def task13_3():
    print("\n=== ЗАДАНИЕ 13.3 ===")
    # а) Латинские буквы и знаки препинания
    print("Введите текст на английском:")
    text = input()
    
    lowercase = set(char for char in text if char.islower() and char.isalpha())
    punctuation_count = sum(1 for char in text if char in '.,!?;:')
    
    print("Строчные латинские буквы:", lowercase)
    print("Знаков препинания:", punctuation_count)
    
    # б) Проверка подмножества
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    is_subset = A.issubset(B)
    print(f"A является подмножеством B: {is_subset}")
    return lowercase, is_subset

def task13_4():
    print("\n=== ЗАДАНИЕ 13.4 ===")
    # а) Общие буквы трех предложений
    print("Введите первое предложение:")
    s1 = input()
    print("Введите второе предложение:")
    s2 = input()
    print("Введите третье предложение:")
    s3 = input()
    
    letters1 = set(char.lower() for char in s1 if char.isalpha())
    letters2 = set(char.lower() for char in s2 if char.isalpha())
    letters3 = set(char.lower() for char in s3 if char.isalpha())
    
    common = letters1 & letters2 & letters3
    print("Общие буквы:", common)
    
    # б) Предметы только одного университета
    print("Введите предметы первого университета через запятую:")
    uni1 = set(x.strip() for x in input().split(','))
    
    print("Введите предметы второго университета через запятую:")
    uni2 = set(x.strip() for x in input().split(','))
    
    only_uni1 = uni1 - uni2
    only_uni2 = uni2 - uni1
    
    print("Только в первом университете:", only_uni1)
    print("Только во втором университете:", only_uni2)
    return common, only_uni1

def task13_5():
    print("\n=== ЗАДАНИЕ 13.5 ===")
    # а) Наибольшая цифра трех чисел
    print("Введите первое число:")
    num1 = int(input())
    print("Введите второе число:")
    num2 = int(input())
    print("Введите третье число:")
    num3 = int(input())
    
    all_digits = set()
    for num in [num1, num2, num3]:
        all_digits.update(str(num))
    
    max_digit = max(int(d) for d in all_digits)
    print("Наибольшая цифра:", max_digit)
    
    # б) Элементы только в одном множестве
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    only_A = A - B
    only_B = B - A
    unique = only_A | only_B
    
    print("Элементы только в одном множестве:", unique)
    return max_digit, unique

def task13_6():
    print("\n=== ЗАДАНИЕ 13.6 ===")
    # а) Уникальные цифры в строке
    print("Введите строку с цифрами:")
    text = input()
    
    unique_digits = set(char for char in text if char.isdigit())
    print(f"Количество уникальных цифр: {len(unique_digits)}")
    print("Уникальные цифры:", sorted(unique_digits))
    
    # б) Товары одного пользователя
    purchases = [
        {"user": 1, "products": ["laptop", "mouse"]},
        {"user": 2, "products": ["monitor", "mouse"]},
        {"user": 3, "products": ["laptop", "headphones"]}
    ]
    
    product_users = {}
    for purchase in purchases:
        for product in purchase["products"]:
            if product not in product_users:
                product_users[product] = set()
            product_users[product].add(purchase["user"])
    
    unique_products = [p for p, users in product_users.items() if len(users) == 1]
    print("Товары одного пользователя:", unique_products)
    return unique_digits, unique_products

def task13_7():
    print("\n=== ЗАДАНИЕ 13.7 ===")
    # а) Уникальные буквы для трех предложений
    print("Введите первое предложение:")
    s1 = input()
    print("Введите второе предложение:")
    s2 = input()
    print("Введите третье предложение:")
    s3 = input()
    
    def get_letters(text):
        return set(char.lower() for char in text if char.isalpha())
    
    l1, l2, l3 = get_letters(s1), get_letters(s2), get_letters(s3)
    
    unique1 = l1 - l2 - l3
    unique2 = l2 - l1 - l3
    unique3 = l3 - l1 - l2
    
    print("Уникальные для первого:", unique1)
    print("Уникальные для второго:", unique2)
    print("Уникальные для третьего:", unique3)
    
    # б) Непересекающиеся множества
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    are_disjoint = A.isdisjoint(B)
    print(f"Множества непересекаются: {are_disjoint}")
    return unique1, are_disjoint

def task13_8():
    print("\n=== ЗАДАНИЕ 13.8 ===")
    # а) Составление строки из символов
    print("Введите первую строку:")
    str1 = input()
    print("Введите вторую строку:")
    str2 = input()
    print("Введите целевую строку:")
    target = input()
    
    available = set(str1 + str2)
    can_form = set(target).issubset(available)
    
    print(f"Можно составить '{target}': {can_form}")
    
    # б) Уникальные навыки сотрудников
    employees = [
        {"id": 1, "skills": ["Python", "SQL"]},
        {"id": 2, "skills": ["Python", "JavaScript"]},
        {"id": 3, "skills": ["Java", "SQL"]}
    ]
    
    skill_count = {}
    for emp in employees:
        for skill in emp["skills"]:
            skill_count[skill] = skill_count.get(skill, 0) + 1
    
    unique_skills = [s for s, count in skill_count.items() if count == 1]
    print("Навыки только у одного сотрудника:", unique_skills)
    return can_form, unique_skills

def task13_9():
    print("\n=== ЗАДАНИЕ 13.9 ===")
    # а) Русские гласные буквы
    print("Введите текст на русском:")
    text = input().lower()
    
    vowels = "аеёиоуыэюя"
    found_vowels = set(char for char in text if char in vowels)
    sorted_vowels = sorted(found_vowels)
    
    print("Уникальные русские гласные:", sorted_vowels)
    
    # б) Категории с одним продуктом
    products = [
        {"id": 1, "categories": ["электроника", "телефоны"]},
        {"id": 2, "categories": ["электроника", "компьютеры"]},
        {"id": 3, "categories": ["книги"]}
    ]
    
    category_count = {}
    for product in products:
        for category in product["categories"]:
            category_count[category] = category_count.get(category, 0) + 1
    
    single_categories = [c for c, count in category_count.items() if count == 1]
    print("Категории с одним продуктом:", single_categories)
    return sorted_vowels, single_categories

def task13_10():
    print("\n=== ЗАДАНИЕ 13.10 ===")
    # а) Уникальные цифры числа
    print("Введите число:")
    number = input()
    
    unique_digits = set(char for char in number if char.isdigit())
    sorted_digits = sorted(int(d) for d in unique_digits)
    print("Уникальные цифры:", sorted_digits)
    
    # б) Строгое подмножество
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    is_strict_subset = A.issubset(B) and A != B
    print(f"A строгое подмножество B: {is_strict_subset}")
    return sorted_digits, is_strict_subset

def task13_11():
    print("\n=== ЗАДАНИЕ 13.11 ===")
    # а) Гласные vs согласные
    print("Введите текст на русском:")
    text = input().lower()
    
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    print(f"Гласных: {vowel_count}, Согласных: {consonant_count}")
    
    if vowel_count > consonant_count:
        print("Гласных больше")
    elif consonant_count > vowel_count:
        print("Согласных больше")
    else:
        print("Поровну")
    
    # б) Товары только в определенный день
    orders = [
        {"day": "2024-01-01", "products": ["laptop", "mouse"]},
        {"day": "2024-01-01", "products": ["keyboard", "mouse"]},
        {"day": "2024-01-02", "products": ["laptop", "monitor"]}
    ]
    
    print("Введите день (например: 2024-01-01):")
    target_day = input()
    
    day_products = set()
    other_products = set()
    
    for order in orders:
        if order["day"] == target_day:
            day_products.update(order["products"])
        else:
            other_products.update(order["products"])
    
    only_target = day_products - other_products
    print(f"Товары только за {target_day}: {only_target}")
    return vowel_count, only_target

def task13_12():
    print("\n=== ЗАДАНИЕ 13.12 ===")
    # а) Отсутствующие цифры в числе
    print("Введите натуральное число:")
    number = input()
    
    all_digits = set("0123456789")
    number_digits = set(number)
    missing = sorted(all_digits - number_digits)
    
    print("Отсутствующие цифры:", missing)
    
    # б) Надмножество
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    is_superset = A.issuperset(B)
    print(f"A надмножество B: {is_superset}")
    return missing, is_superset

def task13_13():
    print("\n=== ЗАДАНИЕ 13.13 ===")
    # а) Удаление пересечения
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    result = A - B
    print(f"A после удаления пересечения с B: {result}")
    
    # б) Товары купленные хотя бы одним
    purchases = [
        {"user": 1, "products": ["laptop", "mouse"]},
        {"user": 2, "products": ["monitor", "keyboard"]},
        {"user": 3, "products": ["laptop", "headphones"]}
    ]
    
    all_products = set()
    for purchase in purchases:
        all_products.update(purchase["products"])
    
    print("Все купленные товары:", all_products)
    return result, all_products

def task13_14():
    print("\n=== ЗАДАНИЕ 13.14 ===")
    # а) Отсутствующие согласные
    print("Введите текст на русском:")
    text = input().lower()
    
    all_consonants = set("бвгджзйклмнпрстфхцчшщ")
    text_consonants = set(char for char in text if char in all_consonants)
    missing = sorted(all_consonants - text_consonants)
    
    print("Отсутствующие согласные:", missing)
    
    # б) Равные множества
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    are_equal = A == B
    print(f"Множества равны: {are_equal}")
    return missing, are_equal

def task13_15():
    print("\n=== ЗАДАНИЕ 13.15 ===")
    # а) Общие элементы
    print("Введите элементы множества A через пробел:")
    A = set(input().split())
    
    print("Введите элементы множества B через пробел:")
    B = set(input().split())
    
    has_common = not A.isdisjoint(B)
    common_elements = A & B
    
    print(f"Есть общие элементы: {has_common}")
    print("Общие элементы:", common_elements)
    
    # б) Общие предметы университетов
    print("Введите предметы первого университета через запятую:")
    uni1 = set(x.strip() for x in input().split(','))
    
    print("Введите предметы второго университета через запятую:")
    uni2 = set(x.strip() for x in input().split(','))
    
    common_subjects = uni1 & uni2
    print("Предметы изучаемые в обоих университетах:", common_subjects)
    return has_common, common_subjects

# Главная программа
def main():
    print("Выберите задание (13.1-13.15):")
    choice = input()
    
    if choice == '13.1':
        result = task13_1()
    elif choice == '13.2':
        result = task13_2()
    elif choice == '13.3':
        result = task13_3()
    elif choice == '13.4':
        result = task13_4()
    elif choice == '13.5':
        result = task13_5()
    elif choice == '13.6':
        result = task13_6()
    elif choice == '13.7':
        result = task13_7()
    elif choice == '13.8':
        result = task13_8()
    elif choice == '13.9':
        result = task13_9()
    elif choice == '13.10':
        result = task13_10()
    elif choice == '13.11':
        result = task13_11()
    elif choice == '13.12':
        result = task13_12()
    elif choice == '13.13':
        result = task13_13()
    elif choice == '13.14':
        result = task13_14()
    elif choice == '13.15':
        result = task13_15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()