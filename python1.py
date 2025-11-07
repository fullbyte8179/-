def generate_permutations(char_list, index, result):
    # Базовый случай: достигнут конец списка
    if index == len(char_list):
        result.append("".join(char_list))
        return

    # Рекурсивный случай: перебираем все возможные символы для текущей позиции
    for i in range(index, len(char_list)):
        # Шаг вперед: Обмен элементов
        char_list[index], char_list[i] = char_list[i], char_list[index]

        # Рекурсивный вызов для следующей позиции
        generate_permutations(char_list, index + 1, result)

        # Откат изменений (backtrack)
        char_list[index], char_list[i] = char_list[i], char_list[index]

# Тестирование
input_str = "ABC"
result = []
print(f"Исходная строка: {input_str}")
print("Все перестановки:")

# Преобразуем строку в список для удобства манипуляций
generate_permutations(list(input_str), 0, result)

for perm in result:
    print(perm)
