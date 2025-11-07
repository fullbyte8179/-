#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // для std::swap

// Рекурсивная функция для генерации перестановок
void generatePermutations(std::string& str, int index, std::vector<std::string>& result) {
    // Базовый случай: достигнут конец строки
    if (index == str.length()) {
        result.push_back(str);
        return;
    }

    // Рекурсивный случай: перебираем все возможные символы для текущей позиции
    for (int i = index; i < str.length(); i++) {
        // Шаг вперед: Обмен элементов
        std::swap(str[index], str[i]);

        // Рекурсивный вызов для следующей позиции
        generatePermutations(str, index + 1, result);

        // Откат изменений (backtrack), чтобы вернуть строку в исходное состояние
        // для следующей итерации цикла
        std::swap(str[index], str[i]);
    }
}

int main() {
    std::string input_str = "ABC";
    std::vector<std::string> result;

    std::cout << "Исходная строка: " << input_str << std::endl;
    std::cout << "Все перестановки:" << std::endl;

    generatePermutations(input_str, 0, result);

    for (const auto& perm : result) {
        std::cout << perm << std::endl;
    }

    return 0;
}
