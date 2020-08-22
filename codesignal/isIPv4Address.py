"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
"""

import re

# Constructs range 0-255
# If we are not at the end of the file (via a negative lookahead function), then we check for a dot afterwards
# If we are at the end of the file, we don't check for a dot. 
# We check for this 4 times.

# Source: https://stackoverflow.com/a/36760050/4698963
regex = r"^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"

def isIPv4Address(inputString):
    return re.match(regex, inputString) != None
