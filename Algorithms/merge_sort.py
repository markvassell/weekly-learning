from random import sample


def merge_sort(data):
    if len(data) <= 1:
        return data

    first_half = data[0:((len(data))//2)]
    second_half = data[((len(data))//2):len(data)]

    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return merge(first_half, second_half)


def merge(left_side, right_side):
    result = []

    while len(left_side) > 0 and len(right_side) > 0:
        if left_side[0] > right_side[0]:
            result.append(right_side[0])
            right_side = right_side[1:]
        else:
            result.append(left_side[0])
            left_side = left_side[1:]

    while len(left_side) > 0:
        result.append(left_side[0])
        left_side = left_side[1:]

    while len(right_side) > 0:
        result.append(right_side[0])
        right_side = right_side[1:]

    return result


if __name__ == '__main__':
    unsorted_list = sample(range(1, 1000), 10)
    print(unsorted_list)
    print(merge_sort(unsorted_list))

