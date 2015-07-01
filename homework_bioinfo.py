#Preprocessing
#from collections import defaultdict
#f = open('Results2(lm).txt','r')
#list = defaultdict(str)
#name = ''
#for line in f:
#    if line.startswith('>'):
#        name = line[1:-1]
#        continue
#    list[name] += line.strip()
#f.close()

#get raw data
f2 = open('Results2.2(lm).txt','r')
seqInfo = []
bank = []
for line in f2:
    if not line.startswith('\n') and '|' not in line and not line.startswith('N'):
        bank.append(line.strip())
f2.close()
del bank[0]

for line in bank:
    if  int(line.strip().split(' ')[0]) < int(line.strip().split(' ')[-1]):   
        seqInfo.append('>NC_023172.1_' + line.strip().split(' ')[0] + '_' + line.strip().split(' ')[-1] + '_' + line.strip().split(' ')[1])
    else:
        seqInfo.append('>NC_023172.1_' + line.strip().split(' ')[-1] + '_' + line.strip().split(' ')[0] + '_' + line.strip().split(' ')[1][::-1])

#filter nt < 18
filter18 = []
filter45 = []

for ele in seqInfo:
    if len(ele.split('_')[4]) >=18:
        filter18.append(ele)
        
#filter loop nt <45
for i in range(len(filter18)):
    if i % 2 == 0:
        if int(filter18[i+1].split('_')[3]) - int(filter18[i].split('_')[2]) >= 45:
            filter45.append(filter18[i])
            filter45.append(filter18[i+1])

f = open('processedSeqNew.txt','w')
for line in filter45:
    f.write('_'.join(line.split('_')[0:4]) + '\n')
    f.write(line.split('_')[4] + '\n')
f.close()