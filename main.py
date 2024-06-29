# Programa para calcular el área de un círculo

import math


def calcular_area(radio):
    """
    Función para calcular el área de un círculo dado su radio.

    Args:
        radio (float): Radio del círculo.

    Returns:
        float: Área calculada del círculo.
    """
    area = math.pi * radio ** 2
    return area


# Ejemplo de uso:
radio = 5.0
area_del_circulo = calcular_area(radio)
print(f'El área del círculo con radio {radio} es: {area_del_circulo}')