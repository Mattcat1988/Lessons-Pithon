import re

mytext = "Vova, vova, mail.ru, .com mattcat, vova, Nikita, Ivan ggggg.gov, gggggggggg.com" \
         "123, stamp, Nik, 345, 564, 234234234234"
"""
\d   = any Digit 0-9
\D   = any non digit
\w   = Any Alphabet sysbol  [A-Z a-z]
\W   = Any non Alphabet symbol
\s   = breakspace
\S   = non breakspace
[0-9]{3}
[A-Z]
[A-Z][a-z]+
\w+\.\w+  domain

"""

textlookfor = r"\w+\.\w+"
allreults = re.findall(textlookfor, mytext)
print(allreults)
