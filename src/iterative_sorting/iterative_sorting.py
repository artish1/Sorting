# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # find next smallest element
        # (hint, can do in 3 loc)
        for n in range(cur_index, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n

        # Swap if NOT sorted
        if not smallest_index == cur_index:
            temp = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]
            arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    max_array_length = len(arr)
    for i in range(0, max_array_length):

        for lhs_index in range(0, max_array_length - i):
            rhs_index = lhs_index + 1
            if rhs_index < max_array_length:
                if arr[lhs_index] > arr[rhs_index]:
                    # Swap
                    temp = arr[lhs_index]
                    arr[lhs_index] = arr[rhs_index]
                    arr[rhs_index] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
