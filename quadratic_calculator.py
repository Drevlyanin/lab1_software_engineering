import math


def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c != 0:
                return "Рівняння не має розв'язків"
            return "Безліч розв'язків"

        return f"Лінійне рівняння: x = {-c / b:.4g}"

    D = b * b - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"D={D:g}; x1={x1:.4g}; x2={x2:.4g}"

    elif D == 0:
        x = -b / (2 * a)
        return f"D=0; x={x:.4g}"

    else:
        return f"D={D:g}; дійсних коренів немає"


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(solve(a, b, c))

except ValueError:
    print("Помилка: потрібно вводити числові значення")
