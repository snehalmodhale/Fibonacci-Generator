def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci_recursive(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Enter the number of Fibonacci numbers to generate: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = fibonacci_recursive(n)
    print(f"/nFibonacci Sequence: {fibonacci_sequence}")