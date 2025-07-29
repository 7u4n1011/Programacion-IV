def alturas (n):
    if n == []:
        return 0
    if n[0] < 150:
        return 1 + alturas(n[1:])
    else:
        return alturas(n[1:])

print(alturas([143,140,154,160,170,180]))