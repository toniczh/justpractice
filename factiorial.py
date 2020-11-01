def factorial(n):
    # stop at 1
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
# Test
print(factorial(5))

