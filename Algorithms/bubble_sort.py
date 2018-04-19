# Bubble sort algorithm


def bubble_sort(array):
    i, j = (0, 0)
    while i < len(array):
        while j < len(array) - 1:
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

            j += 1
        
        i += 1
        j = 0

    return array


array = [8, 5, 2, 35, 36, 4, 88, 55, 48]

result = bubble_sort(array)

for index, val in enumerate(result):
    print(str(index) + " : " + str(val))