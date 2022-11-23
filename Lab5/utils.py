"""
1)
a)
 Write a module named utils.py that contains one function called process_item.
 The function will have one parameter, x, and will return the least prime number greater than x.
 When run, the module will request an input from the user, convert it to a number and it will
 display the output of the process_item function.
"""


def prime_numer(x):
    boolean = False
    if x <= 0:
        return False
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                boolean = True
                break
    if boolean:
        return False
    else:
        return True


def process_item(x):
    x += 1
    while not prime_numer(x):
        x += 1
        prime_numer(x)
    return x


x = int(input("Enter a value:"))
print(process_item(x))
