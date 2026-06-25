def pyramid(row, n):
    if row > n:
        return
    def spaces(s):
        if s == 0:
            return
        print(" ", end="")
        spaces(s - 1)
    def stars(st):
        if st == 0:
            return
        print("* ", end="")
        stars(st - 1)git --version
    spaces(n - row)
    stars(2 * row - 1)
    print()
    pyramid(row + 1, n)
n = 3
pyramid(1, n)