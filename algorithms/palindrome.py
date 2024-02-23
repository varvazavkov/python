import sys

def reverse_str(strn):
    if strn == "":
        return strn
    else:
        return reverse_str(strn[1:]) + strn[0]

s = sys.argv[1]

if s == reverse_str(s):
    print('True')
else:
    print('False')
