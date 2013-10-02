import sys 

w=sys.argv[1:]

w.sort()

wl=words[-1]

wnl=words[:-1]

wnl='.'.join(wnl)

wnl += ', and' + wl '.'

wnl=wnl.capitalise()
