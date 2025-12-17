# ЗАДАНИЕ 14. ФУНКЦИИ (15 задач)

def task1():
    print("\n=== ЗАДАНИЕ 1 ===")
    def Mean(X, Y):
        if X <= 0 or Y <= 0:
            print("Ошибка: числа должны быть положительными!")
            return 0, 0
        
        AMean = (X + Y) / 2
        GMean = (X * Y) ** 0.5
        return AMean, GMean
    
    print("Введите два положительных числа:")
    x = float(input("X = "))
    y = float(input("Y = "))
    
    amean, gmean = Mean(x, y)
    print(f"Среднее арифметическое: {amean}")
    print(f"Среднее геометрическое: {gmean}")
    return amean, gmean

def task2():
    print("\n=== ЗАДАНИЕ 2 ===")
    def Circle(R):
        import math
        area = math.pi * R * R
        length = 2 * math.pi * R
        return area, length
    
    print("Введите радиус окружности:")
    r = float(input("R = "))
    
    area, length = Circle(r)
    print(f"Площадь круга: {area:.2f}")
    print(f"Длина окружности: {length:.2f}")
    return area, length

def task3():
    print("\n=== ЗАДАНИЕ 3 ===")
    def TrianglePS(a):
        P = 3 * a
        S = (3 ** 0.5 / 4) * a * a
        return P, S
    
    print("Введите сторону равностороннего треугольника:")
    a = float(input("a = "))
    
    perimeter, area = TrianglePS(a)
    print(f"Периметр: {perimeter}")
    print(f"Площадь: {area:.2f}")
    return perimeter, area

def task4():
    print("\n=== ЗАДАНИЕ 4 ===")
    def RingS(R1, R2):
        import math
        if R1 <= R2:
            area = math.pi * (R2 * R2 - R1 * R1)
        else:
            area = math.pi * (R1 * R1 - R2 * R2)
        return area
    
    print("Введите радиусы двух окружностей:")
    r1 = float(input("R1 = "))
    r2 = float(input("R2 = "))
    
    area = RingS(r1, r2)
    print(f"Площадь кольца: {area:.2f}")
    return area

def task5():
    print("\n=== ЗАДАНИЕ 5 ===")
    def RectPS(x1, y1, x2, y2):
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        P = 2 * (width + height)
        S = width * height
        return P, S
    
    print("Введите координаты противоположных вершин прямоугольника:")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    
    perimeter, area = RectPS(x1, y1, x2, y2)
    print(f"Периметр: {perimeter}")
    print(f"Площадь: {area}")
    return perimeter, area

def task6():
    print("\n=== ЗАДАНИЕ 6 ===")
    def TriangleP(a, h):
        b = ((a / 2) ** 2 + h ** 2) ** 0.5
        P = a + 2 * b
        return P
    
    print("Введите основание и высоту равнобедренного треугольника:")
    a = float(input("Основание a = "))
    h = float(input("Высота h = "))
    
    perimeter = TriangleP(a, h)
    print(f"Периметр: {perimeter:.2f}")
    return perimeter

def task7():
    print("\n=== ЗАДАНИЕ 7 ===")
    def InvertDigits(K):
        reversed_str = str(K)[::-1]
        return int(reversed_str)
    
    print("Введите целое положительное число:")
    k = int(input("K = "))
    
    if k <= 0:
        print("Ошибка: число должно быть положительным!")
        return 0
    
    inverted = InvertDigits(k)
    print(f"Число с обратным порядком цифр: {inverted}")
    return inverted

def task8():
    print("\n=== ЗАДАНИЕ 8 ===")
    def SumRange(A, B):
        if A > B:
            return 0
        
        total = 0
        for i in range(A, B + 1):
            total += i
        return total
    
    print("Введите два целых числа A и B:")
    a = int(input("A = "))
    b = int(input("B = "))
    
    result = SumRange(a, b)
    print(f"Сумма чисел от {a} до {b}: {result}")
    return result

def task9():
    print("\n=== ЗАДАНИЕ 9 ===")
    def TypeTri(x1, y1, x2, y2, x3, y3):
        def distance(x1, y1, x2, y2):
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        
        a = distance(x1, y1, x2, y2)
        b = distance(x2, y2, x3, y3)
        c = distance(x3, y3, x1, y1)
        
        if a == b == c:
            return "равносторонний"
        elif a == b or b == c or a == c:
            return "равнобедренный"
        elif abs(a*a + b*b - c*c) < 0.0001 or abs(a*a + c*c - b*b) < 0.0001 or abs(b*b + c*c - a*a) < 0.0001:
            return "прямоугольный"
        else:
            return "обычный"
    
    print("Введите координаты вершин треугольника:")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x3 = float(input("x3 = "))
    y3 = float(input("y3 = "))
    
    triangle_type = TypeTri(x1, y1, x2, y2, x3, y3)
    print(f"Треугольник: {triangle_type}")
    return triangle_type

def task10():
    print("\n=== ЗАДАНИЕ 10 ===")
    def Quarter(x, y):
        if x > 0 and y > 0:
            return 1
        elif x < 0 and y > 0:
            return 2
        elif x < 0 and y < 0:
            return 3
        elif x > 0 and y < 0:
            return 4
        else:
            return 0
    
    print("Введите координаты точки (ненулевые):")
    x = float(input("x = "))
    y = float(input("y = "))
    
    if x == 0 or y == 0:
        print("Ошибка: координаты не должны быть нулевыми!")
        return 0
    
    quarter = Quarter(x, y)
    print(f"Точка находится в {quarter}-й координатной четверти")
    return quarter

def task11():
    print("\n=== ЗАДАНИЕ 11 ===")
    def DigitCountSum(K):
        digits = str(K)
        count = len(digits)
        total = 0
        for digit in digits:
            total += int(digit)
        return count, total
    
    print("Введите целое положительное число:")
    k = int(input("K = "))
    
    if k <= 0:
        print("Ошибка: число должно быть положительным!")
        return 0, 0
    
    count, total = DigitCountSum(k)
    print(f"Количество цифр: {count}")
    print(f"Сумма цифр: {total}")
    return count, total

def task12():
    print("\n=== ЗАДАНИЕ 12 ===")
    def Calc(A, B, Op):
        if Op == 1:
            return A - B
        elif Op == 2:
            return A * B
        elif Op == 3:
            if B == 0:
                print("Ошибка: деление на ноль!")
                return 0
            return A / B
        else:
            return A + B
    
    print("Введите два ненулевых числа:")
    a = float(input("A = "))
    b = float(input("B = "))
    
    print("Выберите операцию:")
    print("1 - вычитание")
    print("2 - умножение") 
    print("3 - деление")
    print("другое - сложение")
    op = int(input("Операция = "))
    
    result = Calc(a, b, op)
    print(f"Результат: {result}")
    return result

def task13():
    print("\n=== ЗАДАНИЕ 13 ===")
    def LuckyNum(number):
        digits = str(number)
        if len(digits) != 4:
            return False
        
        first_sum = int(digits[0]) + int(digits[1])
        second_sum = int(digits[2]) + int(digits[3])
        return first_sum == second_sum
    
    print("Проверка счастливого номера:")
    number = int(input("Введите четырехзначное число: "))
    
    if LuckyNum(number):
        print(f"Число {number} - счастливое!")
    else:
        print(f"Число {number} - не счастливое")
    
    print("\nВсе четырехзначные счастливые номера:")
    lucky_numbers = []
    for num in range(1000, 10000):
        if LuckyNum(num):
            lucky_numbers.append(num)
    
    print(f"Найдено {len(lucky_numbers)} счастливых номеров")
    print("Первые 10:", lucky_numbers[:10])
    return lucky_numbers[:10]

def task14():
    print("\n=== ЗАДАНИЕ 14 ===")
    def DegToRad(D):
        import math
        return D * math.pi / 180
    
    print("Введите угол в градусах (0 < D < 360):")
    d = float(input("D = "))
    
    if d <= 0 or d >= 360:
        print("Ошибка: угол должен быть в диапазоне (0, 360)!")
        return 0
    
    radians = DegToRad(d)
    print(f"{d} градусов = {radians:.4f} радиан")
    return radians

def task15():
    print("\n=== ЗАДАНИЕ 15 ===")
    def IsLeapYear(Y):
        if Y % 4 != 0:
            return False
        elif Y % 100 != 0:
            return True
        elif Y % 400 != 0:
            return False
        else:
            return True
    
    print("Введите год:")
    year = int(input("Y = "))
    
    if IsLeapYear(year):
        print(f"{year} год - високосный")
    else:
        print(f"{year} год - не високосный")
    return IsLeapYear(year)

# Главная программа
def main():
    print("Выберите задание (1-15):")
    choice = input()
    
    if choice == '1':
        result = task1()
    elif choice == '2':
        result = task2()
    elif choice == '3':
        result = task3()
    elif choice == '4':
        result = task4()
    elif choice == '5':
        result = task5()
    elif choice == '6':
        result = task6()
    elif choice == '7':
        result = task7()
    elif choice == '8':
        result = task8()
    elif choice == '9':
        result = task9()
    elif choice == '10':
        result = task10()
    elif choice == '11':
        result = task11()
    elif choice == '12':
        result = task12()
    elif choice == '13':
        result = task13()
    elif choice == '14':
        result = task14()
    elif choice == '15':
        result = task15()
    else:
        print("Неверный выбор!")
        return
    
    print("\nРезультат:", result)

if __name__ == "__main__":
    main()