file = open("Sample.txt", "r").read()

def countChar(word, char):
    if len(word) <= 0:
        return 0
    elif word[0] == char:
        return 1 + countChar(word[1:], char)
    else:
        return countChar(word[1:], char)


def count_char(word, char):
    count = 0

    for let in range(0, len(word)):
        if word[let] == char:
            count += 1

    return count


# Result: 38
print(count_char(
    "It is a long established fact that a reader will be distracted by the readable content of a page when looking at "
    "its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, "
    "as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing "
    "packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' "
    "will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by "
    "accident, sometimes on purpose (injected humour and the like).",
    "a"))

# Result: 38
print(countChar(
    "It is a long established fact that a reader will be distracted by the readable content of a page when looking at "
    "its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, "
    "as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing "
    "packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' "
    "will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by "
    "accident, sometimes on purpose (injected humour and the like).",
    "a"))

# Result: 5362
print(count_char(file, "a"))

# Result: RecursionError: maximum recursion depth exceeded while calling a Python object
print(countChar(file, "a"))
