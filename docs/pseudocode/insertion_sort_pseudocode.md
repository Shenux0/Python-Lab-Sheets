# Insertion Sort Pseudocode

```
procedure insertionSort(A : list of items)
    n = length(A)
    for i = 1 to n-1 do
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key do
            A[j+1] = A[j]
            j = j - 1
        end while
        A[j+1] = key
    end for
end procedure 