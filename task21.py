# ЗАДАНИЕ 21. РАБОТА С МАТРИЦАМИ В ФАЙЛАХ

import os

def create_matrix(rows, cols, values):
    """Создание матрицы из списка значений"""
    matrix = []
    for i in range(rows):
        row = values[i*cols:(i+1)*cols]
        matrix.append(row)
    return matrix

def print_matrix(matrix, name=""):
    """Вывод матрицы на экран"""
    if name:
        print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))

def write_matrix_to_file(matrix, filename):
    """Запись матрицы в файл"""
    with open(filename, 'a') as f:
        # Записываем размерность
        f.write(f"{len(matrix)} {len(matrix[0])}\n")
        # Записываем элементы
        for row in matrix:
            f.write(" ".join(str(x) for x in row) + "\n")

def read_matrices_from_file(filename):
    """Чтение матриц из файла"""
    matrices = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                # Читаем размерность
                dims = lines[i].strip().split()
                if len(dims) != 2:
                    break
                rows, cols = int(dims[0]), int(dims[1])
                i += 1
                
                # Читаем элементы матрицы
                matrix = []
                for r in range(rows):
                    if i >= len(lines):
                        break
                    row = list(map(int, lines[i].strip().split()))
                    if len(row) == cols:
                        matrix.append(row)
                    i += 1
                
                if len(matrix) == rows:
                    matrices.append(matrix)
    except:
        pass
    return matrices

def task1():
    print("\n=== ЗАДАНИЕ 1 ===")
    print("Перенести матрицы с a00=0 из первого файла во второй")
    
    # Создаем первый файл с матрицами
    with open('file1_1.txt', 'w') as f:
        # Матрица 1: 2x3, a00=1
        f.write("2 3\n1 2 3\n4 5 6\n")
        # Матрица 2: 2x2, a00=0
        f.write("2 2\n0 2\n3 4\n")
        # Матрица 3: 3x2, a00=5
        f.write("3 2\n5 6\n7 8\n9 10\n")
    
    # Создаем второй файл с матрицами
    with open('file2_1.txt', 'w') as f:
        # Матрица 1: 2x2
        f.write("2 2\n10 20\n30 40\n")
    
    print("Созданы файлы с матрицами:")
    print("Файл 1: 3 матрицы (2x3, 2x2 с a00=0, 3x2)")
    print("Файл 2: 1 матрица (2x2)")
    
    # Читаем матрицы из первого файла
    matrices1 = read_matrices_from_file('file1_1.txt')
    matrices2 = read_matrices_from_file('file2_1.txt')
    
    # Ищем матрицы с a00=0 в первом файле
    matrices_to_move = []
    remaining_matrices = []
    
    for matrix in matrices1:
        if matrix[0][0] == 0:  # проверяем a00
            matrices_to_move.append(matrix)
        else:
            remaining_matrices.append(matrix)
    
    # Добавляем найденные матрицы во второй файл
    for matrix in matrices_to_move:
        matrices2.append(matrix)
    
    # Перезаписываем файлы
    with open('file1_1.txt', 'w') as f:
        for matrix in remaining_matrices:
            write_matrix_to_file(matrix, 'file1_1.txt')
    
    with open('file2_1.txt', 'w') as f:
        for matrix in matrices2:
            write_matrix_to_file(matrix, 'file2_1.txt')
    
    # Выводим содержимое файлов
    print("\nСодержимое файла 1 (после переноса):")
    matrices1_new = read_matrices_from_file('file1_1.txt')
    for i, matrix in enumerate(matrices1_new):
        print_matrix(matrix, f"Матрица {i+1}")
    
    print("\nСодержимое файла 2 (после добавления):")
    matrices2_new = read_matrices_from_file('file2_1.txt')
    for i, matrix in enumerate(matrices2_new):
        print_matrix(matrix, f"Матрица {i+1}")
    
    # Удаляем временные файлы
    os.remove('file1_1.txt')
    os.remove('file2_1.txt')
    
    return len(matrices_to_move)

def task2():
    print("\n=== ЗАДАНИЕ 2 ===")
    print("Убрать лишние матрицы из большего файла в третий")
    
    # Создаем файлы
    with open('file1_2.txt', 'w') as f:
        # 3 матрицы в первом файле
        f.write("2 2\n1 2\n3 4\n")
        f.write("2 2\n5 6\n7 8\n")
    
    with open('file2_2.txt', 'w') as f:
        # 2 матрицы во втором файле
        f.write("2 2\n9 10\n11 12\n")
    
    print("Созданы файлы:")
    print("Файл 1: 2 матрицы")
    print("Файл 2: 1 матрица")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_2.txt')
    matrices2 = read_matrices_from_file('file2_2.txt')
    
    # Определяем, в каком файле больше матриц
    if len(matrices1) > len(matrices2):
        bigger = matrices1
        smaller = matrices2
        bigger_file = 'file1_2.txt'
    else:
        bigger = matrices2
        smaller = matrices1
        bigger_file = 'file2_2.txt'
    
    # Разделяем матрицы: оставляем столько же, сколько в меньшем файле
    keep_count = len(smaller)
    matrices_to_keep = bigger[:keep_count]
    matrices_to_move = bigger[keep_count:]
    
    # Создаем третий файл для лишних матриц
    with open('file3_2.txt', 'w') as f:
        for matrix in matrices_to_move:
            write_matrix_to_file(matrix, 'file3_2.txt')
    
    # Обновляем больший файл
    with open(bigger_file, 'w') as f:
        for matrix in matrices_to_keep:
            write_matrix_to_file(matrix, bigger_file)
    
    # Выводим содержимое
    print("\nСодержимое файла 1:")
    m1 = read_matrices_from_file('file1_2.txt')
    for i, matrix in enumerate(m1):
        print_matrix(matrix, f"Матрица {i+1}")
    
    print("\nСодержимое файла 2:")
    m2 = read_matrices_from_file('file2_2.txt')
    for i, matrix in enumerate(m2):
        print_matrix(matrix, f"Матрица {i+1}")
    
    print("\nСодержимое файла 3 (лишние матрицы):")
    m3 = read_matrices_from_file('file3_2.txt')
    for i, matrix in enumerate(m3):
        print_matrix(matrix, f"Матрица {i+1}")
    
    # Удаляем временные файлы
    os.remove('file1_2.txt')
    os.remove('file2_2.txt')
    os.remove('file3_2.txt')
    
    return len(matrices_to_move)

def task3():
    print("\n=== ЗАДАНИЕ 3 ===")
    print("Умножение пар матриц из файла")
    
    # Создаем файл с парами матриц (m×n и m×l)
    with open('pairs.txt', 'w') as f:
        # Первая пара
        f.write("2 3\n1 2 3\n4 5 6\n")  # матрица 2×3
        f.write("2 2\n1 0\n0 1\n")       # матрица 2×2
        
        # Вторая пара  
        f.write("2 2\n2 3\n4 5\n")       # матрица 2×2
        f.write("2 3\n1 1 1\n2 2 2\n")   # матрица 2×3
    
    print("Создан файл с 2 парами матриц")
    
    # Читаем пары матриц
    pairs = []
    with open('pairs.txt', 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            # Читаем первую матрицу
            dims1 = lines[i].strip().split()
            if len(dims1) != 2:
                break
            rows1, cols1 = int(dims1[0]), int(dims1[1])
            i += 1
            
            mat1 = []
            for r in range(rows1):
                row = list(map(int, lines[i].strip().split()))
                mat1.append(row)
                i += 1
            
            # Читаем вторую матрицу
            dims2 = lines[i].strip().split()
            if len(dims2) != 2:
                break
            rows2, cols2 = int(dims2[0]), int(dims2[1])
            i += 1
            
            mat2 = []
            for r in range(rows2):
                row = list(map(int, lines[i].strip().split()))
                mat2.append(row)
                i += 1
            
            pairs.append((mat1, mat2))
    
    # Умножаем матрицы и записываем результаты
    results = []
    with open('products.txt', 'w') as f:
        for mat1, mat2 in pairs:
            # Умножение матриц (упрощенное)
            rows1, cols1 = len(mat1), len(mat1[0])
            rows2, cols2 = len(mat2), len(mat2[0])
            
            if cols1 == rows2:  # можно умножить
                # Создаем результирующую матрицу
                result = [[0 for _ in range(cols2)] for _ in range(rows1)]
                
                for i in range(rows1):
                    for j in range(cols2):
                        for k in range(cols1):
                            result[i][j] += mat1[i][k] * mat2[k][j]
                
                results.append(result)
                
                # Записываем результат
                f.write(f"{rows1} {cols2}\n")
                for row in result:
                    f.write(" ".join(str(x) for x in row) + "\n")
    
    print("\nИсходные пары матриц:")
    for i, (mat1, mat2) in enumerate(pairs):
        print(f"\nПара {i+1}:")
        print_matrix(mat1, "Матрица A")
        print_matrix(mat2, "Матрица B")
    
    print("\nРезультаты умножения:")
    for i, result in enumerate(results):
        print_matrix(result, f"Произведение {i+1}")
    
    os.remove('pairs.txt')
    os.remove('products.txt')
    return len(results)

def task4():
    print("\n=== ЗАДАНИЕ 4 ===")
    print("Добавить во второй файл матрицы из первого, которых нет во втором")
    
    # Создаем матрицы
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    mat3 = [[9, 10], [11, 12]]
    
    # Записываем в файлы
    with open('file1_4.txt', 'w') as f:
        write_matrix_to_file(mat1, 'file1_4.txt')
        write_matrix_to_file(mat2, 'file1_4.txt')
        write_matrix_to_file(mat3, 'file1_4.txt')
    
    with open('file2_4.txt', 'w') as f:
        write_matrix_to_file(mat1, 'file2_4.txt')  # эта матрица уже есть
    
    print("Созданы файлы:")
    print("Файл 1: 3 матрицы 2x2")
    print("Файл 2: 1 матрица 2x2 (совпадает с первой из файла 1)")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_4.txt')
    matrices2 = read_matrices_from_file('file2_4.txt')
    
    # Находим матрицы из первого файла, которых нет во втором
    matrices_to_add = []
    for mat in matrices1:
        found = False
        for mat2 in matrices2:
            if mat == mat2:  # простая проверка на равенство
                found = True
                break
        if not found:
            matrices_to_add.append(mat)
    
    # Добавляем найденные матрицы во второй файл
    for mat in matrices_to_add:
        matrices2.append(mat)
    
    # Перезаписываем второй файл
    with open('file2_4.txt', 'w') as f:
        for mat in matrices2:
            write_matrix_to_file(mat, 'file2_4.txt')
    
    print(f"\nНайдено матриц для добавления: {len(matrices_to_add)}")
    
    # Выводим содержимое
    print("\nСодержимое файла 1:")
    m1 = read_matrices_from_file('file1_4.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nСодержимое файла 2 (после добавления):")
    m2 = read_matrices_from_file('file2_4.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('file1_4.txt')
    os.remove('file2_4.txt')
    return len(matrices_to_add)

def task5():
    print("\n=== ЗАДАНИЕ 5 ===")
    print("Найти матрицы с четной суммой положительных четных элементов")
    
    # Создаем файл с матрицами
    with open('matrices5.txt', 'w') as f:
        # Матрица 1: положительные четные: 2, 4, 6 → сумма 12 (четная)
        f.write("2 3\n1 2 3\n4 5 6\n")
        # Матрица 2: положительные четные: 8 → сумма 8 (четная)
        f.write("2 2\n-1 7\n8 -3\n")
        # Матрица 3: нет положительных четных → сумма 0 (четная)
        f.write("2 2\n1 3\n5 7\n")
    
    print("Создан файл с 3 матрицами")
    
    # Читаем матрицы
    matrices = read_matrices_from_file('matrices5.txt')
    
    matrices_with_even_sum = []
    remaining_matrices = []
    
    for mat in matrices:
        # Вычисляем сумму положительных четных элементов
        total = 0
        for row in mat:
            for elem in row:
                if elem > 0 and elem % 2 == 0:
                    total += elem
        
        print(f"Сумма положительных четных элементов: {total}")
        
        if total % 2 == 0:  # четная сумма
            matrices_with_even_sum.append(mat)
            # Создаем единичную матрицу для замены
            rows, cols = len(mat), len(mat[0])
            identity = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    if i == j and i < cols:  # на главной диагонали
                        row.append(1)
                    else:
                        row.append(0)
                identity.append(row)
            remaining_matrices.append(identity)
        else:
            remaining_matrices.append(mat)
    
    # Записываем матрицы с четными суммами в отдельный файл
    with open('even_sum_matrices.txt', 'w') as f:
        for mat in matrices_with_even_sum:
            write_matrix_to_file(mat, 'even_sum_matrices.txt')
    
    # Перезаписываем исходный файл
    with open('matrices5.txt', 'w') as f:
        for mat in remaining_matrices:
            write_matrix_to_file(mat, 'matrices5.txt')
    
    print(f"\nНайдено матриц с четной суммой: {len(matrices_with_even_sum)}")
    
    # Выводим содержимое
    print("\nИсходный файл (после замены):")
    m1 = read_matrices_from_file('matrices5.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл с матрицами с четной суммой:")
    m2 = read_matrices_from_file('even_sum_matrices.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('matrices5.txt')
    os.remove('even_sum_matrices.txt')
    return len(matrices_with_even_sum)

def task6():
    print("\n=== ЗАДАНИЕ 6 ===")
    print("Поменять местами нечетные матрицы из двух файлов")
    
    # Создаем файлы
    with open('file1_6.txt', 'w') as f:
        # 4 матрицы в первом файле
        f.write("2 2\n1 1\n1 1\n")   # нечетная (1)
        f.write("2 2\n2 2\n2 2\n")   # четная (2)
        f.write("2 2\n3 3\n3 3\n")   # нечетная (3)
        f.write("2 2\n4 4\n4 4\n")   # четная (4)
    
    with open('file2_6.txt', 'w') as f:
        # 3 матрицы во втором файле
        f.write("2 2\nA A\nA A\n")   # нечетная (1) - условно
        f.write("2 2\nB B\nB B\n")   # четная (2)
        f.write("2 2\nC C\nC C\n")   # нечетная (3)
    
    print("Созданы файлы:")
    print("Файл 1: 4 матрицы (значения 1,2,3,4)")
    print("Файл 2: 3 матрицы (значения A,B,C)")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_6.txt')
    matrices2 = read_matrices_from_file('file2_6.txt')
    
    # Меняем местами нечетные матрицы (индексы 0, 2, 4...)
    min_len = min(len(matrices1), len(matrices2))
    
    for i in range(min_len):
        if i % 2 == 0:  # нечетная по порядку (индекс четный)
            matrices1[i], matrices2[i] = matrices2[i], matrices1[i]
    
    # Перезаписываем файлы
    with open('file1_6.txt', 'w') as f:
        for mat in matrices1:
            write_matrix_to_file(mat, 'file1_6.txt')
    
    with open('file2_6.txt', 'w') as f:
        for mat in matrices2:
            write_matrix_to_file(mat, 'file2_6.txt')
    
    # Выводим содержимое
    print("\nФайл 1 (после обмена):")
    m1 = read_matrices_from_file('file1_6.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 2 (после обмена):")
    m2 = read_matrices_from_file('file2_6.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('file1_6.txt')
    os.remove('file2_6.txt')
    return min_len

def task7():
    print("\n=== ЗАДАНИЕ 7 ===")
    print("Добавить единичные матрицы в файл с меньшим числом матриц")
    
    # Создаем файлы с квадратными матрицами
    with open('file1_7.txt', 'w') as f:
        # 2 матрицы 3x3
        f.write("3 3\n1 2 3\n4 5 6\n7 8 9\n")
        f.write("3 3\n9 8 7\n6 5 4\n3 2 1\n")
    
    with open('file2_7.txt', 'w') as f:
        # 1 матрица 3x3
        f.write("3 3\n0 0 0\n0 0 0\n0 0 0\n")
    
    print("Созданы файлы с квадратными матрицами 3x3:")
    print("Файл 1: 2 матрицы")
    print("Файл 2: 1 матрица")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_7.txt')
    matrices2 = read_matrices_from_file('file2_7.txt')
    
    # Определяем, в каком файле меньше матриц
    if len(matrices1) < len(matrices2):
        smaller = matrices1
        smaller_file = 'file1_7.txt'
        bigger_count = len(matrices2)
    else:
        smaller = matrices2
        smaller_file = 'file2_7.txt'
        bigger_count = len(matrices1)
    
    # Добавляем единичные матрицы
    if len(smaller) < bigger_count:
        # Определяем размерность (предполагаем, что все матрицы одной размерности)
        if smaller:
            n = len(smaller[0])  # размер квадратной матрицы
        else:
            n = 3  # по умолчанию
            
        # Создаем единичные матрицы
        for _ in range(bigger_count - len(smaller)):
            identity = []
            for i in range(n):
                row = []
                for j in range(n):
                    if i == j:
                        row.append(1)
                    else:
                        row.append(0)
                identity.append(row)
            smaller.append(identity)
    
    # Перезаписываем файл
    with open(smaller_file, 'w') as f:
        for mat in smaller:
            write_matrix_to_file(mat, smaller_file)
    
    # Выводим содержимое
    print("\nФайл 1:")
    m1 = read_matrices_from_file('file1_7.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 2:")
    m2 = read_matrices_from_file('file2_7.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('file1_7.txt')
    os.remove('file2_7.txt')
    return abs(len(matrices1) - len(matrices2))

def task8():
    print("\n=== ЗАДАНИЕ 8 ===")
    print("Найти матрицы с нечетной суммой диагональных элементов")
    
    # Создаем файл с матрицами
    with open('matrices8.txt', 'w') as f:
        # Матрица 1: 2x3, главная диагональ: 1,5 → сумма 6 (четная)
        f.write("2 3\n1 2 3\n4 5 6\n")
        # Матрица 2: 3x3, главная диагональ: 1,5,9 → сумма 15 (нечетная)
        f.write("3 3\n1 2 3\n4 5 6\n7 8 9\n")
        # Матрица 3: 2x2, главная диагональ: 2,3 → сумма 5 (нечетная)
        f.write("2 2\n2 1\n4 3\n")
    
    print("Создан файл с 3 матрицами")
    
    # Читаем матрицы
    matrices = read_matrices_from_file('matrices8.txt')
    
    matrices_with_odd_sum = []
    updated_matrices = []
    
    for mat in matrices:
        # Вычисляем сумму элементов главной диагонали
        total = 0
        min_dim = min(len(mat), len(mat[0]))
        for i in range(min_dim):
            total += mat[i][i]
        
        print(f"Сумма диагональных элементов: {total}")
        
        if total % 2 == 1:  # нечетная сумма
            matrices_with_odd_sum.append(mat)
            # Создаем транспонированную матрицу для замены
            rows, cols = len(mat), len(mat[0])
            transposed = []
            for j in range(cols):
                row = []
                for i in range(rows):
                    row.append(mat[i][j])
                transposed.append(row)
            updated_matrices.append(transposed)
        else:
            updated_matrices.append(mat)
    
    # Записываем матрицы с нечетными суммами в отдельный файл
    with open('odd_sum_matrices.txt', 'w') as f:
        for mat in matrices_with_odd_sum:
            write_matrix_to_file(mat, 'odd_sum_matrices.txt')
    
    # Перезаписываем исходный файл
    with open('matrices8.txt', 'w') as f:
        for mat in updated_matrices:
            write_matrix_to_file(mat, 'matrices8.txt')
    
    print(f"\nНайдено матриц с нечетной суммой: {len(matrices_with_odd_sum)}")
    
    # Выводим содержимое
    print("\nИсходный файл (после замены на транспонированные):")
    m1 = read_matrices_from_file('matrices8.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл с матрицами с нечетной суммой:")
    m2 = read_matrices_from_file('odd_sum_matrices.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('matrices8.txt')
    os.remove('odd_sum_matrices.txt')
    return len(matrices_with_odd_sum)

def task9():
    print("\n=== ЗАДАНИЕ 9 ===")
    print("Разделить квадратные матрицы на симметричные и несимметричные")
    
    # Создаем файл с квадратными матрицами
    with open('matrices9.txt', 'w') as f:
        # Матрица 1: симметричная
        f.write("3 3\n1 2 3\n2 4 5\n3 5 6\n")
        # Матрица 2: несимметричная
        f.write("2 2\n1 2\n3 4\n")
        # Матрица 3: симметричная
        f.write("2 2\n5 6\n6 7\n")
    
    print("Создан файл с 3 квадратными матрицами")
    
    # Читаем матрицы
    matrices = read_matrices_from_file('matrices9.txt')
    
    symmetric = []
    asymmetric = []
    
    for mat in matrices:
        # Проверяем симметричность (A = A^T)
        is_symmetric = True
        rows, cols = len(mat), len(mat[0])
        
        if rows != cols:  # не квадратная
            is_symmetric = False
        else:
            for i in range(rows):
                for j in range(cols):
                    if mat[i][j] != mat[j][i]:
                        is_symmetric = False
                        break
                if not is_symmetric:
                    break
        
        if is_symmetric:
            symmetric.append(mat)
        else:
            asymmetric.append(mat)
    
    # Записываем в разные файлы
    with open('symmetric.txt', 'w') as f:
        for mat in symmetric:
            write_matrix_to_file(mat, 'symmetric.txt')
    
    with open('asymmetric.txt', 'w') as f:
        for mat in asymmetric:
            write_matrix_to_file(mat, 'asymmetric.txt')
    
    print(f"\nСимметричных матриц: {len(symmetric)}")
    print(f"Несимметричных матриц: {len(asymmetric)}")
    
    # Выводим содержимое
    print("\nИсходный файл:")
    for i, mat in enumerate(matrices):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл с симметричными матрицами:")
    sym = read_matrices_from_file('symmetric.txt')
    for i, mat in enumerate(sym):
        print_matrix(mat, f"Симметричная {i+1}")
    
    print("\nФайл с несимметричными матрицами:")
    asym = read_matrices_from_file('asymmetric.txt')
    for i, mat in enumerate(asym):
        print_matrix(mat, f"Несимметричная {i+1}")
    
    os.remove('matrices9.txt')
    os.remove('symmetric.txt')
    os.remove('asymmetric.txt')
    return len(symmetric), len(asymmetric)

def task10():
    print("\n=== ЗАДАНИЕ 10 ===")
    print("Умножение соответствующих матриц из двух файлов")
    
    # Создаем первый файл с матрицами m×n
    with open('file1_10.txt', 'w') as f:
        # 2 матрицы 2×3
        f.write("2 3\n1 2 3\n4 5 6\n")
        f.write("2 3\n2 0 1\n1 1 1\n")
    
    # Создаем второй файл с матрицами m×l
    with open('file2_10.txt', 'w') as f:
        # 2 матрицы 3×2
        f.write("3 2\n1 0\n0 1\n1 1\n")
        f.write("3 2\n2 1\n1 2\n0 0\n")
    
    print("Созданы файлы:")
    print("Файл 1: 2 матрицы 2x3")
    print("Файл 2: 2 матрицы 3x2")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_10.txt')
    matrices2 = read_matrices_from_file('file2_10.txt')
    
    # Умножаем соответствующие матрицы
    results = []
    min_len = min(len(matrices1), len(matrices2))
    
    for i in range(min_len):
        mat1 = matrices1[i]
        mat2 = matrices2[i]
        
        # Проверяем возможность умножения (cols1 = rows2)
        if len(mat1[0]) == len(mat2):
            # Умножение матриц
            rows1, cols1 = len(mat1), len(mat1[0])
            rows2, cols2 = len(mat2), len(mat2[0])
            
            result = [[0 for _ in range(cols2)] for _ in range(rows1)]
            
            for r in range(rows1):
                for c in range(cols2):
                    for k in range(cols1):
                        result[r][c] += mat1[r][k] * mat2[k][c]
            
            results.append((mat1, mat2, result))
    
    # Записываем в третий файл в виде структур
    with open('results_10.txt', 'w') as f:
        for mat1, mat2, result in results:
            # Записываем первую матрицу
            f.write("Матрица A:\n")
            write_matrix_to_file(mat1, 'results_10.txt')
            
            # Записываем вторую матрицу
            f.write("Матрица B:\n")
            write_matrix_to_file(mat2, 'results_10.txt')
            
            # Записываем результат
            f.write("Результат A×B:\n")
            write_matrix_to_file(result, 'results_10.txt')
            
            f.write("---\n")
    
    # Выводим содержимое
    print("\nФайл 1:")
    for i, mat in enumerate(matrices1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 2:")
    for i, mat in enumerate(matrices2):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 3 (результаты):")
    with open('results_10.txt', 'r') as f:
        print(f.read())
    
    os.remove('file1_10.txt')
    os.remove('file2_10.txt')
    os.remove('results_10.txt')
    return len(results)

# Задачи 11-15
def task11():
    print("\n=== ЗАДАНИЕ 11 ===")
    print("Обмен нечетными матрицами из первого файла с четными из второго")
    
    # Создаем первый файл с k матрицами
    with open('file1_11.txt', 'w') as f:
        # 3 матрицы 2x2
        for i in range(3):
            f.write(f"2 2\n{i*10+1} {i*10+2}\n{i*10+3} {i*10+4}\n")
    
    # Создаем второй файл с l матрицами  
    with open('file2_11.txt', 'w') as f:
        # 4 матрицы 2x2
        for i in range(4):
            f.write(f"2 2\n{i*100+10} {i*100+20}\n{i*100+30} {i*100+40}\n")
    
    print("Созданы файлы:")
    print("Файл 1: 3 матрицы 2x2 (номера 1-3)")
    print("Файл 2: 4 матрицы 2x2 (номера 10-40)")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_11.txt')
    matrices2 = read_matrices_from_file('file2_11.txt')
    
    # Меняем местами нечетные из первого с четными из второго
    # (нумерация с 1: нечетные - 1,3,5...; четные - 2,4,6...)
    # В индексах: нечетные - четные индексы (0,2,4...), четные - нечетные индексы (1,3,5...)
    
    min_len = min(len(matrices1), len(matrices2))
    
    # Индексы для обмена: нечетные из первого (индексы 0,2,4...) 
    # с четными из второго (индексы 1,3,5...)
    for i in range(0, min_len, 2):  # нечетные из первого
        if i + 1 < len(matrices2):  # есть четная во втором
            matrices1[i], matrices2[i+1] = matrices2[i+1], matrices1[i]
    
    # Определяем, какой файл больше
    if len(matrices1) > len(matrices2):
        bigger = matrices1
        bigger_file = 'file1_11.txt'
        smaller_len = len(matrices2)
    else:
        bigger = matrices2
        bigger_file = 'file2_11.txt'
        smaller_len = len(matrices1)
    
    # Оставшиеся матрицы из большего файла записываем в третий
    remaining = bigger[smaller_len:]
    
    # Записываем обновленные файлы
    with open('file1_11.txt', 'w') as f:
        for mat in matrices1[:min_len]:
            write_matrix_to_file(mat, 'file1_11.txt')
    
    with open('file2_11.txt', 'w') as f:
        for mat in matrices2[:min_len]:
            write_matrix_to_file(mat, 'file2_11.txt')
    
    # Записываем оставшиеся в третий файл
    with open('remaining_11.txt', 'w') as f:
        for mat in remaining:
            write_matrix_to_file(mat, 'remaining_11.txt')
    
    # Выводим содержимое
    print("\nФайл 1 (после обмена):")
    m1 = read_matrices_from_file('file1_11.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 2 (после обмена):")
    m2 = read_matrices_from_file('file2_11.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 3 (оставшиеся матрицы):")
    m3 = read_matrices_from_file('remaining_11.txt')
    for i, mat in enumerate(m3):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('file1_11.txt')
    os.remove('file2_11.txt')
    os.remove('remaining_11.txt')
    return len(remaining)

def task12():
    print("\n=== ЗАДАНИЕ 12 ===")
    print("Сумма пар матриц из файла")
    
    # Создаем файл с парами матриц
    with open('pairs12.txt', 'w') as f:
        # Первая пара
        f.write("2 2\n1 2\n3 4\n")  # матрица A
        f.write("2 2\n5 6\n7 8\n")  # матрица B
        
        # Вторая пара
        f.write("2 2\n2 0\n0 2\n")  # матрица C
        f.write("2 2\n1 1\n1 1\n")  # матрица D
    
    print("Создан файл с 2 парами матриц 2x2")
    
    # Читаем пары матриц
    pairs = []
    matrices = read_matrices_from_file('pairs12.txt')
    
    # Группируем по парам
    for i in range(0, len(matrices), 2):
        if i + 1 < len(matrices):
            pairs.append((matrices[i], matrices[i+1]))
    
    # Вычисляем суммы и записываем во второй файл
    sums = []
    with open('sums12.txt', 'w') as f:
        for mat1, mat2 in pairs:
            # Сумма матриц
            rows, cols = len(mat1), len(mat1[0])
            result = []
            for r in range(rows):
                row = []
                for c in range(cols):
                    row.append(mat1[r][c] + mat2[r][c])
                result.append(row)
            
            sums.append(result)
            write_matrix_to_file(result, 'sums12.txt')
    
    # Выводим содержимое
    print("\nИсходный файл (пары матриц):")
    for i, (mat1, mat2) in enumerate(pairs):
        print(f"\nПара {i+1}:")
        print_matrix(mat1, "Матрица A")
        print_matrix(mat2, "Матрица B")
    
    print("\nФайл с суммами:")
    for i, result in enumerate(sums):
        print_matrix(result, f"Сумма {i+1}")
    
    os.remove('pairs12.txt')
    os.remove('sums12.txt')
    return len(sums)

def task13():
    print("\n=== ЗАДАНИЕ 13 ===")
    print("Найти матрицы с нечетной суммой отрицательных нечетных элементов")
    
    # Создаем файл с матрицами
    with open('matrices13.txt', 'w') as f:
        # Матрица 1: отрицательные нечетные: -1, -3, -5 → сумма -9 (нечетная)
        f.write("2 2\n-1 2\n-3 -5\n")
        # Матрица 2: отрицательные нечетные: -1 → сумма -1 (нечетная)
        f.write("2 2\n1 -1\n2 -2\n")
        # Матрица 3: нет отрицательных нечетных → сумма 0 (четная)
        f.write("2 2\n2 4\n6 8\n")
    
    print("Создан файл с 3 матрицами")
    
    # Читаем матрицы
    matrices = read_matrices_from_file('matrices13.txt')
    
    matrices_with_odd_sum = []
    updated_matrices = []
    
    for mat in matrices:
        # Вычисляем сумму отрицательных нечетных элементов
        total = 0
        for row in mat:
            for elem in row:
                if elem < 0 and elem % 2 == -1:  # отрицательное нечетное
                    total += elem
        
        print(f"Сумма отрицательных нечетных элементов: {total}")
        
        if total % 2 == -1 or total % 2 == 1:  # нечетная сумма
            matrices_with_odd_sum.append(mat)
            # Создаем единичную матрицу для замены
            rows, cols = len(mat), len(mat[0])
            identity = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    if i == j and i < cols:
                        row.append(1)
                    else:
                        row.append(0)
                identity.append(row)
            updated_matrices.append(identity)
        else:
            updated_matrices.append(mat)
    
    # Записываем матрицы с нечетными суммами в отдельный файл
    with open('odd_sum_matrices13.txt', 'w') as f:
        for mat in matrices_with_odd_sum:
            write_matrix_to_file(mat, 'odd_sum_matrices13.txt')
    
    # Перезаписываем исходный файл
    with open('matrices13.txt', 'w') as f:
        for mat in updated_matrices:
            write_matrix_to_file(mat, 'matrices13.txt')
    
    print(f"\nНайдено матриц с нечетной суммой: {len(matrices_with_odd_sum)}")
    
    # Выводим содержимое
    print("\nИсходный файл (после замены):")
    m1 = read_matrices_from_file('matrices13.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл с матрицами с нечетной суммой:")
    m2 = read_matrices_from_file('odd_sum_matrices13.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('matrices13.txt')
    os.remove('odd_sum_matrices13.txt')
    return len(matrices_with_odd_sum)

def task14():
    print("\n=== ЗАДАНИЕ 14 ===")
    print("Перенести матрицы с суммой первой строки > заданного числа")
    
    # Создаем файлы
    with open('file1_14.txt', 'w') as f:
        # Матрица 1: первая строка [1,2,3] сумма=6
        f.write("2 3\n1 2 3\n4 5 6\n")
        # Матрица 2: первая строка [10,20] сумма=30
        f.write("2 2\n10 20\n30 40\n")
        # Матрица 3: первая строка [0,1,2] сумма=3
        f.write("3 3\n0 1 2\n3 4 5\n6 7 8\n")
    
    with open('file2_14.txt', 'w') as f:
        f.write("2 2\n100 200\n300 400\n")
    
    print("Созданы файлы:")
    print("Файл 1: 3 матрицы")
    print("Файл 2: 1 матрица")
    
    threshold = 5  # заданное число
    print(f"Заданное число: {threshold}")
    
    # Читаем матрицы
    matrices1 = read_matrices_from_file('file1_14.txt')
    matrices2 = read_matrices_from_file('file2_14.txt')
    
    # Находим матрицы для переноса
    matrices_to_move = []
    remaining_matrices = []
    
    for mat in matrices1:
        # Сумма первой строки
        if mat:  # матрица не пустая
            first_row_sum = sum(mat[0])
            print(f"Сумма первой строки: {first_row_sum}")
            
            if first_row_sum > threshold:
                matrices_to_move.append(mat)
            else:
                remaining_matrices.append(mat)
    
    # Добавляем найденные матрицы во второй файл
    for mat in matrices_to_move:
        matrices2.append(mat)
    
    # Перезаписываем файлы
    with open('file1_14.txt', 'w') as f:
        for mat in remaining_matrices:
            write_matrix_to_file(mat, 'file1_14.txt')
    
    with open('file2_14.txt', 'w') as f:
        for mat in matrices2:
            write_matrix_to_file(mat, 'file2_14.txt')
    
    print(f"\nПеренесено матриц: {len(matrices_to_move)}")
    
    # Выводим содержимое
    print("\nФайл 1 (после переноса):")
    m1 = read_matrices_from_file('file1_14.txt')
    for i, mat in enumerate(m1):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл 2 (после добавления):")
    m2 = read_matrices_from_file('file2_14.txt')
    for i, mat in enumerate(m2):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('file1_14.txt')
    os.remove('file2_14.txt')
    return len(matrices_to_move)

def task15():
    print("\n=== ЗАДАНИЕ 15 ===")
    print("Найти матрицы с произведением диагонали > заданного числа")
    
    # Создаем файл с матрицами
    with open('matrices15.txt', 'w') as f:
        # Матрица 1: 2x2, диагональ: 1,4 → произведение 4
        f.write("2 2\n1 2\n3 4\n")
        # Матрица 2: 3x3, диагональ: 2,5,8 → произведение 80
        f.write("3 3\n2 1 1\n1 5 1\n1 1 8\n")
        # Матрица 3: 2x3, диагональ: 1,5 → произведение 5
        f.write("2 3\n1 2 3\n4 5 6\n")
    
    print("Создан файл с 3 матрицами")
    
    threshold = 10  # заданное число
    print(f"Заданное число: {threshold}")
    
    # Читаем матрицы
    matrices = read_matrices_from_file('matrices15.txt')
    
    matrices_with_big_product = []
    
    for mat in matrices:
        # Вычисляем произведение элементов главной диагонали
        product = 1
        min_dim = min(len(mat), len(mat[0]))
        for i in range(min_dim):
            product *= mat[i][i]
        
        print(f"Произведение диагональных элементов: {product}")
        
        if product > threshold:
            matrices_with_big_product.append(mat)
    
    # Записываем найденные матрицы в отдельный файл
    with open('big_product_matrices.txt', 'w') as f:
        for mat in matrices_with_big_product:
            write_matrix_to_file(mat, 'big_product_matrices.txt')
    
    print(f"\nНайдено матриц с произведением > {threshold}: {len(matrices_with_big_product)}")
    
    # Выводим содержимое
    print("\nИсходный файл:")
    for i, mat in enumerate(matrices):
        print_matrix(mat, f"Матрица {i+1}")
    
    print("\nФайл с матрицами (произведение > заданного числа):")
    big_mats = read_matrices_from_file('big_product_matrices.txt')
    for i, mat in enumerate(big_mats):
        print_matrix(mat, f"Матрица {i+1}")
    
    os.remove('matrices15.txt')
    os.remove('big_product_matrices.txt')
    return len(matrices_with_big_product)

# Главная программа
def main():
    print("ВЫБЕРИТЕ ЗАДАНИЕ (1-15):")
    print("Задания 1-10:")
    print("1. Перенести матрицы с a00=0")
    print("2. Убрать лишние матрицы в третий файл")
    print("3. Умножение пар матриц")
    print("4. Добавить отсутствующие матрицы")
    print("5. Матрицы с четной суммой положительных четных")
    print("6. Обмен нечетными матрицами")
    print("7. Добавить единичные матрицы")
    print("8. Матрицы с нечетной суммой диагонали")
    print("9. Разделить на симметричные/несимметричные")
    print("10. Умножение матриц из двух файлов")
    print("\nЗадания 11-15:")
    print("11. Обмен нечетными/четными матрицами")
    print("12. Сумма пар матриц")
    print("13. Матрицы с нечетной суммой отрицательных нечетных")
    print("14. Перенести матрицы с большой суммой первой строки")
    print("15. Матрицы с большим произведением диагонали")
    
    choice = input("\nВведите номер задания (1-15): ")
    
    tasks = {
        '1': task1, '2': task2, '3': task3, '4': task4, '5': task5,
        '6': task6, '7': task7, '8': task8, '9': task9, '10': task10,
        '11': task11, '12': task12, '13': task13, '14': task14, '15': task15
    }
    
    if choice in tasks:
        result = tasks[choice]()
        print(f"\nЗадание {choice} выполнено!")
        print(f"Результат: {result}")
        return result
    else:
        print("Неверный выбор! Введите число от 1 до 15.")
        return None

if __name__ == "__main__":
    main()