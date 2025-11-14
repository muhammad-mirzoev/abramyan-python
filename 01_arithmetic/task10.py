def all_ops(a, b):
    return {
        "sum": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b,
    }


print(all_ops(8, 2))
