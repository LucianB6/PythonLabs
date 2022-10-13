"""
      1. Write a function to return a list of the first n numbers in the Fibonacci string.
      n = 4
      0 1 1 2
      n = 6
      0 1 1 2 3 5
"""


def fibonacci(n):
    fibonacci_list = []
    f0 = 0
    f1 = 1

    if n <= 0:
        fibonacci_list.append(f0)

    else:
        fibonacci_list.append(f0)
        fibonacci_list.append(f1)

        for i in range(2, n):
            next_element = f0 + f1
            fibonacci_list.append(next_element)
            f0 = f1
            f1 = next_element
    return fibonacci_list


print(fibonacci(1))
