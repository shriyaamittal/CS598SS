import mdtraj as md
import glob
import numpy as np

lines=[]
f=open('mydata_new.txt','rb')

for line in f:
       	lines.append(line.split('\t'))

cont=[]
for i in range(len(lines)):
       	count=0
       	for item in lines[i]:
       		if item==str(1):
       			cont.append([i, count])
       		count=count+1

path='/Users/shriyaa/Desktop/CS598SS/project/villin-data'
topfile='villin_ca.pdb'

for file in sorted(glob.glob(path+'/*.dcd')):
       	t=md.load(file,top=topfile)
       	dist=md.compute_contacts(t,cont,scheme='ca')
       	ftr=[np.ndarray.tolist(dist[0][i][:]) for i in range(len(dist[0]))]
       	np.save(path+'/'+file.split('/')[-1]+'.npy', ftr)

dataset=[]
for file in sorted(glob.glob(path+'/*.npy')):
       	a=np.load(file)
       	dataset.append(a)

from msmbuilder.utils import io

io.dump(dataset,'dataset_distances.pkl')
