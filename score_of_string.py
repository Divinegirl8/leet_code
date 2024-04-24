def scoreOfString(s):
    total = 0
    for value in range(len(s)-1):
        result = ord(s[value]) - ord(s[value+1])
        if result < 0:
            result *= -1
        total += result

    return total


print(scoreOfString("hello"))
