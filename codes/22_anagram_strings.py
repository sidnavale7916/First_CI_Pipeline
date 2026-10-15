
def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    return sorted(first) == sorted(second)
