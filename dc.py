import sys

a=sys.argv[1:]
print a
a=a[0]
if a.count("T") > 0:
  l=["G","A","T","C"]
  print "DNA"
  
if a.count("U") > 0:
  l=["G","A","U","C"]
  print "RNA"
d={l[i]: a.count(l[i]) for i in range(0,4)}
print d
b=len(a)
p=(d["G"]+d["C"])/float(b)
print p 
