def binary_search(array, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, start, mid+1)