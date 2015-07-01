from collections import defaultdict

f1 = open('dataset2.txt','r')
namelist = defaultdict(str)
name = ''
for line in f1:
    if line.startswith('>'):
        name = line[0:-1]
        continue
    namelist[name] += line.strip()
f1.close()

seqlist = {}
for key in namelist.keys():
    if len(namelist[key]) <= 21:
        seqlist[key] = namelist[key]
        del namelist[key]
        
potlist = {}
for key in namelist.keys():
    count = 0
    while count <= len(namelist[key]) - 21:
        potential = ''
        potential = namelist[key][count:(count+21)]
        potlist[key+'_'+str(count)] = potential
        count += 1

#f2 = open('prediction.txt','w')
#for key in seqlist.keys():
#    f2.write(key + '\n')
#    f2.write(seqlist[key] +'\n')
#f2.close()
#
#f3 = open('prediction2.txt','w')
#for key in potlist.keys():
#    f3.write(key + '\n')
#    f3.write(potlist[key] +'\n')
#f3.close()