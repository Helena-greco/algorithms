def is_anagram(first_string, second_string):
    first = list(first_string.lower())
    second = list(second_string.lower())

    for word in first:
        if word in second:
            second.remove(word)

    if not first_string or not second_string:
        return False

    if len(second) == 0:
        return True

    else:
        return False

# print(is_anagram(cat, act))
