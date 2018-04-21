from random import sample

'''
This sort runtime is in between O(n) and O(n^2). It is O(n) if the list is already sorted and it is O(n^2) if the list 
is sorted in descending order. This algorithm breaks the list into two separate sections. A sorted section and a 
non-sorted section. Initially the algorithm considers the first element of the list to be sorted and the remainder of 
the list to be unsorted. It then checks the first element in the unsorted list and determines where in the sorted list 
it should be placed and puts it in that position. It then continues this action until the list is fully sorted.
'''

def insertion_sort(data):
    position = 1
    while position < len(data):
        tracker = position - 1
        current_data = data[position]
        while tracker >= 0:
            if current_data < data[tracker]:
                data[tracker+1] = data[tracker]
                data[tracker] = current_data
            tracker -= 1
        position += 1

    return data


if __name__ == '__main__':
    unsorted_list = sample(range(1, 1000), 50)
    print(unsorted_list)
    print(insertion_sort(unsorted_list))
