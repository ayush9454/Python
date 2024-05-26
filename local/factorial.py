def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result  # Added return statement to return the result

def binomial_coefficient(n, r):
    if n < r:
        return 0
    else:
        # Fixed the calculation and added return statement
        return factorial(n) / (factorial(n - r) * factorial(r))

n = int(input("Enter a non-negative integer to calculate the factorial: "))

if n < 0:
    print("Factorial is not defined for negative number")
else:
    result = factorial(n)
    print(f"{n}! = {result}")

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = binomial_coefficient(n, r)
print(f"Binomial coefficient C({n}, {r}) = {result}")
