def reverseWords(self, s):
    pass


def changeToArray(word: str) -> []:
    return word.split(" ")


def remove_extra_space(word: str) -> []:
    return word.replace("\\S{2,}", " ")


print(remove_extra_space("i am    3"))

