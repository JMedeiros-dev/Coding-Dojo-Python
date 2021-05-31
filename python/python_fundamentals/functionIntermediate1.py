import random


def randInt(min=" ", max=" "):
    if min == " " and max == " ":
        num = random.random() * 100
        return round(num)
    elif min == " " and max != " ":
        num = random.random() * max
        return round(num)
    elif min != " " and max == " ":
        num = random.random() * 100 + min
        if num > 100:
            num = 99
        return round(num)
    else:
        num = random.random() * max + min
        if num > max:
            num = max - 1
    return round(num)


print(randInt(min=60))
