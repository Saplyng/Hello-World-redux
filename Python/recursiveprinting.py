
def recursion(n):
    if n >= 1:
        recursion(n - 1)
        print(n)


recursion(42)
