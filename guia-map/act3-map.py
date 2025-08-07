def grados (n):
    if n == []:
        return "no hay nada hermanoooooooooooooo"
    else:
        return list(map(lambda x: x * 9/5 + 32, n))

print("que grados queres cambiar hermanaso maquina crack?")
entrada = eval(input(""))
print(grados(entrada))