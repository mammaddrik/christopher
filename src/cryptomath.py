def gcd(a:int, b:int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm
    
    Parameters:
    a(int): The first number.
    b(int): The second number.
    
    Returns:
    b(int): The Greatest Common Divisor (GCD) of two number.
    
    Example:
    >>> gcd(48,18)
    6
    """
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a: int, m: int)-> int:
    """
    Computes the modular multiplicative inverse of a under modulo m.

    Parameters:
    -----------
    a : int
        The integer for which the modular inverse is to be found.
    m : int
        The modulus.

    Returns:
    --------
    int or None:
        The modular multiplicative inverse of a modulo m if it exists, otherwise None.
        The inverse exists only if gcd(a, m) == 1, meaning a and m are coprime.

    Examples:
    ---------
    >>> findModInverse(3, 11)
    4
    >>> findModInverse(10, 17)
    12
    >>> findModInverse(6, 9)  # No inverse exists since gcd(6, 9) != 1
    None
    """
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m