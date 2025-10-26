// Пункт 3: Сортировка вставками (Insertion Sort)
// Ввод: 5
// 12 11 13 5 6
// Вывод: 5 6 11 12 13

#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int n;
    std::cout << "Введите количество элементов: ";
    std::cin >> n;
    
    std::vector<int> arr(n);
    std::cout << "Введите элементы массива:" << std::endl;
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    
    std::cout << "Исходный массив: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    
    insertionSort(arr);
    
    std::cout << "\nОтсортированный массив: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    
    return 0;
}

// Пункт 9: Бинарный поиск (Binary Search)
// Ввод: 10
// 1 3 5 7 9 11 13 15 17 19
// 7
// Вывод: Элемент найден на позиции: 3

#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    int n;
    std::cout << "Введите количество элементов: ";
    std::cin >> n;
    
    std::vector<int> sortedArray(n);
    std::cout << "Введите отсортированные элементы массива:" << std::endl;
    for (int i = 0; i < n; i++) {
        std::cin >> sortedArray[i];
    }
    
    int target;
    std::cout << "Введите элемент для поиска: ";
    std::cin >> target;
    
    int result = binarySearch(sortedArray, target);
    
    if (result != -1) {
        std::cout << "Элемент найден на позиции: " << result << std::endl;
    } else {
        std::cout << "Элемент не найден" << std::endl;
    }
    
    return 0;
}

