"""
Write a function that extracts the words from a given text as a parameter.
A word is defined as a sequence of alpha-numeric characters.
"""

def exercise1(element, **kargs):
    list_of_words = {}
    i = 0
    words = element.split()
    
    for word in words:
        list_of_words.update({i : word})
        i += 1

    return list_of_words    

print("Exercise 1: " + str(exercise1("Mama mea are mere")), end = "\n\n")


"""
Write a function that receives as a parameter a regex string,
a text string and a whole number x, and returns those long-length x substrings that match the regular expression.
"""
import re

def exercise2(text, regex, number):
    my_text = text.split()
    list_of_words = []

    for word in my_text:
        if re.search(regex, word) and len(word) == number:
            list_of_words.append(word)
    
    return list_of_words


text = "Mama mea este florareasa"
regex = "^[a-z]"
number = 4

print("Exercise 2: " + str(exercise2(text, regex, number)), end = "\n\n")

"""
Write a function that receives two parameters: a list of strings and a list of regular expressions.
The function will return a list of the strings that match on at least one regular expression
from the list given as parameter.
"""

def exercise3(string, regex):
    list_of_words = string
    list_of_regex = regex
    list_of_resulted_words = []
    
    for newWord in list_of_words:
        res = any(re.search(newRegex, newWord) for newRegex in list_of_regex)
        if res:
            list_of_resulted_words.append(newWord)

    return list_of_resulted_words

list_of_strings = ['Mama', 'mea', 'este', 'florareasa']
list_of_regex = ['^m', 'a$']

print("Exercise 3: " + str(exercise3(list_of_strings, list_of_regex)), end = "\n\n")


"""
Write a function that receives as a parameter the path to an xml document
and an attrs dictionary and returns those elements that have as attributes all the keys
in the dictionary and values ​​the corresponding values. For example,
if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be
those tags whose attributes are class="url" si name="url-form" si data-id="item".
"""
import xml.etree.ElementTree as ET


def exercise3(data, dict):
    my_reg = "^<.*>$"
    list_of_xml = []
    
    tree = ET.parse('data.xml')
    root = tree.getroot()
    list_of_tag = []
    for child in root:
        for key, value in dict.items():
            for k, v in child.attrib.items():
              if value == v and key == k:
                list_of_tag.append(child.tag)
    
    return list_of_tag
data = 'data.xml'
dict = {"id":"bk106"}
print("Exercise 3: " + str(exercise3(data, dict)), end = "\n\n")

"""
Write another variant of the function from the previous exercise that
returns those elements that have at least one attribute that corresponds
to a key-value pair in the dictionary.
"""

def exercise4(data, dict):
    my_reg = "^<.*>$"
    list_of_xml = []
    
    tree = ET.parse('data.xml')
    root = tree.getroot()
    list_of_tag = []
    empty_dic = {}
    
    for child in root:
        shared_items = {dict[k]: dict[k] for k in dict if k in child.attrib and dict[k] == child.attrib[k]}
        if shared_items != empty_dic:
            list_of_tag.append(child.tag)
    
    return list_of_tag
data = 'data.xml'
dict = {"id":"bk106"}
print("Exercise 4: " + str(exercise4(data, dict)), end = "\n\n")

"""
Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
Censorship means replacing characters from odd positions with *.
"""

def exercise6(censured):
    my_Text = censured.split()
    my_text_list = []
    for word in my_Text:
        if re.search("[^aeiou]", word) and re.search("[aeiou]$", word):
            for ch in range(len(word)):
                if ch % 2 != 0:
                    word = word.replace(word[ch], "*")
            my_text_list.append(word)
        else:
            my_text_list.append(word)
    my_text = ' '.join(my_text_list)
    return my_text

censured = "Arite a function that, for a text given as a parameter, censures words that begin and end with vowels."

print("Exercise 6: " + str(exercise6(censured)), end = "\n\n")


"""
Verify using a regular expression whether a string is a valid CNP.

https://regex101.com/library/bpaE5K
"""

def exercise7(cnpReg, personal):
    if re.search(cnpRegex, personal):
        print("Good CNP")
    else:
        print("Bad CNP")

cnpRegex = "^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$"
cnp = "5010801375492"
print("Exercise 7: ", end=" ") 
exercise7(cnpRegex, cnp)
print(end="\n")


"""
Write a function that recursively scrolls a directory and displays those files whose
name matches a regular expression given as a parameter or contains a string
that matches the same expression.
Files that satisfy both conditions will be prefixed with ">>"
"""
import os

def exercise8(director, regex):
    fileNames = os.listdir(director)
    list_of_extension = set()
    char = ">>"
    try:
        for fileName in fileNames:
            file, extension = os.path.splitext(fileName)
            if re.match(regex, file) or re.search(regex, file):
                file = char + str(file)
                list_of_extension.add(file) # adaug fisier cand gasesc regexul
                if re.search("txt$", extension): # deschid fisierul ca sa gasesc acest reget in int sau
                    with open(file, "r") as e:
                        new_Check = os.readlines(e)
                        new_Check = new_Check.split()

                        for line in new_Check:
                            if re.search(regex, line):
                                line = char + str(line)
                                list_of_extension.add(line)
                                
            # in caz de avem fisiere ce contine spatii in string
            # aici nu am inteles exact ideea probleme, sper sa fie ok-ish
            else:
                my_file = file.split()
                for element in my_file:
                    if re.search(regex, element):
                        file = char + str(file)
                        list_of_extension.add(file)

        return list_of_extension

    except Exception as e:
        print("Nu s-a putut accesa fisierul " + str(e))
        return []

regex = "^m"
print("Exercise 8: " + str(exercise8("C:\\Users\\Lucian\\OneDrive\\Documents", regex)), end="\n\n")