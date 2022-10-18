import numpy as np

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


print(fibonacci(3), end="\n\n")

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


def list_of_numbers(list_of_elem):
    new_list = []

    for i in list_of_elem:
        prime_numbers(i)

    print(end="\n")
    return new_list


list_of_elem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The prime numbers are: ", end="")
list_of_numbers(list_of_elem)

"""
      3. Write a function that receives as parameters two lists a and b and returns:
         (a intersected with b, a reunited with b, a - b, b - a)
"""


def intersection(a, b):
    list_of_intersection = []
    for i in a:
        for j in b:
            if i == j:
                list_of_intersection.append(i)
    return list_of_intersection


def reunion(a, b):
    list_of_reunion = a + b
    final_list = []
    for i in list_of_reunion:
        if i not in final_list:
            final_list.append(i)

        final_list.sort()
    return final_list


def a_minus_b(a, b):
    a_minus_b_list = []
    for i in a:
        if i not in b:
            a_minus_b_list.append(i)
    return a_minus_b_list


def b_minus_a(a, b):
    b_minus_a_list = []
    for i in b:
        if i not in a:
            b_minus_a_list.append(i)
    return b_minus_a_list


a = [2, 3, 4, 5, 6, 7, 12, 14]
b = [1, 3, 5, 7, 9, 12]
print("The intersection of a and b is: " + str(intersection(a, b)), end="\n")
print("The union of a and b is: " + str(reunion(a, b)), end="\n")
print("A minus B is: " + str(a_minus_b(a, b)), end="\n")
print("B minus A is: " + str(b_minus_a(a, b)), end="\n\n")

"""
4. Write a function that receives as a parameters a list of musical notes (strings),
   a list of moves (integers) and a start position (integer).
   The function will return the song composed by going though the musical notes beginning
   with the start position and following the moves given as parameter.
   
   Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] 
"""


def compose(musicalNotes, Moves, Start):
    print(musicalNotes[Start], end=" "),
    for move in Moves:
        print(musicalNotes[(Start + move) % musicalNotes.size], end=" ")
        Start = Start + move
    print(end="\n\n")


musicalNotes = np.array(["do", "re", "mi", "fa", "sol"])
compose(musicalNotes, [1, -3, 4, 2], 2)

"""
    5. Write a function that receives as parameter a matrix
       and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
       
       source : https://stackoverflow.com/questions/9958577/changing-the-values-of-the-diagonal-of-a-matrix-in-numpy
"""


def zero_matrix(matrix):
    matrix[np.diag_indices_from(matrix)] = 0

    return matrix


A = np.array([[2, 3, 1],
              [5, 1, 5],
              [1, 7, 2]])

print("The 0 matrix is: \n" + str(zero_matrix(A)), end="\n\n")

"""
6. Write a function that receives as a parameter a variable number of lists and a whole number x. 
   Return a list containing the items that appear exactly x times in the incoming lists. 
"""


def exactlyX(list_of_lists, x):
    new_list = []
    last = -1
    count = 0
    final_list = []
    for i in list_of_lists:
        new_list.extend(i)

    for i in new_list:
        var = new_list.count(i)
        if var == x and i not in final_list:
            print(str(i) + " appears exactly " + str(var) + " times", end="\n\n")
            final_list.append(i)


list_of_lists = [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]
x = 2
exactlyX(list_of_lists, x)

"""
      7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
         The first element of the tuple will be the number of palindrome numbers found in the list
         and the second element will be the greatest palindrome number.
"""


def tuples(list_of_numbers):
    tuples_of_2_elem = ()
    list_of_pal = []
    count = 0

    for i in list_of_numbers:
        copy_number = i
        new_number = 0

        while i > 0:
            helper = i % 10
            new_number = new_number * 10 + helper
            i = i // 10

        if copy_number == new_number:
            count += 1
            list_of_pal.append(copy_number)

    tuples_append = tuples_of_2_elem + (count,)

    var = max(list_of_pal)
    tuples_append = tuples_append + (var,)

    print("My tuple with numbers of palindroms and the greatest one is: " + str(tuples_append), end="\n\n")


list_of_palindroms = [121, 3321, 3113, 1421421, 1221, 414]
tuples(list_of_palindroms)

"""
8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set 
to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the 
flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x. 

 Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must 
 return list of lists.
"""


def gen(lista, x=1, flag=True):
    solution = []
    for currStr in lista:
        currSol = []
        for ascii in currStr:
            if (ord(ascii) % x == 0 and flag) or (ord(ascii) % x != 0 and flag == False):
                currSol.append(ascii)
        if currSol:
            solution.append(currSol)

    return solution


print(gen(["test", "hello", "lab002"], 2, False), end="\n\n")

"""
 Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.

	Example:

# FIELD

[[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]] 

Will return : [(2, 2), (3, 4), (2, 4)] """


def get_spectators(matrix):

    sol = set()
    for j in range(0, len(matrix[0])):
        for i in range(0, len(matrix)):
            for k in range(0, i):
                if matrix[i][j] <= matrix[k][j]:
                    sol.add((i, j))

    return sol


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

print(get_spectators(matrix), end="\n\n")

"""
10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
 the first tuple contains the first items in the lists,
  the second element contains the items on the position 2 in the lists, etc.
   Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 

Note: If input lists do not have the same number of items, missing items will be replaced with
 None to be able to generate max ([len(x) for x in input_lists]) tuples.
 
 
 """


def make_a_tuple(lists):
    tuple_output = ()

    input_lists = list(lists)

    max_tuple = max([len(x) for x in input_lists])

    for input_list in input_lists:
        if len(input_list) < max_tuple:
            input_list.extend(None for _ in range(len(input_list), max_tuple))

    transpusa = np.reshape(list_of_elements, (len(lists), len(lists[0])))
    transpusa = transpusa.transpose()

    rows = len(transpusa)
    columns = len(transpusa[0])

    for i in range(rows):
        for j in range(columns):
            tuple_output = tuple_output + (transpusa[i][j],)
        print(tuple_output, end="\n")
        tuple_output = ()
    print(end="\n")
    # .


list_of_elements = [1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]
make_a_tuple(list_of_elements)

"""
11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
 Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
"""


def order_tuple(string_list):
    return sorted(string_list, key=lambda x: x[1][2])


print(order_tuple([('abc', 'bcd'), ('abc', 'zza')]), end="\n\n")

"""
12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
 grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
    Example:
    group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']] 
    
    Asta este explicat de un coleg
    
    Explic la ora daca este nevoie, dar las si niste comentarii aici
    Facem un filter de cuvinte care au ultimele 2 litere la fel, si parcurgem lista pana la size
    daca gasim un cuvant care sa rimeze cu altul, se pastreaza noua lista cu cele 2 cuvinte si se adauga in lista de cuvinte
    daca acesta nu se regaseste acolo, ii facem in append in lista,
"""


def rhyme(words):
    final_result = []
    for index in range(0, len(words)):
        list_words = list(filter(lambda item: item[-2:] == words[index][-2:], words))
        if not (list_words in final_result):
            final_result.append(list_words)
    return final_result


print(rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
