
def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)

    total = 0
    for digit in digits:
        total += int(digit) ** power

    return total == number
