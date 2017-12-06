import mdtraj as md
import glob
import numpy as np
from msmbuilder.utils import io
import os
import math

path='/Users/shriyaa/Desktop/CS598SS/project/villin-data'
topfile=path+'/villin_ca.pdb'

numRes=35

def createDatasetFile(lines):

       	cont_all=[]
       	for i in range(numRes):
       		for j in range(i+1,numRes):
       			cont_all.append([i,j])

       	cont=[]
       	for i in range(len(lines)):
       		if lines[i]==str(1):
       			cont.append(cont_all[i])

       	print
       	print "Cont: ",
       	print cont
       	print

       	for file in sorted(glob.glob(path+'/*.dcd')):
       		t=md.load(file,top=topfile)
       		dist=md.compute_contacts(t,cont,scheme='ca')
       		ftr=[np.ndarray.tolist(dist[0][i][:]) for i in range(len(dist[0]))]
       		np.save(path+'/'+file.split('/')[-1]+'.npy', ftr)

       	dataset=[]
       	for file in sorted(glob.glob(path+'/*.npy')):
       		a=np.load(file)
       		dataset.append(a)

       	io.dump(dataset,'dataset_distances.pkl')

def runOsprey():

       	pseudoScore=-10

       	cmd="rm *.db temp_*.txt"
       	os.system(cmd)

       	cmd="osprey worker osprey-config-example.yaml"
       	os.system(cmd)

       	cmd="osprey current_best osprey-config-example.yaml > temp_best.txt"
       	os.system(cmd)

       	cmd="head -n 2 temp_best.txt > temp_score_line.txt"
       	os.system(cmd)

       	f=open('temp_score_line.txt','rb')
       	lines=[]
       	for line in f:
       		lines.append(line)
       	f.close()

       	if len(lines)<2:
       		return pseudoScore
       	else:
       		return float(lines[1].split(' ')[4])

def calcGMRQScores(lines):

       	createDatasetFile(lines)
       	gmrq_score=runOsprey()

       	score=math.exp(gmrq_score)

       	return score
