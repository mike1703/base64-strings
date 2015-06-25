import base64
import sys
import re

#regex = re.compile("(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}[AEIMQUYcgkosw048]=|[A-Za-z0-9+/][AQgw]==)")
regex = re.compile("(?:[A-Za-z0-9+]{4}){2,}(?:[A-Za-z0-9+]{2}[AEIMQUYcgkosw048]=|[A-Za-z0-9+][AQgw]==)")

def get_strings(string):
    potentials = regex.findall(string)
    result = {}
    for potential in potentials:
        try:
            result[potential] = base64.b64decode(potential)
        except:
            pass
    return result

file = open(sys.argv[1])
for line in file:
    strings = get_strings(line)
    print strings

