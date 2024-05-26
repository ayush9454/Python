# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return  n* fact(n-1)

# a=int(input("whose factorial you want "))

# print(fact(a))
def fibonacci(n):
    fib_series = [0, 1]  # Initialize the series with first two elements
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]  # Generate next Fibonacci number
        fib_series.append(next_num)
    return fib_series

# Example usage:
n = 10  # Number of Fibonacci numbers to generate
fib_sequence = fibonacci(n)
print("Fibonacci series of length", n, ":", fib_sequence)
