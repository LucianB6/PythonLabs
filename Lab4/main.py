import os

"""
1)	Să se scrie o funcție ce primeste un singur parametru, director,
 ce reprezintă calea către un director. 

Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica)
 a fișierelor din directorul dat ca parametru.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’ 
"""


def exercise1(director):
    fileNames = os.listdir(director)
    list_of_extension = set()
    try:
        for fileName in fileNames:
            file, extension = os.path.splitext(fileName)
            if extension is not list_of_extension:
                list_of_extension.add(extension)
        return sorted(list_of_extension)

    except Exception as e:
        print(str(e))
        return []

print("Exercise 1: " + str(exercise1("C:\\Users\\Lucian\\OneDrive\\Documents")), end="\n\n")

"""
2)	Să se scrie o funcție ce primește ca argumente două căi:
 director si fișier. 

Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
 calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. 
"""


def exercise2(director, fisier):
    try:
        with open(fisier, "w") as f:
            print("Exercise 2:", end="")
            for el in os.listdir(director):
                name = os.path.join(director, el)
                if os.path.isfile(name) and el.startswith("A"):
                    print(os.path.abspath(name) + os.linesep)
    except Exception as e:
        print(str(e))

exercise2(".", "b.b")

"""
3)	Să se scrie o funcție ce primește ca parametru un string my_path.

Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
 Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count,
  unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv)
   din directorul dat ca parametru. 
"""


def exercise3(my_path):
    try:
        if os.path.isfile(my_path):
            file = os.path.basename(my_path)
            length = len(my_path)

            return file[length - 20:]

        elif os.path.isdir(my_path):
            lista = {}
            for root, dirs, files in os.walk(my_path):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in lista:
                        lista[ext] += 1
                    else:
                        lista[ext] = 1
            lista = lista.items()
            return sorted(lista, key=lambda el: el[1], reverse=True)

    except Exception as e:
        print(str(e))

my_path = "C:\\Users\\Lucian\\OneDrive\\Documents"
print("Exercise 3:" + str(exercise3(my_path)), end="\n\n")

"""
4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la 
linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală. 
"""


def exercise4():
    path = "C:\\Users\\Lucian\\OneDrive\\Documents"
    fileNames = os.listdir(path)
    list = set()
    for fileName in fileNames:
        extension = os.path.splitext(fileName)[1]
        list.add(extension)

    return sorted(list)


print("Exercise 4: " + str(exercise4()), end="\n\n")

"""
5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza
 o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar
  in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
   Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
"""
#
# def exercise5(target, to_search):
#
#     def file_contains_to_search(target, to_search):
#         fileNames = os.listdir(target)
#         list = set()
#         for fileName in fileNames:
#             file = os.path.splitext(fileName)[0]
#             if file(to_search):
#                 list.add(file)
#         return list
#
#
#     if os.path.isfile(target):
#         file = os.path.basename(target)
#         if file in file_contains_to_search(target, to_search):
#             return target
#
#
#     elif os.path.isdir(target):
#         fileNames = os.listdir(target)
#         list = set()
#
#         for fileName in fileNames:
#             file = os.path.splitext(fileName)[1]
#             if file in file_contains_to_search(target, to_search):
#                 list.add(file)
#
#         return list
#
#     else:
#         raise ValueError(target + ": is not a valid path to file or directory")
#
#
#
# print(exercise5(".", "b"))


"""
6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior,
 cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru,
  iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.
"""

"""
7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer
 si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti,
  file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
"""

def exercise7(file):
    return {"full_path:": os.path.abspath(file),
            "file_size:": os.path.getsize(file),
            "file_extension:": os.path.splitext(file)[1],
            "read:": os.access(file, os.R_OK),
            "write:": os.access(file, os.W_OK)
            }


file = "find.txt"
print("Exercise 7: " + str(exercise7(file)), end="\n\n")


"""
8)	Să se scrie o funcție ce primește un parametru cu numele dir_path.
 Acest parametru reprezintă calea către un director aflat pe disc.
  Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]

Calea "C:\\director" are pe disc următoarea structură:

C:\\director\\fisier1.txt <- fișier

C:\\director\\fisier2.txt <- fișier

C:\\director\\director1 <- director

C:\\director\\director2 <- director
"""


def exercise8(dir_path):
    result = []
    fileNames = os.listdir(dir_path)
    for file in fileNames:
        if (os.path.isfile(file)):
            name = os.path.join(dir_path, file)
            result += [os.path.abspath(name)]
    return result


dir_path = "C:\\Users\\Lucian\\OneDrive\\Desktop\\FIAnul3\\Python\\PythonLabs\\Lab4"
print("Exercise 8: " + str(exercise8(dir_path)), end="\n\n")
