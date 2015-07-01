from collections import defaultdict

f = open('firstrun.txt','r')
namelist = []
for line in f:
    if line.startswith('>'):
        namelist.append(line.strip())
f.close()

f1 = open('filter45database.txt','r')
seqlist = defaultdict(str)
name = ''
for line in f1:
    if line.startswith('>'):
        name = line[0:-1]
        continue
    seqlist[name] += line.strip()
f1.close()

for a in namelist:
    del seqlist[a]

f2 = open('dataset2.txt','w')
for key in seqlist.keys():
    f2.write(key + '\n')
    f2.write(seqlist[key] +'\n')
f2.close()