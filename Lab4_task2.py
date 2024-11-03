import json


def task() -> float:
    # Пример данных в формате JSON
    data = [
        {"score": 0.0009456152645028281, "weight": 1},
        {"score": 0.00020640167757499364, "weight": 1},
        {"score": 0, "weight": 1},
        {"score": 1.6557065217391307, "weight": 1},
        {"score": 0, "weight": 1},
        {"score": 0.6066065217391303, "weight": 1},
        {"score": 0.03126181644071977, "weight": 1},
        {"score": 0.001253973281817707, "weight": 1}
    ]

    # Инициализируем сумму
    total_sum = 0.0

    # Проходим по каждому словарю в списке
    for entry in data:
        # Проверяем наличие ключей и вычисляем произведение
        if 'score' in entry and 'weight' in entry:
            product = entry['score'] * entry['weight']
            total_sum += product

    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)


if __name__ == '__main__':
    print(task())