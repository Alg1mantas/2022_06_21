# create a public function, which generate a dictionary with
# 10 random  key value pairs
# keys yra random raide kuri negali kartotis
# value yra random skaicius, kuris negali kartotis nuo 0iki 30
#grazinti kokiam key priklauso didziausias value

import random, string
 
def dict_generator() -> str:
    my_dictionary = {}
 
    while True:
        random_letter = random.choice(string.ascii_lowercase)
        random_number = random.randint(1, 30)
 
        if random_number not in my_dictionary.values():
            my_dictionary[random_letter] = random_number
 
        if len(my_dictionary) >= 10:
            break
    print(my_dictionary)   
    return max(my_dictionary, key=my_dictionary.get)