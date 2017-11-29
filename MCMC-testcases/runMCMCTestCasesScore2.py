from readData import *
import numpy as np
import random
import time
import os
import sys

random.seed(time.time())

iterationsForConvergence=5

inputfilename='./test.txt'
inputvaluefilename='./values.txt'
solutionfilename='./solution.txt'
iterationfile='./iterations.txt'

MAX_ITERATIONS=10000

def calcTestScoresWithPenalty(lines_0_1,lines_value):
       	sumScore=0
       	count=0
       	for i in range(len(lines_0_1)):
       		if (lines_0_1[i]==str(1)):
       			sumScore+=float(lines_value[i])
       			count+=1
       	return sumScore-float(count)/len(lines_0_1)

def doMCMC(lines,k):

       	lines_mod=lines[:]

       	"""
       	print "in MCMC"
       	print "old ",
       	print lines
       	"""

       	choose=random.sample(range(len(lines)),k)

       	for i in range(len(lines)):
       		if i in choose:
       			lines_mod[i]=str(1)
       		else:
       			lines_mod[i]=str(0)

#########
#      	i=random.randint(0, len(lines)-1)
#      	if (lines[i]==str(1)):
#      		lines_mod[i]=str(0)
#      	elif (lines[i]==str(0)):
#      		lines_mod[i]=str(1)
#########
#      	for i in range(len(lines)):
#      		r=random.random()
#      		if (r>uniformDistributionCutOff):
#      			if (lines[i]==str(1)):
#      				lines[i]=str(0)
#      			elif (lines[i]==str(0)):
#      				lines[i]=str(1)
#########

       	"""
       	print "new ",
       	print lines_mod
       	"""

       	new_k=random.randrange(2,len(lines))

       	return lines_mod, new_k

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

#      	k=sys.argv[1]
       	k=2

       	currentScore=calcTestScoresWithPenalty(lines_0_1[0],lines_value[0])

       	rejectFlag=0

       	while (True):

       		iteration+=1

       		print
       		print "iteration "+str(iteration)
       		print

       		new_lines,k=doMCMC(lines_0_1[0],k)

       		newScore=calcTestScoresWithPenalty(new_lines,lines_value[0])

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

       	writeData(solutionfilename,lines_0_1[0])

       	f=open(iterationfile,'wb')
       	f.write("iterations: "+str(iteration)+'\n')
       	f.write("k: "+str(k)+'\n')
       	f.write("score: "+str(currentScore)+'\n')
       	f.close()

       	cmd="rm old-0-1-iter*.txt"
       	os.system(cmd)
       	cmd="rm new-0-1-iter*.txt"
       	os.system(cmd)

       	print "Final choice: ",
       	print lines_0_1[0]
