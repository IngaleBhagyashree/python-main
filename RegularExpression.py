# This imports Python's built-in re module, which provides support for regular expressions.
# Regular expressions allow you to search, match, and manipulate strings based on specific patterns.
import re
print(re.findall(r'\d+', "Age is 25"))  # ['25']
print(re.match(r'hello', 'hello world'))  # match

# Explanation:
# re.findall(): Returns a list of all non-overlapping matches of the regular expression pattern in the string
# r'\d+':
# The r before the string makes it a raw string, so special characters like \ are not treated as escape sequences.
# \d matches any digit (0–9).
# + means "one or more" of the preceding element (i.e., one or more digits).
# "Age is 25": The input string.
# ✅ Output: ['25']
# It finds one match: 25, and returns it as a list.

# Explanation:
# re.match(): Attempts to match the pattern only at the beginning of the string.
# r'hello': The pattern to match — here, the literal string 'hello'.
# 'hello world': The string to search in.
# ✅ Output: A match object, because the string starts with 'hello'.

# Line	Function	Purpose	Output
# 2	re.findall	Find all digit sequences in a string	['25']
# 3	re.match	Match pattern at string start	Match object
