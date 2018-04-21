from random import sample

'''
This function is used to find the minimum value and its index from a list. This function initially sets the first value 
in the list as the minimum value and its index at the current index. The function loops through the remainder of the 
list, and checks if there is another value in the list that is smaller than the first value.  If there is then the the 
current min value and its index will get updated.
'''


def find_min(data):
    current_min, current_position = [data[0], 0]

    for index, value in enumerate(data[1:]):
        if value < current_min:
            current_min = value
            current_position = index + 1

    return current_min, current_position


'''
The selection sort algorithm dictates that the list being sorted must get separated into two sections, a sorted and an 
unsorted portion. To start off there are no elements in the sorted portion of the list and the original list is the 
unsorted section. The unsorted section of the list looped through and at each step the minimum value from the unsorted 
portion is appended to the sorted portion of the list. This concept is carried out until there are no more elements left
in the unsorted portion. The run-time of this algorithm is on average O(n^2). 
'''


def selection_sort(data):
    i = 0

    while i < len(data):
        temp_val = data[i]
        data[i], index = find_min(data[i:])
        data[index + i] = temp_val
        i += 1

    return data


if __name__ == '__main__':
    unordered_list = sample(range(1, 1000), 10)
    print(unordered_list)
    print(selection_sort(unordered_list))
