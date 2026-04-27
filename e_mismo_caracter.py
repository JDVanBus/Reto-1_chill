def mismo_caracter(lista_a: list) -> list:
    lista_a=[palabra.strip() for palabra in lista_a] #Elimina los espacios en blanco al inicio y al final de cada palabra en la lista.
    for i in range(len(lista_a)):
        for j in range (i,len(lista_a)):
            if lista_a[i][].lower() == lista_a[j][0].lower(): #Compara el primer carácter de cada palabra, ignorando mayúsculas y minúsculas.
                return [lista_a[i], lista_a[j]] #Si encuentra dos palabras que comienzan con el mismo carácter, devuelve una lista con esas dos palabras.
            #en construccion, no se si tienen casos donde la primera palabra es difereten a todas, no se si influye que tengana diferetnes len. 