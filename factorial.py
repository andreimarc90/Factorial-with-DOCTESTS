MAX_NUM = 4

def main():
    for i in range (MAX_NUM):
        print(i, factorial(i))

def factorial(n):
    """
    Doctests:
    >>> factorial(3)
    6
    >>> factorial(1)
    1
    >>> factorial(0)
    1

    DOCTEST COMMAND: python3 -m doctest factorial.py -v
    """

    result = 1
    for i in range (1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    main()
