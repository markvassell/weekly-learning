from random import sample


def find_min(data):
    current_min, current_position = [data[0], 0]

    for index, value in enumerate(data[1:]):
        if value < current_min:
            current_min = value
            current_position = index + 1

    return current_min, current_position


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
