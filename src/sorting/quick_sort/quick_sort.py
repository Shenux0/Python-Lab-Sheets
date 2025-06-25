def partition(arr, low, high, metrics):
    pivot = arr[high]
    i = low - 1
    print(f"\nPartitioning subarray from index {low} to {high}. Pivot: {pivot}")
    for j in range(low, high):
        metrics["comparisons"] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            metrics["swaps"] += 1
            print(f"  Swapped {arr[i]} and {arr[j]}. Array: {arr}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    metrics["swaps"] += 1
    print(f"  Placed pivot {pivot} at index {i+1}. Array: {arr}")
    return i + 1

def quick_sort_recursive(arr, low, high, metrics):
    metrics["recursive_calls"] += 1
    if low < high:
        pi = partition(arr, low, high, metrics)
        quick_sort_recursive(arr, low, pi - 1, metrics)
        quick_sort_recursive(arr, pi + 1, high, metrics)

def quick_sort(arr):
    metrics = {"swaps": 0, "comparisons": 0, "recursive_calls": 0}
    quick_sort_recursive(arr, 0, len(arr)-1, metrics)
    return arr, metrics

def main():
    print("--- Quick Sort ---")
    numbers = []
    while True:
        try:
            size = int(input("Enter the number of elements: "))
            if size > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"Please enter {size} numbers:")
    for i in range(size):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    print("\nOriginal array:")
    print(numbers)
    print("\nStarting Quick Sort...")
    sorted_array, metrics = quick_sort(numbers.copy())
    print("\nSorting finished.")
    print("\nSorted array:")
    print(sorted_array)
    print("\nPerformance Metrics:")
    print(f"- Swaps: {metrics['swaps']}")
    print(f"- Comparisons: {metrics['comparisons']}")
    print(f"- Recursive calls: {metrics['recursive_calls']}")

if __name__ == "__main__":
    main() 