from random import sample


def quick_sort(array, start, end):
    new_array = list(array)
    if len(array) == 1:
        return array
    elif start < end:
        part = partition(new_array, start, end)
        quick_sort(new_array, start, part - 1)
        quick_sort(new_array, part + 1, end)

    return new_array


def partition(array, start, end):
    #  using the middle index as the pivot
    mid = ((end + start) // 2)
    #  print('Pivot: ', array[mid])
    #  moves the pivot to the end of the list
    swap(array, mid, end)
    i = start - 1
    j = start

    pivot = array[end]

    while j < end:
        if array[j] < pivot:
            i += 1
            swap(array, i, j)
        j += 1
    swap(array, i + 1, end)
    return i + 1


def swap(array, pos1, pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp


if __name__ == '__main__':
    data = sample(range(1, 1000), 5)
    print('Unsorted List: ', data)
    sorted_list = quick_sort(data, 0, len(data) - 1)
    print("Sorted List: ", sorted_list)
