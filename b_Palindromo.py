def palindromo():
    """Esta función verifica si una palabra o frase es un palíndromo, es decir,
      si se lee igual de izquierda a derecha que de derecha a izquierda.
    """
    palabra = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
    palabra = palabra.replace(" ", "").lower() #elimina espacios y convierte a minúsculas
    return palabra == palabra[::-1] #compara la palabra con su reverso

test=palindromo()
if test==True:
    print("Es un palíndromo.")
else:    print("No es un palíndromo.")
