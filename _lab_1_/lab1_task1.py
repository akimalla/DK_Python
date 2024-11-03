# Исходный список с пропущенным элементом
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс пропущенного элемента
missing_index = numbers.index(None)

# Удаляем пропущенный элемент для расчета суммы и количества
filtered_numbers = [num for num in numbers if num is not None]

# Вычисляем сумму и количество элементов
total_sum = sum(filtered_numbers)
count = len(filtered_numbers) + 1  # Общее количество, включая пропуск

# Вычисляем среднее арифметическое
average = total_sum / count

# Заменяем пропущенный элемент средним арифметическим
numbers[missing_index] = average

# Выводим измененный список
print("Измененный список:", numbers)

