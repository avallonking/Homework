f1 = open('predicted.txt','r')
results = []
for line in f1:
    if line.startswith('>'):
        singleInfo = [line.strip()]
    else:
        singleInfo.append(line.strip())
    results.append(singleInfo)
f1.close()

new = []
for item in results:
    if float(item[5].split(' ')[-1]) >= 0.85:
        new.append(item)
        
new1 = []
for item in new:
    g = 0
    c = 0
    for base in item[1]:
        if base == 'g':
            g += 1
        elif base == 'c':
            c += 1
    if float((g+c))/len(item[1]) >= 0.33 and float((g+c))/len(item[1]) <= 0.5:
        new1.append(item)

new2 = []
for item in new1:
    temp = item[3].split(' ')[-1][0:-1]
    if '[' in temp:
        temp = temp[1:]
    
    if float(temp) <= -5.9725:
        new2.append(item)

new3 = []
for item in new2:
    struct = item[3].split(' ')[0]
    loop = 0
    for i in range(len(struct)-2):
        if struct[i:i+2] == '(.':
            loop += 1
    if loop < 2:
        new3.append(item)

new4 = []
for item in new3:
    loopLen = item[3].split(' ')[0]
    if '(...)' in loopLen:
        pass
    elif '(..)' in loopLen:
        pass
    elif '(.)' in loopLen:
        pass
    elif '{...}' in loopLen:
        pass
    else:
        new4.append(item)
#
#new5 = []
#for item in new4:
#    lnum = 0
#    rnum = 0
#    seqStruct = item[3].split(' ')[0]
#    left = seqStruct.split('(')
#    right = seqStruct.split(')')
#    
#    for i in left[1:-1]:
#        if i != '':
#            lnum = len(i)
#            
#    for t in right[1:-1]:
#        if t != '':
#            rnum = len(t)
#            
#    if lnum + rnum >= 4:
#        new5.append(item)

f2 = open('dataset3.txt','w')
for item in new4:
    f2.write(item[0] + '\n')
    f2.write(item[1] + '\n')
f2.close()