def solver(n, f, h, t):
    if (n == 0):
        return
    solver(n-1, f, t, h)
    print(f'Move {f} to {t}')
    solver(n-1, h, f, t)


# num of disks, from, helper, to
solver(3, "A", "B", "C")
