import random
import timeit
from tabulate import tabulate
from termcolor import colored
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.timsort import timsort

# Функція для імпорту функцій сортування в глобальний контекст, щоб уникнути проблем із областю видимості в timeit
def setup_module_imports():
    global insertion_sort, merge_sort, timsort
    from sorting_algorithms.insertion_sort import insertion_sort
    from sorting_algorithms.merge_sort import merge_sort
    from sorting_algorithms.timsort import timsort

# Функція для вимірювання часу виконання заданого алгоритму сортування на масиві
def time_sort_algorithm(algorithm_name, arr):
    import_statement = f"from sorting_algorithms.{algorithm_name} import {algorithm_name}"
    stmt = f"{algorithm_name}(list({arr}))"
    setup = import_statement + "\n" + "from __main__ import arr"
    return timeit.timeit(stmt, setup=setup, number=1)

def main():
    # Різні розміри масивів для тестування
    sizes = [1000, 5000, 10000]
    results = []
    headers = ["Algorithm", "1000", "5000", "10000"]

    # Генерація масивів випадкових чисел та вимірювання часу для кожного алгоритму
    for size in sizes:
        global arr
        arr = [random.randint(0, 10000) for _ in range(size)]
        result = []
        for sort_method in ["insertion_sort", "merge_sort", "timsort"]:
            time_taken = time_sort_algorithm(sort_method, arr)
            result.append(f"{time_taken:.5f} sec")
        results.append(result)

    # Формування та вивід таблиці результатів з кольоровим форматуванням
    table = []
    for i, method in enumerate(["Insertion Sort", "Merge Sort", "Timsort"]):
        # Виділення кольором для кращого візуального сприйняття
        row = [colored(method, 'yellow', attrs=['bold'])] + [colored(r, 'cyan') for r in results[i]]
        table.append(row)

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
