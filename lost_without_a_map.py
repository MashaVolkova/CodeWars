def map_function(elem):
    return elem * 2


def maps(arr):
    new_array = list(map(map_function, arr))
    return new_array
