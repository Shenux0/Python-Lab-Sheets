def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
        print(f"Pass {i+1}: Smallest element found is {arr[i]} at index {i}. Array: {arr}")
    metrics = {
        "comparisons": comparisons,
        "swaps": swaps
    }
    return arr, metrics

def main():
    print("--- Selection Sort ---")
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
    print("\nStarting Selection Sort...")
    sorted_array, metrics = selection_sort(numbers.copy())
    print("\nSorting finished.")
    print("\nSorted array:")
    print(sorted_array)
    print("\nPerformance Metrics:")
    print(f"- Comparisons: {metrics['comparisons']}")
    print(f"- Swaps: {metrics['swaps']}")

if __name__ == "__main__":
    main() 