"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
"""

def arrayChange(inputArray):
    previous = inputArray[0]
    total = 0
    
    for i in range(1, len(inputArray)):
        if inputArray[i] <= previous:
            need_to_add = previous - inputArray[i] + 1
            inputArray[i] += need_to_add
            total += need_to_add
            
        previous = inputArray[i]
    
    return total
