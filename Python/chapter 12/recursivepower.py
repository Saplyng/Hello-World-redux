def recursivepower(n, p):
    if p == 0:
        return 1

    if p >= 1:
        return n * recursivepower(n, p - 1)


onepunchman = recursivepower(7, 7)
print(onepunchman)
