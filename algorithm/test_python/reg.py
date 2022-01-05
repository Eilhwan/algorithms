import re

pattern = r"spam"
strings = "sspam"
# Regular expressions in Python can be accessed using the re module, which is part of the standard library.
# After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
# If it does, match returns an object representing the match, if not, it returns None.
# To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
# Raw strings don't escape anything, which makes use of regular expressions easier.

if re.match(pattern, "sspamsspamsspam"):
    print("Match")


# Other functions to match patterns are re.search and re.findall.
# The function re.search finds a match of a pattern anywhere in the string.
# The function re.findall returns a list of all substrings that match a pattern.

if re.search(pattern, strings):
    print("searched", re.search(pattern, strings))

# it out list of all the matched substring
if re.findall(pattern, strings):
    print("findall", (re.findall(pattern, strings)))

# The regex search returns an object with several methods that give details about it.
# These methods include group which returns the string matched, start and end which return the start and ending positions of the first match, 
# and span which returns the start and end positions of the first match as a tuple.
# Example:
match = re.search(pattern, "spammerspan")
if match:
    print(match.group(0))
    print(match.start())
    print(match.end())
    print(match.span())

# One of the most important re methods that use regular expressions is sub.
# Syntax:
print(re.sub(pattern, "hi", strings, 1))

# Metacharacters are what make regular expressions more powerful than normal string methods.
# They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

# selection of metacharacters = . [^, $] * + - [{ }]

pattern = '^...$'
if re.match(pattern, 'aaaaa'):
    print("match4")

if re.match(r"[1-4][a-z]", "4z"):
    print("match5")

if re.match(r"spam(egg)", "spamegg"):
    print(re.match(r"[a-zA-z]*(1)*", "a1a1").group(1))

