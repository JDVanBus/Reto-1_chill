def analisa_primos(numero:int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    input_num = input("Ingrese números separados por comas para verificar si son primos: ")
    lista_entrada = [int(num.strip()) for num in input_num.split(",")] #La entrada que es un string, se seprara por las comas y se cra una lista, en esta lista se eliminan los espacios y se convierten a enteros.
    lista_salida = []
    for num in lista_entrada:
        if analisa_primos(num):
            lista_salida.append(num)
    print("Los números primos ingresados son: ", lista_salida)

if __name__ == "__main__":
    main()  