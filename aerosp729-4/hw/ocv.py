import numpy as np


def OCV(Q, Q_max=5.080457832540185):
    coeffs = [
        -0.44934919,
        -0.07263436,
        0.03009002,
        -0.02263346,
        -0.24777699,
        -0.26923143,
        3.72029854,
    ]
    x = Q / Q_max
    result = 0.0
    for i in range(0, len(coeffs) - 1):
        result += (coeffs[i]) * (
            (2 * x - 1) ** (i + 1) - (2 * x * i * (1 - x)) / (2 * x - 1) ** (1 - i)
        )

    result += coeffs[len(coeffs) - 1] + (8.3145 * 298.15 / 96485.3321) * np.log(
        (1 - x) / x
    )
    return result
