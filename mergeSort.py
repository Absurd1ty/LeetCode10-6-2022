import random


def mergeSort(arr):
    # Recusion Algorithm. Base case is when there is 1 element or 0 in the array. Divide the array into two halves
    # with recursion
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0

        # Just basic comparisons for sorting.
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # the two endcases if there is 1 element left over to the left in right. ( if the array number of elemetns is odd)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

test_arr = [12,69,59,23,49,520,9,2,4,6,10,35, 1,3]
mergeSort(test_arr)
print_array(test_arr)
