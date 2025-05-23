def print_fib(num, a=0, b=1, current=0):
    if current == 0:
        print(a, end=' ')
    if current < num:
        if current > 0:
            print(b, end=' ')  # Changed to print the current Fibonacci number (b) instead of a+b
        print_fib(num, b, a + b, current + 1)


# Example usage:
print_fib(99)

# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# def fib_sequence(n):
#     for i in range(n + 1):
#         print(fib(i), end=' ')
#     print()  # For newline after printing the sequence
#
#
# print(fib_sequence(10))
