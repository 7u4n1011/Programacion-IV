def multi (n):
    if n == []:
        return 1
    return n[0] * multi (n[1:])

print (multi([5,6,7]))