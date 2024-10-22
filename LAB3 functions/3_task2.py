# TODO Напишите функцию find_common_participants


#participants_first_group = "Иванов|Петров|Сидоров"
#participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)