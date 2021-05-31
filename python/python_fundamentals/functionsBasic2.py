# 1 Countdown
def countdown(num):

    newlist = []
    for i in range(num, -1, -1):
        newlist.append(i)
    return newlist


# 2 Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])


list = [1, 2]
print(print_and_return(list))

# 3 First Plus Length


def first_plus_length(list):
    return list[0] + len(list)


list = [1, 2, 3, 4, 5]
print(first_plus_length(list))

# 4 Values Greater than Second
list = [5, 2, 3, 2, 1, 4]


def values_greater_than_second(list):
    sum = 0
    new_list = []
    for i in range(len(list)):
        if list[i] > list[1]:
            new_list.append(list[i])
            sum = sum + 1
    print(sum)
    return new_list


print(values_greater_than_second(list))

# 5 This Length, That Value


def length_and_value(length, value):
    new_list = []
    for i in range(length):
        new_list.append(value)
    return new_list


print(length_and_value(6, 2))
