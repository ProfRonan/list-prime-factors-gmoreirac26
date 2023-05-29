"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    
    prime_factors = []
    for i in range(2, number + 1):
        if is_prime(i):
            while number % i == 0:
                prime_factors.append(i)
                number //= i
    return prime_factors
