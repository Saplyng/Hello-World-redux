def recursivelist(rl):
    if not rl:
        return 0

    return rl[0] + recursivelist(rl[1:])


somelist = [1, 4, 71, 3, 2, 19]
print(recursivelist(somelist))
