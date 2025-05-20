def palindromo():
    print("Ingrese una palabra para corroborar si es palindromo...")
    word = input("").lower().replace(" ", "")
    palabra = list(word)
    
    for i in range (len(palabra)//2):
        if palabra[i] != palabra[-(i + 1)]:
            print("NO ES PALINDROMO, NEGRO INDIGENA")
            return False
        
    print("ES PALINDROMOOOOOOOOOOOOOOOO!!!!!")
    return True
        
palindromo()