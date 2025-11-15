def add(a, b):
    """
    Add two numbers together.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : int or float
        The number to subtract from.
    b : int or float
        The number to subtract.

    Returns
    -------
    int or float
        The result of a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : int or float
        The numerator.
    b : int or float
        The denominator.

    Returns
    -------
    float
        The result of a / b.

    Raises
    ------
    ValueError
        If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Example usage
    print("Add:       ", add(5, 3))
    print("Subtract:  ", subtract(10, 4))
    print("Multiply:  ", multiply(6, 7))
    print("Divide:    ", divide(20, 5))
