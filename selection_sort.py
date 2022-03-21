from random import randint
from sys import argv

def selection_sort(list): # selection sort algoritm
    
    lenght = len(list)
    
    for i in range(lenght - 1):
        minim = list[i]
        minim_id = i
    
        for j in range(minim_id + 1, lenght): # search minim value and id
            if minim > list[j]:
                minim = list[j]
                minim_id = j
    
        if minim_id != i: # found minim then replace values
            list[minim_id], list[i] = list[i], list[minim_id]

    return list

value_arg = argv[1]

if value_arg == "-r":
    list = []
    lenght = randint(5, randint(10, 20)) # generate lenght
    
    for x in range(lenght): # generate list
        list.append(randint(x, lenght + x)) # generate random values
    
    print("list with random values: {}".format(list))
    print("selection sort algoritm: {}".format(selection_sort(list)))

else:
    list = list(
        map(int, argv[1].split(",")
        )
    )
    print(selection_sort(list))