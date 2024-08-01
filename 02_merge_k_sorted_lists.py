import heapq
from tabulate import tabulate
from termcolor import colored

def visualize_merge_process(min_heap, result, column_width=10):
    # Створення таблиці з поточним станом купи та результатом
    heap_display = [colored(f"{item[0]:<{column_width}}", 'green') for item in min_heap]
    result_display = [colored(f"{item:<{column_width}}", 'blue') for item in result]
    
    # Вирівнювання таблиць за допомогою ширини стовпця
    formatted_heap = [x.ljust(column_width) for x in heap_display]
    formatted_result = [x.ljust(column_width) for x in result_display]

    # Вивід таблиці з поточним станом купи та результатом
    print(tabulate([formatted_heap, formatted_result], headers=["Heap", "Result"], tablefmt='fancy_grid'))

def merge_k_lists(lists):
    min_heap = []
    result = []

    # Створюємо мінімальну купу з першого елементу кожного списку
    for i in range(len(lists)):
        if lists[i]:  # перевірка, що список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    # Вивід початкового стану
    print("Initial State:")
    visualize_merge_process(min_heap, result)

    # Злиття списків
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        visualize_merge_process(min_heap, result)

        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
            print(f"After adding next element from list {list_idx}:")
            visualize_merge_process(min_heap, result)

    return result

def print_final_merged_list(merged_list):
    # Виведення фінального відсортованого списку
    print("Відсортований список:", merged_list)

# Приклад використання:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print_final_merged_list(merged_list)
