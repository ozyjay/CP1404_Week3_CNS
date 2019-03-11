import string


def letter_count(text):
    tally = 0
    for letter in text:
        if letter in string.ascii_lowercase:
            tally += 1
    return tally


count = letter_count("hello world")
print("expected: 10, actual: ", count)
count = letter_count("1234$%$##%")
print("expected: 0, actual:", count)
count = letter_count("Demo1234")
print("expected: 4, actual: ", count)