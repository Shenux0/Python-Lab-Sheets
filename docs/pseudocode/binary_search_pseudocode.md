# Binary Search Pseudocode (Recursive)

```
procedure binarySearch(A : sorted list of items, low, high, x)
    if high >= low then
        mid = low + (high - low) / 2
        if A[mid] == x then
            return mid
        else if A[mid] > x then
            return binarySearch(A, low, mid - 1, x)
        else
            return binarySearch(A, mid + 1, high, x)
        end if
    else
        return -1
    end if
end procedure 