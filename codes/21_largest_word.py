
def largest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    largest = words[0]

    for word in words:
        if len(word) > len(largest):
            largest = word

    return largest
