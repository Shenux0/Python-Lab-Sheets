def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm and tracks performance metrics.
    """
    comparisons = 0
    while_loop_executions = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Pass {i}: Key={key}, Array={arr}")
        while j >= 0:
            while_loop_executions += 1
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    metrics = {
        "comparisons": comparisons,
        "while_loop_executions": while_loop_executions
    }
    return arr, metrics

def main():
    print("--- Insertion Sort ---")
    while True:
        try:
            size = int(input("Enter the number of elements (10-20): "))
            if 10 <= size <= 20:
                break
            else:
                print("Please enter a number between 10 and 20.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    numbers = []
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
    print("\nStarting Insertion Sort...")
    sorted_array, metrics = insertion_sort(numbers.copy())
    print("\nSorting finished.")
    print("\nSorted array (Ascending Order):")
    print(sorted_array)
    print("\nPerformance Metrics:")
    print(f"- Comparisons: {metrics['comparisons']}")
    print(f"- While loop executions: {metrics['while_loop_executions']}")

if __name__ == "__main__":
    main() 