
# 4 вариант 
# 1. Построить бинарное дерево из элементов: {15, 7, 20, 3, 10, 18, 25}. 
# 2. Найти элемент со значением 7, удалить элемент со значением 18. 
# 3. Реализовать сортировку на куче для массива: [15, 7, 20, 3, 10, 18, 25]. 

from binarytree import build

# Построение бинарного дерева #

# Элементы дерева (в порядке уровня, слева направо)
elements = [15, 7, 20, 3, 10, 18, 25]

# Построение дерева
binary_tree = build(elements)

# Вывод дерева
print("Бинарное дерево:")
print(binary_tree)

# Поиск элемента (вручную, так как в binarytree нет встроенного поиска)
def search_node(root, value):
    if root is None:
        return None
    if root.value == value:
        return root
    left_search = search_node(root.left, value)
    if left_search is not None:
        return left_search
    return search_node(root.right, value)

# Поиск элемента 7
node_7 = search_node(binary_tree, 7)
print("\nНайден элемент 7:", node_7.value if node_7 else "Не найден")

# Удаление элемента (вручную, так как binarytree не поддерживает удаление)
# Для этого построим новое дерево без 18
elements_without_18 = [15, 7, 20, 3, 10, None, 25]  # None вместо 18
tree_without_18 = build(elements_without_18)

print("\nДерево после удаления 18:")
print(tree_without_18)

# Сортировка на куче #

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Пример использования
arr = [15, 7, 20, 3, 10, 18, 25]
heapsort(arr)
print("Отсортированный массив:", arr)