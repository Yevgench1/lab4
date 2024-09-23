import math

def f(x):
    try:
        value = math.tan(2*x) + math.cos(4*x - math.sqrt(x)) - 2/(math.pow(abs(x + 1) + 0.1, 1/3))
        return value
    except ValueError:
        return "Помилка: невірне значення x для кореня"

x = float(input("Введіть значення x: "))
result = f(x)
print("f(x) =", result)
