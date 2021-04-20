import itertools
liste = list(itertools.permutations(["ahmet", "uslu", "1990"]))
firstwordlist = open("firstwordlist.txt", "w")

def listToString(a):
    str1 = ""

    for ele in liste[a]:
        str1 += ele
    return str1

i = 0
while i < 6:
    print(listToString(i))
    firstwordlist.write(listToString(i) + "\n")
    i = i + 1