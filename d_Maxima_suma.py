def max_suma(lista_a:list) ->float:
    suma_max = 0
    for i in range(len(lista_a)):
        for j in range(i + 1, len(lista_a)):
            suma_actual = lista_a[i] + lista_a[j]
            if suma_actual > suma_max:
                suma_max = suma_actual
    return suma_max


def main():
    lista_entrada = [float(num.strip()) for num in input("Ingrese números separados por comas para calcular la suma máxima: ").split(",")]
    resultado = max_suma(lista_entrada) 
    print("La suma máxima de los números ingresados es: ", resultado)

if __name__ == "__main__":    main()
