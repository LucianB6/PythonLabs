# 1. Find The greatest common divisor of multiple numbers read from the console.

print("")
numbers = [2, 4, 6, 16, 28]

first = numbers[3]
second = numbers[4]


def gcd(value1, value2):
    first_list = []
    second_list = []
    greatest = 0

    for i in range(2, value1 + 1):
        if value1 % i == 0:
            first_list.append(i)

    for j in range(1, value2 + 1):
        if value2 % j == 0:
            second_list.append(j)

    for i in range(len(first_list)):
        for j in range(len(second_list)):
            if first_list[i] == second_list[j]:
                if greatest < first_list[i]:
                    greatest = first_list[i]

    return greatest


print("Cmmdc dintre " + str(first) + " si " + str(second) + " este " + str(gcd(first, second)))

print("")


# 2. Write a script that calculates how many vowels are in a string.

def vowelCalculator(vowel, string):
    vowelCounter = 0

    for i in range(len(string)):
        if string[i] in vowel:
            vowelCounter += 1

    return vowelCounter


vowel = 'aeiou'
string = "Mama are mere"

print("In stringul " + str(string) + " sunt " + str(vowelCalculator(vowel, string)) + " vocale")


# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def occurences(string1, string2):
    word = 0
    first_word = string1.split()
    second_word = string2.split()

    for i in range(len(first_word)):
        for j in range(len(second_word)):
            if first_word[i].lower() == second_word[j].lower():
                word += 1

    return word


string1 = 'daniel'
string2 = 'Daniel mama mama'

print("")
print("De cate ori gasim stringul 1 in stringul 2: " + str(occurences(string1, string2)))
print("")


# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def lowercase(convert):
    for i in range(len(convert)):
        if convert[i].islower() == True and convert[i + 1].isupper() == True:
            convert = convert[:i + 1] + "_" + convert[i + 1:]

    convert = convert.lower()
    return convert


print("The lower case form is: " + str(lowercase('UpperCamelCase')))
print("")


# 5. Given a square matrix of characters write a script that prints the string obtained
# by going through the matrix in spiral order (as in the example):

# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
def spiralPath(matrix):

    rows = len(matrix)  # indexul lui i de final
    columns = len(matrix[0])  # indexul lui j de final

    left = 0  # indexul lui i de inceput
    right = 0  # indexul lui j de inceput

    while left < rows and right < columns:

        for i in range(right, columns):
            print(matrix[left][i], end="")
        left += 1

        for i in range(left, rows):
            print(matrix[i][rows - 1], end="")
        columns -= 1

        if left < rows:
            for i in range(columns - 1, right - 1, -1):
                print(matrix[rows - 1][i], end="")

            rows -= 1

        if right < columns:
            for i in range(rows - 1, left - 1, -1):
                print(matrix[i][right], end="")
            right += 1


matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]

print("The word formed is: ", end="")

spiralPath(matrix)

print("")

# 6. Write a function that validates if a number is a palindrome.
print("")


def palindrom(number):
    copy_number = number
    new_number = 0

    while number > 0:
        helper = number % 10
        new_number = new_number * 10 + helper
        number = number // 10

    if copy_number == new_number:
        print(str(copy_number) + " este palindrom ")
    else:
        print(str(copy_number) + " nu este palindrom ")


palindrom(1211)
print("")

# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123,
# or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.

import re


def extract(i):
    a = re.findall("(-?\d+)", i)
    a = a[0]
    return a


i = 'aa23bb22'
print("First number character is: " + str(extract(i)))

# 8. Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
print("")
value = 24
binary = "{0:b}".format(value)
binary = int(binary)


def binaryCounter(bin):
    index = 0

    while bin > 0:
        if bin % 10 == 1:
            index += 1
        bin = bin // 10

    return index


print("We have " + str(binaryCounter(binary)) + " bites for " + str(value))

# 9. Write a functions that determine the most common letter in a string. For example if the string is "an apple is
# not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

print("")


def commonLetter(common):
    letter = {}

    newWord1 = common.lower()
    newWord = newWord1.replace(" ", "")

    for i in newWord:
        if i in letter:
            letter[i] += 1
        else:
            letter[i] = 1
    result = max(letter, key=letter.get)

    return result


word = "an apple is not A tomato"

print("The most common letter is: " + str(commonLetter(word)))

print("")


# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.


def wordCounter(sentence):
    word_counter = 0
    j = len(sentence)

    newSentence = sentence.split()

    for i in newSentence:
        word_counter += 1

    return word_counter


sentence = "I have Python exam "

print("The number of words is: " + str(wordCounter(sentence)))

print("")
