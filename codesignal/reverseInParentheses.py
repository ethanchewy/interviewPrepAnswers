"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.
"""

def reverseInParentheses(inputString):
    final_string = ""
    temp = ""
    starting = False
    most_recent_left = []
    temp = inputString
    for idx, val in enumerate(inputString):
        if val == "(":
            most_recent_left += [idx]
        elif val == ")":
            most_recent_right = idx
            current_left = most_recent_left.pop()
            current_string = temp[current_left+1: most_recent_right][::-1]
            temp = temp[:current_left] + " " + current_string + " " + temp[most_recent_right+1:]
            
    temp = temp.replace(" ", "")
    return temp
            
