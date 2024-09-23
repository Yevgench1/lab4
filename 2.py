import math  

def calculate_U(x, y):
  
    try:
        U = x * math.log10(y) + 1 / (x**2 + y**2 + 0.3) - math.exp(6 * x - y)
        return U 
    except ValueError:
        return "Помилка: введені невірні значення "

x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

result = calculate_U(x, y)
print("U =", result)
