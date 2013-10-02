

def base_count(a, b):
    n=a.count(b)
    return n
    
def gc_content(a):
    b=len(a)
    p=(a.count("G")+a.count("C")/float(b)
    return p

print base_count("GTUCC", "G")
print gc_content("GTUCC")
