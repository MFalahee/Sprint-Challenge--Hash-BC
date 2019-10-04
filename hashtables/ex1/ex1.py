#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    limit
    """
    YOUR CODE HERE
    """
    print('Weights: ', weights)
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        target = limit - weights[i]
        if hash_table_retrieve(ht, target):
            we_got_it = hash_table_retrieve(ht, target)
            # print('we', we_got_it, target)
            # print('i', i, weights[i])
            if weights[i] > target:
                answer = (i, we_got_it)
                print(answer)
                return answer 
            else:
                answer = (we_got_it, i)
                print(answer)
                return answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


