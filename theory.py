import numpy as np


def calculate_function(data: dict) -> dict:
    resistance_coefficient = data['resistance_coefficient'] + (1 / 1e7)
    mass = data['mass']
    g = data['g']
    velocity_x = data['velocity_x']
    velocity_y = data['velocity_y']
    velocity = np.sqrt(velocity_x ** 2 + velocity_y ** 2)
    alpha = resistance_coefficient / mass
    k = resistance_coefficient / (g * mass)
    theta = np.arctan(velocity_y / velocity_x)

    def y_function_v(x: float) -> float:
        return g * np.log(((velocity_x / alpha) - x) * alpha / velocity_x) / (alpha ** 2) + (g + alpha * velocity_y) * (
                1 - ((velocity_x / alpha) - x) * alpha / velocity_x) / (alpha ** 2)

    def y_function_square_v(x: float) -> float:
        return x * np.tan(theta) + (x / (2 * k * velocity ** 2 * np.cos(theta))) - (
                    1 / (4 * k ** 2 * g * velocity ** 2)) * (np.exp(2 * k * g * x / np.cos(theta)) - 1)

    return {"v": y_function_v, "square_v": y_function_square_v}
