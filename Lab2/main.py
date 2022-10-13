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

"""
      2. Write a function that receives a list of numbers 
         and returns a list of the prime numbers found in it.
"""


def prime_numbers(number):

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number, end=" ")


def list_of_numbers(list):
    new_list = []

    for i in list:
        prime_numbers(i)

    return new_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_numbers(list)

"""
      3. Write a function that receives as parameters two lists a and b and returns:
         (a intersected with b, a reunited with b, a - b, b - a)
         
         
"""