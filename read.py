

f=open('uniprot_sprot.fasta',r)


a=f.readline()


if not a:
    break
#OS=Homo sapiens
if (a[0]==">" and "OS=Homo sapiens" in line):
    count+=1
file.close()

print count
