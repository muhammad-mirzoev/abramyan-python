def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else "Ошибка"
    return "Неизвестная операция"


print(calculate(10, 5, "-"))
