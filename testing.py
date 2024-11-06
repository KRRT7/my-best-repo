from __future__ import annotations
import math


class Polynomial:
    """
    Implements polynomial logic.
    Don't use this for anything other than implementing AKS.
    """

    def __init__(self, coefficients: list[int]):
        self.coefficients = coefficients

        self.degree = len(coefficients) - 1

    def multiply(self, other: Polynomial, r: int, modulus: int) -> Polynomial:
        """
        Calculates multiplication of the polynomial over the polynomial ring `S = (Z/nZ)[X]/(X^r - 1)`
        """
        coefficients = [0] * (self.degree + other.degree + 1)
        for degree, coefficient in enumerate(self.coefficients):
            if coefficient == 0:
                continue

            for other_degree, other_coefficient in enumerate(other.coefficients):
                """
                Implementation detail:

                Here, you don't need to calculate the polynomial remainder of `self` modulo `X^r - 1`, as you can substitute `X^r` to `1` and reduce the degree modulo `r`.
                """
                deg = (degree + other_degree) % r  # reducing polynomial modulo X^r - 1
                coefficients[deg] += coefficient * other_coefficient

                coefficients[deg] %= modulus  # reducing coefficients modulo n

        return Polynomial(coefficients)

    def __add__(self, other: Polynomial):
        return Polynomial(
            list(
                map(
                    lambda a: a[0] + a[1],
                    zip(self.coefficients, other.coefficients),
                )
            )
        )

    def __sub__(self, other: Polynomial):
        return Polynomial(
            list(
                map(
                    lambda a: a[0] - a[1],
                    zip(self.coefficients, other.coefficients),
                )
            )
        )

    def __mod__(self, other: int) -> Polynomial:
        return Polynomial(list(map(lambda a: a % other, self.coefficients)))

    def increase_degree(self, m: int) -> Polynomial:
        """
        Increases the degree of the polynomial by `m`
        """
        coefficients = [0] * (self.degree + m + 1)
        for i in range(self.degree + m, 0, -1):
            if i < m:
                coefficients[i] = 0
            else:
                coefficients[i] = self.coefficients[i - m]

        return Polynomial(coefficients)

    def multiply_no_reduce(self, other: Polynomial) -> Polynomial:
        coefficients = [0] * (self.degree + other.degree + 1)
        for degree, coefficient in enumerate(self.coefficients):
            if coefficient == 0:
                continue

            for other_degree, other_coefficient in enumerate(other.coefficients):
                deg = degree + other_degree
                coefficients[deg] += coefficient * other_coefficient

        return Polynomial(coefficients)

    def karatsuba(self, other: Polynomial, test: bool = False) -> Polynomial:
        """
        Calculates the polynomial multiplication using the Karatsuba algorithm
        """
        m = min(self.degree, other.degree) // 2

        if m <= 2:
            return self.multiply_no_reduce(other)

        low1 = Polynomial(self.coefficients[:m])
        high1 = Polynomial(self.coefficients[m:])

        low2 = Polynomial(other.coefficients[:m])
        high2 = Polynomial(other.coefficients[m:])
        if high2 == Polynomial([]):
            high2 = Polynomial([1])

        z0 = low1.karatsuba(low2)
        z2 = high1.karatsuba(high2)
        z3 = (low1 + high1).karatsuba(low2 + high2)

        z1 = z3 - z2 - z0

        if test:
            print(f"z0: {z0}")
            print(f"z2: {z2}")
            print(f"z3: {z3}")
            print(f"z1: {z1}")

            print()

            print(f"low1: {low1}")
            print(f"high1: {high1}")
            print(f"low2: {low2}")
            print(f"high2: {high2}")

        result = z2.increase_degree(m * 2) + z1.increase_degree(m) + z0
        return result

    def pow2(self, exponent: int) -> Polynomial:
        """
        Calculates the polynomial to the power of `exponent` in the polynomial ring `S = (Z/nZ)[X]/(X^r - 1)`
        """
        if exponent == 0:
            return Polynomial([1])
        elif exponent == 1:
            return self

        base = self
        output = Polynomial([1])
        while exponent > 0:  # exponentiation by squaring
            if exponent % 2 == 1:
                output = output.multiply_no_reduce(base)  # o * s mod (x^r - 1, n)

            base = base.multiply_no_reduce(base)  # s * s mod (x^r - 1, n)
            exponent //= 2

        return output

    def pow(self, exponent: int) -> Polynomial:
        """
        Calculates the polynomial to the power of `exponent` in the polynomial ring `S = (Z/nZ)[X]/(X^r - 1)`
        """
        if exponent == 0:
            return Polynomial([1])
        elif exponent == 1:
            return self

        output = Polynomial([1])
        for _ in range(exponent):
            output = output.karatsuba(self)

        return output

    def reduce(self, degree: int) -> Polynomial:
        """
        Reduces the polynomial modulo X^degree - 1
        """
        if self.degree < degree:
            return self

        coefficients = [0] * degree
        for index, coefficient in enumerate(self.coefficients):
            coefficients[index % degree] += coefficient

        return Polynomial(coefficients)

    def __eq__(self, other: Polynomial) -> bool:  # pyright: ignore[reportImplicitOverride, reportIncompatibleMethodOverride]
        return self.coefficients == other.coefficients

    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        def format_coefficient(pair: tuple[int, int]) -> str:
            co = ""

            if pair[1] > 1 or pair[0] == 0 and pair[1] == 1:
                co += f"{pair[1]}"
            if pair[0] != 0:
                co += f"x^{pair[0]}"

            return co

        return " + ".join(
            filter(
                lambda a: a != "",
                map(
                    format_coefficient,
                    filter(
                        lambda a: a[1] != 0,
                        reversed(list(enumerate(self.coefficients))),
                    ),
                ),
            )
        )


def phi(n: int):
    """
    Calculates Euler's totient function (or number of coprimes less than n) of n.
    """

    totient = n
    for i in range(2, n):
        if n % i == 0:
            totient *= i - 1
            totient /= i
        while n % i == 0:
            n //= i

    return totient


def is_power(n: int, base: int) -> bool:
    for exponent in range(1, n):
        if base**exponent == n:
            return True
        elif base**exponent > n:
            return False

    return False


def check_power(n: int) -> bool:
    """
    Checks if n is a power of a number.
    """
    for b in range(2, int(math.log2(n)) + 1):
        if is_power(n, b):
            return True

    return False


def find_r(n: int) -> int:
    """
    Finds the smallest r such that the multiplicative order of r is more than log2(n)^2.
    """
    maxK = int(math.log2(n) ** 2)

    nextR = True

    r = 1
    while nextR:
        r += 1
        nextR = False
        k = 1
        while k <= maxK and nextR is False:
            k += 1
            nextR = pow(n, k, r) in [1, 0]

    return r


def aks(n: int) -> bool:
    """
    Checks if n is a prime number.
    """
    if n < 31:
        return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if check_power(n):
        return False

    r = find_r(n)

    if math.gcd(n, r) != 1:
        return False

    if n <= r:
        return True

    for a in range(2, r):
        if n % a == 0:
            return False

    for a in range(2, int(math.sqrt(phi(r)) * math.log2(n))):
        poly = Polynomial([a, 1])

        if poly.pow(n) != Polynomial([a] + [0] * (n - 1) + [1]).reduce(r):
            return False

    return True
