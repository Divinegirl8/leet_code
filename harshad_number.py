def check_divisibility(value, divisor):
    if value % divisor == 0:
        return divisor
    return -1


def sumOfTheDigitsOfHarshadNumber(x):
    convert_to_string = str(x)
    total = 0

    for value in convert_to_string:
        result = int(value)
        total += result

    return check_divisibility(x, total)


print(sumOfTheDigitsOfHarshadNumber(18))

