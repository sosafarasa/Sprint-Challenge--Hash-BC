#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index in range(0, length): #adds weights to the ht
        hash_table_insert(ht, weights[index], index)

    for index in range(0, length): # checks limit - weights[index] = True
        if hash_table_retrieve(ht, limit - weights[index]):
            if index > hash_table_retrieve(ht, limit - weights[index]):
                return index, hash_table_retrieve(ht, limit - weights[index])
            else:
                return(hash_table_retrieve(ht, limit - weights[index]), index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
