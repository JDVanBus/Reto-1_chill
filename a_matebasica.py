print("Hola mundo")

def matebasica(x: float, y: float, operacion: str):
    """Realiza una operación matemática básica entre dos números. Operaciones 
    permitidas: suma, resta, multiplicacion y divición"""
    x=float(x)
    y=float(y)  
    if operacion == "+":
        return x + y
    elif operacion == "-":
        return x - y
    elif operacion == "*":
        return x * y
    elif operacion == "/":
        if y != 0:
            return x / y
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"
    
x=matebasica(input("Ingrese el primer número: "), input("Ingrese el segundo número: "), input("Ingrese la operación (+, -, *, /): "))
print("El resultado es: ", x)
