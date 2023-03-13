# Solving this exercise will be helpful in the first actual exercise
# (Exercise 1), so consider using this as an opportunity to warm up.
#
# Your task is the define a function that returns the so called
# factorial: for any non-negative integer n, the factorial is defined
# as 1 * 2 * ... * n. For example, factorial(5) = 1*2*3*4*5 = 120.
#
# Hint: the simplest way to compute the factorial is to use a
# recursive function, or in other words, a function that calls
# itself as in
#     factorial(n) = n * factorial(n-1)
# The recursion should terminate at factorial(0) = 1 so that we
# don't create an infinite loop.
def factorial(n):
    if n == 0:
        return 1
    else:
        x = n * factorial(n-1)
        print(x)
        return x


print(factorial(6))  # this should print 720


def my_factorial(n):
    if n == 0:
        return 1
    else:
        tmp = range(1, n + 1)
        num = tmp[0]
        for i in tmp:
            num *= i
        return num

print(my_factorial(6))