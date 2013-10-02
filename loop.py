import sys
a=sys.argv[1:]
print a
sum=0
for i in range (0,len(a)):
    b=float(a[i])
    print b
    sum+=b
print sum
