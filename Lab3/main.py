"""
1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
 (a intersected with b, a reunited with b, a - b, b - a)
"""


def functions(a, b):
    my_set_of_reunited = sorted(list(set(a) | set(b)))
    my_set_of_a_minus_b = sorted(list(set(a) - set(b)))
    my_set_of_intersection = sorted(list(set(a) & set(b)))
    my_set_of_b_minus_a = sorted(list(set(b) - set(a)))

    print("Reunited: " + str(my_set_of_reunited), end='\n')
    print("Intersection: " + str(my_set_of_intersection), end='\n')
    print("A minus B: " + str(my_set_of_a_minus_b), end='\n')
    print("B minus A: " + str(my_set_of_b_minus_a), end='\n\n')


a = [2, 3, 4, 5, 6, 7, 12, 14]
b = [1, 3, 5, 7, 9, 12]
functions(a, b)

"""
2. Write a function that receives a string as a parameter and returns a dictionary
   in which the keys are the characters in the character string and the values are 
   the number of occurrences of that character in the given text.
"""


def dictionary(words):
    letter = {}
    for i in words:
        for j in i:
            if j in letter:
                letter[j] += 1
            else:
                letter[j] = 1
    print("The dictionary is: " + str(letter), end="\n\n")


words = "Ana has apples."
dictionary(words)

"""
3. Compare two dictionaries without using the operator "==" returning True or False.
 (Attention, dictionaries must be recursively covered because they can contain other containers,
  such as dictionaries, lists, sets, etc.)
  
  https://www.geeksforgeeks.org/how-to-compare-two-dictionaries-in-python/
"""


def comparation(d, d1):
    res = all((d1.get(k) is v for k, v in d.items()))
    print(res, end="\n\n")


d = {"a": 3, "b": 2}
d1 = {"a": 3, "b": 2}
comparation(d, d1)

"""
4. The build_xml_element function receives the following parameters:
 tag, content, and key-value elements given as name-parameters.
  Build and return a string that represents the corresponding XML element.
   Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ",
    id= " someid ") returns  the string = "<a href=\"http://python.org \ "_class = \" my-link 
    \ "id = \" someid \ "> Hello there </a>
"""


def build_xml_element(tag, content, elements):
    return "<{} {}> {} <\{}>".format(tag, ", ".join("{} = \" {} \"".format(keys, value)
                                                    for keys, value in elements.items())
                                     , content, tag)


tag = "a"
content = "Hello there"
elements = {
    "href": "http://python.org",
    "_class": "my-link",
    "id": "someid"
}
print(build_xml_element(tag, content, elements))

"""
5. The validate_dict function that receives as a parameter a set of tuples
 ( that represents validation rules for a dictionary that has strings as keys and values)
  and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
   A value is considered valid if it starts with "prefix", "middle" is inside the value
    (not at the beginning or end) and ends with "suffix".
 The function will return True if the given dictionary matches all the rules, False otherwise.
"""


def validate_dict(rules_set, dictionary_set):
    for rules in rules_set:
        value = dictionary_set.get(rules[0])

        if value is None:
            return False

        if not value.startswith(rules[1]):
            return False
        if not value.endswith(rules[3]):
            return False
        if not rules[2] in value:
            return False

    return True


rules_set = {("key1", "come", "inside", "out"), ("key2", "start", "middle", "winter")}
dictionary_set = {"key1": "come inside, it's too cold out", "key2": "start middle this is not valid winter"}

print(validate_dict(rules_set, dictionary_set))

"""
6. Write a function that receives as a parameter a list and returns a tuple (a, b),
 representing the number of unique elements in the list, and b representing the number
  of duplicate elements in the list (use sets to achieve this objective).
  """


def aparitii(cuvant):
    letter = {}
    list2 = set()
    for i in cuvant:
        for j in i:
            if j in letter:
                letter[j] += 1
            else:
                letter[j] = 1
    print(letter)
    a = 0
    b = 0
    for keys, values in letter.items():
        if values == 1:
            a += 1
        if values == 2:
            b += 1
    list2.add((a, b))

    print(list2, end="\n\n")


my_list = ["mamaiaattooukj"]
aparitii(my_list)

"""
7. Write a function that receives a variable number of sets and returns a dictionary
 with the following operations from all sets two by two: reunion,
  intersection, a-b, b-a. The key will have the following form: "a op b",
   where a and b are two sets, and op is the applied operator: |, &, -. 

Ex: {1,2}, {2, 3} =>

{

    "{1, 2} | {2, 3}":  {1, 2, 3},

    "{1, 2} & {2, 3}":  { 2 },

    "{1, 2} - {2, 3}":  { 1 },

    ...

}
"""


def matemathicalFunctions(dict):
    print(str(dict[0]) + " | " + str(dict[1]) + " : " + str(dict[0] | dict[1]))
    print(str(dict[0]) + " & " + str(dict[1]) + " : " + str(dict[0] & dict[1]))
    print(str(dict[0]) + " - " + str(dict[1]) + " : " + str(dict[0] - dict[1]))
    print(str(dict[1]) + " - " + str(dict[0]) + " : " + str(dict[1] - dict[0]), end="\n\n")


dict = {1, 2}, {2, 3}
matemathicalFunctions(dict)

"""
8. Write a function that receives a single dict parameter named mapping.
 This dictionary always contains a string key "start".
  Starting with the value of this key you must obtain a list of objects by iterating over mapping
   in the following way: the value of the current key is the key for the next value,
    until you find a loop (a key that was visited before). The function must return the list of objects
     obtained as previously described.

Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
 will return ['a', '6', 'z', '2']
"""


def loop(mapping):
    current_value = mapping['start']
    final_list = list()

    while current_value not in final_list:
        final_list.append(current_value)
        current_value = mapping[current_value]
    print(final_list, end="\n\n")


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
loop(mapping)

"""
9. Write a function that receives a variable number of positional arguments
 and a variable number of keyword arguments adn will return the number of positional arguments
  whose values can be found among keyword arguments values.

Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3
"""


def my_function(values, my_dictionary):
    counter = 0
    list_of_values = []
    for current_value in values:
        for value_from_dictionary in my_dictionary.values():
            if current_value == value_from_dictionary and current_value not in list_of_values:
                list_of_values.append(current_value)
                counter += 1

    print(counter)


values = [1, 2, 3, 4]
my_dictionary = {'x': 1, 'y': 2, 'z': 3, 'w': 5}
my_function(values, my_dictionary)
