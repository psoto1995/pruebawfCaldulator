def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


if __name__ == "__main__":
    print("=== Calculadora Básica ===")
    
    # Ejemplo de uso interactivo o predefinido
    # (Opcional para tu caso; puedes manejar entradas de usuario si lo deseas)
    
    a, b = 10, 2
    print(f"{a} + {b} = {sumar(a, b)}")
    print(f"{a} - {b} = {restar(a, b)}")
    print(f"{a} x {b} = {multiplicar(a, b)}")
    print(f"{a} / {b} = {dividir(a, b)}")
