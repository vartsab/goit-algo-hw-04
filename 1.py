import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_random_list(size):
    return random.sample(range(size * 10), size)

sizes = [100, 1000, 10000, 100000]
for size in sizes:
    data = generate_random_list(size)
    print(f"Testing with size: {size}")

    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
    print(f"Merge Sort: {merge_sort_time:.6f} seconds")

    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
    print(f"Insertion Sort: {insertion_sort_time:.6f} seconds")

    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=10)
    print(f"Timsort: {timsort_time:.6f} seconds")
    print()
