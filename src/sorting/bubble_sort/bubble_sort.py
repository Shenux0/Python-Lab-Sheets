def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm and tracks performance metrics.
    """
    n = len(arr)
    swaps = 0
    comparisons = 0
    iterations = 0
    for i in range(n):
        iterations += 1
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        print(f"After pass {i+1}: {arr}")
        if not swapped:
            break
    metrics = {
        "swaps": swaps,
        "comparisons": comparisons,
        "iterations": iterations
    }
    return arr, metrics

def main():
    print("--- Bubble Sort ---")
    numbers = []
    print("Please enter 8 numbers:")
    for i in range(8):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    print("\nOriginal array:")
    print(numbers)
    print("\nStarting Bubble Sort...")
    sorted_array, metrics = bubble_sort(numbers.copy())
    print("\nSorting finished.")
    print("\nSorted array:")
    print(sorted_array)
    print("\nPerformance Metrics:")
    print(f"- Swaps: {metrics['swaps']}")
    print(f"- Comparisons: {metrics['comparisons']}")
    print(f"- Outer loop iterations: {metrics['iterations']}")

if __name__ == "__main__":
    main() 