# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(lefthalf, righthalf, orig_array):
    i = j = k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            orig_array[k] = lefthalf[i]
            i = i + 1
        else:
            orig_array[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        orig_array[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        orig_array[k] = righthalf[j]
        j = j + 1
        k = k + 1
    return orig_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # Seperate lists into 1 length arrays first
    length = len(arr)
    if length > 1:
        middle = length // 2
        lefthalf = arr[:middle]
        righthalf = arr[middle:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # Use merge helper function to join the 2 arrays in a sorted way.
        arr = merge(lefthalf, righthalf, arr)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
