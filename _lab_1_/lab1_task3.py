# Определение параметров книги
pages_in_book = 100          # Количество страниц в книге
lines_per_page = 50          # Количество строк на странице
chars_per_line = 25          # Количество символов в строке
bytes_per_char = 4           # Объем хранения одного символа в байтах

# Объем дискеты в байтах
disk_capacity_mb = 1.44
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # Преобразование в байты

# Расчет объема одной книги
total_chars_in_book = pages_in_book * lines_per_page * chars_per_line
book_size_bytes = total_chars_in_book * bytes_per_char

# Расчет количества книг на дискете
number_of_books = disk_capacity_bytes // book_size_bytes  # Целочисленное деление

# Вывод результата без точки
print("Количество книг, помещающихся на дискету:", int(number_of_books))