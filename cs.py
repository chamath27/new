import sys
import string
a=sys.argv[1:]
print a

a=a[0]



a=a.upper()
al=string.uppercase
a=set(a)
a=a.intersection(al)
l=len(a)

print l
