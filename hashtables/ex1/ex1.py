#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    target = limit
    """
    YOUR CODE HERE
    """
    print('Target: ', target)
    print('Weights: ', weights)
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



weights_3 = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights_3, 5, 21)