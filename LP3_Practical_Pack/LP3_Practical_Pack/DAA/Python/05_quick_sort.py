"""Practical 5: Deterministic and randomized Quick Sort."""
import random
def partition(a, low, high):
    """Partition a[low:high+1] around the final element as pivot."""
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1
def quick_sort(a, low, high, randomized=False):
    """Sort list a in place between indices low and high, inclusive."""
    if low < high:
        if randomized:
            pivot_index = random.randint(low, high)
            a[pivot_index], a[high] = a[high], a[pivot_index]
        pivot_index = partition(a, low, high)
        quick_sort(a, low, pivot_index - 1, randomized)
        quick_sort(a, pivot_index + 1, high, randomized)
def main():
    try:
        values = list(map(int, input("Enter numbers separated by spaces: ").split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    deterministic = values.copy()
    randomized_values = values.copy()
    quick_sort(deterministic, 0, len(deterministic) - 1)
    quick_sort(randomized_values, 0, len(randomized_values) - 1, randomized=True)
    print("Deterministic Quick Sort:", deterministic)
    print("Randomized Quick Sort:   ", randomized_values)
    print("Best/average time: O(n log n); worst-case time: O(n^2).")
    print("Random pivot selection reduces the chance of consistently poor pivots.")
if __name__ == "__main__":
    main()
