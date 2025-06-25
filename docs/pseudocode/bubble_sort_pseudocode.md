# Bubble Sort Pseudocode

```
procedure bubbleSort(A : list of items)
    n = length(A)
    for i = 0 to n-1 do
        swapped = false
        for j = 0 to n-i-2 do
            if A[j] > A[j+1] then
                swap(A[j], A[j+1])
                swapped = true
            end if
        end for
        if not swapped then
            break
        end if
    end for
end procedure 