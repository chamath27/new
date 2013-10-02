def fib(n):
    suma=0;
    sumb=1;
    if n==1:
        sumc=1
    else:
        for i in range(1,n):
            print "i",i
            sumc=suma+sumb
            print suma
            suma=sumb
            print sumb
            sumb=sumc
            print sumc
    return sumc

print fib(10)
print fib(1)
