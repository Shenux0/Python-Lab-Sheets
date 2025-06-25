def binary_search_recursive(arr, low, high, x, metrics):
    metrics["recursive_calls"] += 1
    if high >= low:
        mid = low + (high - low) // 2
        print(f"  Searching in subarray from index {low} to {high}. Middle is {mid}.")
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x, metrics)
        else:
            return binary_search_recursive(arr, mid + 1, high, x, metrics)
    else:
        return -1

def binary_search(arr, x):
    metrics = {"recursive_calls": 0}
    arr.sort()
    print(f"Array must be sorted for Binary Search: {arr}")
    result = binary_search_recursive(arr, 0, len(arr)-1, x, metrics)
    return result, metrics

def main():
    print("--- Binary Search ---")
    numbers = []
    while True:
        try:
            size = int(input("Enter the number of elements for the array: "))
            if size > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"Please enter {size} numbers (they will be sorted for the search):")
    for i in range(size):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    while True:
        try:
            search_element = int(input("\nEnter the element to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("\nStarting Binary Search...")
    result, metrics = binary_search(numbers, search_element)
    print(f"\nSearching finished in {metrics['recursive_calls']} recursive calls.")
    if result != -1:
        print(f"\nSuccess! Element {search_element} found at index {result}.")
    else:
        print(f"\nFailure. Element {search_element} not found in the array.")

if __name__ == "__main__":
    main() 