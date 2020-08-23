"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name
"""

import re

regex = r"^([A-Za-z_][\d|]*)+$"

def variableName(name):
    return re.match(regex, name) != None
