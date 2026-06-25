def pattern3(row, n):
    if row > n:
        return
    def spaces(s):
        if s == 0:
            return
        print("  ", end="")
        spaces(s - 1)
    def stars(st):
        if st == 0:
            return
        print("* ", end="")
        stars(st - 1)
    spaces(row - 1)
    stars(n - row + 1)
    print()
    pattern3(row + 1, n)
n = 5
pattern3(1, n)