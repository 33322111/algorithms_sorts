import time
import matplotlib.pyplot as plt
from generate_data import generate_data
from merge_insertion_sort import merge_insertion_sort


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


def measure_time(sort_function, data, *args):
    start_time = time.time()
    sort_function(data, *args)
    end_time = time.time()
    return end_time - start_time


sizes = list(range(500, 4100, 100))
insertion_sort_thresholds = [5, 10, 20, 50]

for threshold in insertion_sort_thresholds:
    merge_sort_times = []
    merge_insertion_sort_times = []

    for size in sizes:
        random_data = generate_data(4000)[:size]
        reversed_data = generate_data(4000, reversed_order=True)[:size]
        almost_sorted_data = generate_data(4000, almost_sorted=True)[:size]

        merge_sort_time_random = measure_time(merge_sort, random_data.copy())
        merge_sort_time_reversed = measure_time(merge_sort, reversed_data.copy())
        merge_sort_time_almost_sorted = measure_time(merge_sort, almost_sorted_data.copy())
        merge_sort_times.append([merge_sort_time_random, merge_sort_time_reversed, merge_sort_time_almost_sorted])

        merge_insertion_sort_time_random = measure_time(merge_insertion_sort, random_data.copy(), threshold)
        merge_insertion_sort_time_reversed = measure_time(merge_insertion_sort, reversed_data.copy(), threshold)
        merge_insertion_sort_time_almost_sorted = measure_time(merge_insertion_sort, almost_sorted_data.copy(),
                                                               threshold)
        merge_insertion_sort_times.append([merge_insertion_sort_time_random, merge_insertion_sort_time_reversed,
                                           merge_insertion_sort_time_almost_sorted])

    labels = ['Random', 'Reversed', 'Almost Sorted']

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.plot(sizes, [time[0] for time in merge_sort_times], label='Merge Sort')
    plt.plot(sizes, [time[0] for time in merge_insertion_sort_times],
             label=f'Merge + Insertion Sort (Threshold={threshold})')
    plt.title(f'Sorting Random Arrays (Threshold={threshold})')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(sizes, [time[1] for time in merge_sort_times], label='Merge Sort')
    plt.plot(sizes, [time[1] for time in merge_insertion_sort_times],
             label=f'Merge + Insertion Sort (Threshold={threshold})')
    plt.title(f'Sorting Reversed Arrays (Threshold={threshold})')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.plot(sizes, [time[2] for time in merge_sort_times], label='Merge Sort')
    plt.plot(sizes, [time[2] for time in merge_insertion_sort_times],
             label=f'Merge + Insertion Sort (Threshold={threshold})')
    plt.title(f'Sorting Almost Sorted Arrays (Threshold={threshold})')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.tight_layout()
    plt.show()
