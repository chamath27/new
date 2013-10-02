a=5;
import sys
a=sys.argv[1:]
a=int(a[0])
if a%2==1:
    print "odd"
elif a%2==0:
    print "even"
