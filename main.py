import re
from timeit import default_timer as timer


def isanagrams(s1, s2):
    return sorted(re.sub("[^A-za-z0-9]+", "", s1)) == sorted(
        re.sub("[^A-za-z0-9]+", "", s2)
    )


def hex_to_dec(hex_string):
    try:
        return int(f"0x{hex_string}", 16)
    except:
        return "Your string can't convert to decimal"


s1 = input("Type first string: ")
s2 = input("Type second string: ")
if isanagrams(s1, s2):
    print(f"{s1} and {s2} are anagrams.")
else:
    print(f"{s1} and {s2} are not anagrams.")

string = input("Type string to convert to base-10: ")
print(hex_to_dec(string))
