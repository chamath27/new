import sys
a=sys.argv[1:]
a=int(a[0])

if a<50 and a>0:
    print "Minor"
elif a>=50 and a<1000:
    print "Major"
    

