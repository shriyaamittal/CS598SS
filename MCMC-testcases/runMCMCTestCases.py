from readData import *
import numpy as np
import random
import time
import os
import sys
random.seed(time.time())

# Macros
BEST_SCORE=0
BEST_CHOICE=[]
MAX_ITERATIONS=100
iterationsForConvergence=5
CHOOSE_ELEMENTS=2

# Input file paths
inputfilename='./test.txt'
inputvaluefilename='./values.txt'
solutionfilename='./solution.txt'
iterationfile='./iterations.txt'


def calcTestScores(lines_0_1,lines_value):
       	sumScore=0
       	for i in range(len(lines_0_1)):
       		if (lines_0_1[i]==str(1)):
       			sumScore+=float(lines_value[i])
       	return sumScore

def doMCMC(lines,k):

       	lines_mod=lines[:]

       	"""
       	print "in MCMC"
       	print "old ",
       	print lines
       	"""

       	index_k=[]
       	index_not_k=[]

       	for i in range(len(lines)):
       		if (lines[i]==str(0)):
       			index_not_k.append(i)
       		else:
       			index_k.append(i)

       	choose_index_from_k=random.choice(index_k)
       	choose_index_for_k=random.choice(index_not_k)

       	for i in range(len(lines)):
       		if i==choose_index_from_k:
       			lines_mod[i]=str(0)
       		elif i==choose_index_for_k:
       			lines_mod[i]=str(1)

       	"""
       	print "new ",
       	print lines_mod
       	"""

       	return lines_mod

def checkAcceptReject(old,new):

       	pseudocount=0.001

       	if old==0:
       		old+=pseudocount

       	val=float(new)/old
       	A=min(1,val)

       	r=random.random()

       	if (r<=A):
       		flag="Accept"
       	else:
       		flag="Reject"

       	return flag

def writeData(filename,array):
       		f=open(filename,'wb')
       		for i in range(len(array)-1):
       			f.write(array[i]+'\t')
       		i+=1
       		f.write(array[i]+'\n')
       		f.close()


if __name__ == "__main__":

       	iteration=0

       	oldFilename=inputfilename
       	lines_value=readData(inputvaluefilename)
       	lines_0_1=readData(oldFilename)

       	k=CHOOSE_ELEMENTS

       	currentScore=calcTestScores(lines_0_1[0],lines_value[0])

       	rejectFlag=0

       	while (True):

       		iteration+=1

       		print
       		print "iteration "+str(iteration)
       		print

       		new_lines=doMCMC(lines_0_1[0],k)

       		newScore=calcTestScores(new_lines,lines_value[0])

       		flagAcceptReject=checkAcceptReject(currentScore,newScore)

       		print "currentScore "+str(currentScore)
       		print "newScore "+str(newScore)
       		print flagAcceptReject

       		if flagAcceptReject=="Accept":
       			rejectFlag=0

       			oldFilename="old-0-1-iter"+str(iteration)+'.txt'
       			newFilename="new-0-1-iter"+str(iteration)+'.txt'

       			writeData(oldFilename,lines_0_1[0])
       			writeData(newFilename,new_lines)

       			currentScore=newScore
       			oldFilename=newFilename
       			lines_0_1=readData(newFilename)

       		else:
       			rejectFlag+=1
       			if (rejectFlag==iterationsForConvergence):
       				break;

       		if newScore>BEST_SCORE:
       			BEST_SCORE=newScore
       			BEST_CHOICE=lines_0_1[0]

       		if (iteration>4):
       			cmd="rm old-0-1-iter"+str(iteration-1)+".txt"
       			os.system(cmd)
       			cmd="rm new-0-1-iter"+str(iteration-1)+".txt"
       			os.system(cmd)

       		if (iteration==MAX_ITERATIONS):
       			break;
#      		cmd="sleep 10"
#      		os.system(cmd)

       	print
       	print "Final score: "+str(currentScore)
       	print "Final BEST score: "+str(BEST_SCORE)

       	writeData(solutionfilename,BEST_CHOICE)

       	f=open(iterationfile,'wb')
       	f.write("iterations: "+str(iteration)+'\n')
       	f.write("k: "+str(k)+'\n')
       	f.write("score: "+str(BEST_SCORE)+'\n')
       	f.close()

       	cmd="rm old-0-1-iter*.txt"
       	os.system(cmd)
       	cmd="rm new-0-1-iter*.txt"
       	os.system(cmd)

       	print "Final choice: ",
       	print lines_0_1[0]
       	print "Final BEST choice: ",
       	print BEST_CHOICE
