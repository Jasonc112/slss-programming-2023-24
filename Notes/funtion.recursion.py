def factorial(num: int) -> int:
    """Returns the result of the number's
    factorial using recursiono
    
    Parmas:
        num - number we're calculating
        
    Returns:
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num - 1) * num
    
def fib(n: int) -> int:
    """Calculate and return the nth
    Fibonacci number."""

    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

print(``)