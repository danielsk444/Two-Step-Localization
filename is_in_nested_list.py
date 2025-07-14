def is_in_nested_list(arr, x):
    return any(x in sublist for sublist in arr)
