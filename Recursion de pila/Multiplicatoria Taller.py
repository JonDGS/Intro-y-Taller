def sumatoria(n):
    if isinstance(n, int) and (n > 0):
        return suma(n)
    else:
        return "Error"

def suma(n):
    if n == 0:
        return 1
    else:
        return ((3*n) - 2) * suma(n-1)

