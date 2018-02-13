import re

"""
Identifiers
\d - any number
\D - anything but a number
\s - space
\S - anything but a space
\w - any character
. - any character except \n
/b - white space around words
\. - a period

Modifiers
{1,3} - 1-3 of a thing
+ - match 1 or more
? - match 0 or 1
* - match 0 or more
$ - end of a string
^ - beginning of a string
| - either or -- d{1-3) | \w{5-6}
[] - range or "variance"
{5} - exact number

White Space Characters
\n - newline
\s - space
\t - tab
\e - escape
\f - form feed
\r - return 
"""

toFix = "2x2 + 3x - 5x + 6x5"
#numTimesX = re.findall(r"\d(x)", toFix)
#xToPower = re.findall(r"x(\d)", toFix)

toFix = re.sub("(\d+)(x)", lambda x: str(x.group(1)) + "*x", toFix)
toFix = re.sub("(x)(\d+)", lambda x: "x**" + str(x.group(2)), toFix)
print(toFix)
