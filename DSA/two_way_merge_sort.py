def mergeSort(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = j = k = 0
    arr3 = [0] * (m + n)

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    while i < m:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < n:
        arr3[k] = arr2[j]
        j += 1
        k += 1
    return arr3

print(mergeSort([1, 3, 5], [2, 4, 6]))
    