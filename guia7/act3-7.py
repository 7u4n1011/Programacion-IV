def pares (n):
    if n == []:
        return []
    if n[0] % 2 == 0:
        return [n[0]] + pares(n[1:])
    return pares(n[1:])

print(pares([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))