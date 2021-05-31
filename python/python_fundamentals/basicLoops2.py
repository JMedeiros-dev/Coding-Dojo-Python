# 1 Biggie Size
list = [-1, 3, 5, -5]


def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    print(list)


print(biggie_size(list))

# 2 Count Positives

list = [-1, 1, 1, 1]


def count_positives(list):
    sum = 0
    for i in range(len(list)):
        if list[i] > 0:
            sum = sum + 1
    list.append(sum)
    return list


print(count_positives(list))

# 3 Sum Total
list = [1, 2, 3, 4]


def sum_total(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


print(sum_total(list))

# 4 Average
list = [1, 2, 3, 4]


def average(list):
    sum = 0
    avg = 0
    for i in list:
        sum = sum + i
    avg = sum / len(list)
    return avg


print(average(list))

# 5 Length
list = [37, 2, 1, -9]


def length(list):
    return len(list)


print(length(list))

# 6 Minimum
list = [37, 2, 1, -9]


def minimum(list):
    if list == []:
        return False
    else:
        min = list[0]
        for i in list:
            if min > i:
                min = i
    return min


print(minimum(list))

# 7 Maximum
list = [37, 2, 1, -9]


def maximum(list):
    if list == []:
        return False
    else:
        max = list[0]
        for i in list:
            if max < i:
                max = i
    return max


print(maximum(list))

# 8 Ultimate Analysis
list = [37, 2, 1, -9]


def ultimate_analysis(list):
    sum = 0
    avg = 0
    min = 0
    max = 0

    for i in list:
        if min > i:
            min = i
        if max < i:
            max = i
        sum = sum + i
        avg = sum / len(list)
    new_dict = {'sumTotal': sum, 'average': avg,
                'minimum': min, 'maximum': max, 'length': len(list)}
    return new_dict


print(ultimate_analysis(list))

# 9 Reverse List
list = [37, 2, 1, -9]


def reverse_list(list):
    list.reverse()
    return list


print(reverse_list(list))
