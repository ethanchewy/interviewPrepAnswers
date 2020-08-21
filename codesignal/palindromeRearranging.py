"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""

def palindromeRearranging(inputString):
    # for us to have a palindrome we need:
    # - even count of each character except for perhaps 1 (if odd length). ex: (aabcbaa)
    # if we meet all those conditions, we can rearrange it into a palindrome
    
    dict_input = {}
    
    for ch in inputString:
        if ch in dict_input:
            dict_input[ch] += 1
        else:
            dict_input[ch] = 1

    count_odd = 0
    for _, val in dict_input.items():
        if val == 1 or val % 2 != 0:
            count_odd += 1
        if count_odd > 1:
            return False
    
    return True
