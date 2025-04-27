def es_palindromo(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]

def es_palindromo2(texto):
    
    texto = texto.lower().replace(" ", "")
    print(texto)
    j = len(texto)-1
    for i in texto:
     
     if (i != texto[j]):
        print(f"{i} y {texto[j]}")
        return False
     j=j-1
     
    return True    
        

print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False
print(es_palindromo2("Anita lava la tina"))
