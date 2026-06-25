def pattern(row):
    if row == 0:
        return

    def print_nums(n):
        if n == 0:
            return
        print(n, end=" ")
        print_nums(n - 1)

    print_nums(row)
    print()

    pattern(row - 1)

pattern(5)