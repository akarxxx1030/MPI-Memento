def fibonacci(n):
    if n <= 1:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)
fibonacci(4)
