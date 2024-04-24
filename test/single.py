
inf = 'abc', 'xyz'


def remove_last_index(words):
    new_list = []
    for word in range(len(words)):
        val = words[word]
        new_list.append(val[0:2])

    return new_list


def append_strings(words):
    value = remove_last_index(words)
    return f'{value[1] + inf[0][2::]} {value[0] + inf[1][2::]}'


print(append_strings(inf))

