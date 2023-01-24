from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def Calculate_Square_Root(number):
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number >= 0:
        answer = Calculate_Square_Root(your_number)
        return print(f"Мы вычислили квадратный корень из "
                     f"введённого вами числа. Это будет: {answer}")
    

print(message)
calc(25.5)
