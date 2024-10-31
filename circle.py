import math


def AreaCircle(r):
    '''принимает r и возвращает квадрат r умноженный на значение хранящиеся в math.pi'''
    '''Пример вызова: AreaCircle(1) - вернет math.pi * 1 * 1. '''
    return math.pi * r * r


def PerimeterCircle(r):
    '''принимает r и возвращает r умноженное на значение хранящиеся в math.pi и умноженное на 2'''
    '''Пример вызова: PerimeterCircle(1) - вернет 2 * math.pi * 1. '''
    return 2 * math.pi * r