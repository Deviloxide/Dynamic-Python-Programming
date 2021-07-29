# Tail Recursion
def func(string, n):
    if n > 0:
        print(string, "called func with n =", n)
        func("func", n - 1)


def main():
    func("main", 7)


main()
