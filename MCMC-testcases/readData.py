def readData(filename):
       	lines=[]
       	f=open(filename,'rb')

       	for line in f:
       		lines.append(line.split('\t'))

       	cont=[]
       	for i in range(len(lines)):
       		count=0
       		for item in lines[i]:
       			if item==str(1):
       				cont.append([i, count])
       			count=count+1

       	for i in range(len(lines)):
       		lines[i][-1]=lines[i][-1].strip('\n')

       	return lines
