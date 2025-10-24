# Пункт 2: Сортировка обменом (пузырьком) - Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    arr = []
    
    print("Введите элементы массива:")
    for i in range(n):
        arr.append(int(input()))
    
    print("Исходный массив:", arr)
    
    bubble_sort(arr)
    
    print("Отсортированный массив:", arr)

# Пункт 5: Сортировка Шелла (Shell Sort)
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    arr = []
    
    print("Введите элементы массива:")
    for i in range(n):
        arr.append(int(input()))
    
    print("Исходный массив:", arr)
    
    shell_sort(arr)
    
    print("Отсортированный массив:", arr)

# Пункт 6: Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    arr = []
    
    print("Введите элементы массива:")
    for i in range(n):
        arr.append(int(input()))
    
    print("Исходный массив:", arr)
    
    sorted_array = quick_sort(arr)
    
    print("Отсортированный массив:", sorted_array)
# Пункт 8: Последовательный (линейный) поиск (Linear Search)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    arr = []
    
    print("Введите элементы массива:")
    for i in range(n):
        arr.append(int(input()))
    
    target = int(input("Введите элемент для поиска: "))
    
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")


# Пункт 11: Поиск Фибоначчи (Fibonacci Search)
def fibonacci_search(arr, target):
    n = len(arr)
    
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1
    
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1
    
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    arr = []
    
    print("Введите отсортированные элементы массива:")
    for i in range(n):
        arr.append(int(input()))
    
    target = int(input("Введите элемент для поиска: "))
    
    result = fibonacci_search(arr, target)
    
    if result != -1:
        print(f"Элемент найден на позиции: {result}")
    else:
        print("Элемент не найден")
