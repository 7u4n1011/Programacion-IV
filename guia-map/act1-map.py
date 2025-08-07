def duplicar (n):
    if n == []:
        return "no hay nada hermano"
    else:
        return list(map(lambda x: x * 2, n))

print("que numero agregas hermanaso maquina crack?")
entrada = eval(input())
print(duplicar(entrada))