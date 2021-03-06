from random import sample


def insertion_sort(data):
    if len(data) == 1:
        return data
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
