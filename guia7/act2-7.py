def invertir (n):
    if n == []:
        return []
    return invertir(n[1:]) + [n[0]]

print(invertir([1,2,3,4,5,6,7,8,9]))