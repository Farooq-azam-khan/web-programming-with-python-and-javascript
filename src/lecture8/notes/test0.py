from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")
        
if __name__ == '__main__':
    test_prime(1, False)
    test_prime(2, True)
    test_prime(8, False)
    test_prime(11, True)
    test_prime(25, False)
    test_prime(28, False)