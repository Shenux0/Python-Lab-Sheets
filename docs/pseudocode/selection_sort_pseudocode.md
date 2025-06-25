# Selection Sort Pseudocode

```
procedure selectionSort(A : list of items)
    n = length(A)
    for i = 0 to n-1 do
        min_idx = i
        for j = i+1 to n-1 do
            if A[j] < A[min_idx] then
                min_idx = j
            end if
        end for
        if min_idx != i then
            swap(A[i], A[min_idx])
        end if
    end for
end procedure 