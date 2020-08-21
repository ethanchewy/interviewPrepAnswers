"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
"""

def areSimilar(a, b):
    # a and b can only be similar if we unionize a and b results in only 2 or 0 dissimilarities because we can at most swap once 
    count = 0
    a_dict = {}
    b_dict = {}
    for a_val, b_val in zip(a, b):
        if a_val != b_val:
            count+=1
        if a_val in a_dict:
            a_dict[a_val] += 1
        else:
            a_dict[a_val] = 1
        
        if b_val in b_dict:
            b_dict[b_val] += 1
        else:
            b_dict[b_val] = 1

    if (count == 0 or count == 2) and a_dict == b_dict:
        return True
    return False
