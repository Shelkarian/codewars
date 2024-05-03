def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True