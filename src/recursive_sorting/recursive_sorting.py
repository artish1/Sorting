# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # Seperate lists into 1 length arrays first
    length = len(arr)
    if length != 1:
        middle = length // 2
        split_arr1 = arr[:middle]
        split_arr2 = arr[middle:]
        merge_sort(split_arr1)
        merge_sort(split_arr2)

        # Use merge helper function to join the 2 arrays in a sorted way.
        merge(split_arr1, split_arr2)

    return arr


merge_sort([3, 2, 4, 5, 6, 7, 8, 1, 1])

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
