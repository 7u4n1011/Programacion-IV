def pasar (n):
    if n == []:
        return "no hay nada aca hermanaso"
    else:
        return list(map(lambda x: -abs(x), n))

print("que numero agregas hermanaso maquina crack?")
entrada = eval(input())
print(pasar(entrada))