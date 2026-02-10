def sum(a, b):
    return a + b

def devide(a, b):
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Строки делить нельзя")

    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multilpy(a, b):
    return a * b