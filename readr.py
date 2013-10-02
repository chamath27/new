from rodents import Rodent
rodents = {}
tagid=
weightm=
f=open('ref.csv')
while True:
    line=file.readline()
    if (tagid in line):
        Rodent.add_weight(weightm)
    else:
        x = Rodent(tagid)
        Rodent.add_weight(weightm)
    if not line:
        break
file.close
