def fact (n):
    if n == 0:
        return 1
    return n * fact(n-1)

print("De que numero desea realizar el factorial?")
print(fact(int(input(""))))