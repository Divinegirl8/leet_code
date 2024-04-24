def sample(numbers: list):
    for index in range(len(numbers)):
        if numbers[index] % 2 == 0:
            numbers[index] = 0
        else:
            numbers[index] = 1
    return numbers


my_list = [2, 4, 1, 5, 9]

result = list(filter(lambda x: (x % 2 == 0), my_list))

print(result)
# def sample_lambda(numbers:list):
#     value = lambda numbers :
