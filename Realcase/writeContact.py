numRes=35

cont=[]

for i in range(numRes):
	for j in range(i+1,numRes):
		cont.append([i, j])

f=open('contacts_mapping.txt','wb')

for i in range(len(cont)):
	f.write(str(cont[i])+'\n')

f.close()
