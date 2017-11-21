from readData import *
import numpy as np
import random
import time
import os

random.seed(time.time())

uniformDistributionCutOff=0.9

iterationsForConvergence=20

inputfilename='/Users/shriyaa/Desktop/CS598SS/project/my-mcmc-code/test.txt'
inputvaluefilename='/Users/shriyaa/Desktop/CS598SS/project/my-mcmc-code/values-01.txt'

def calcTestScoresWithPenalty(lines_0_1,lines_value):
       	sumScore=0
       	count=0
       	for i in range(len(lines_0_1)):
       		if (lines_0_1[i]==str(1)):
       			sumScore+=float(lines_value[i])
       			count+=1
       	return sumScore-count

def calcTestScores(lines_0_1,lines_value):
       	sumScore=0
       	for i in range(len(lines_0_1)):
       		if (lines_0_1[i]==str(1)):
       			sumScore+=float(lines_value[i])
       	return sumScore

def doMCMC(lines):
       	i=random.randint(0, len(lines)-1)
       	if (lines[i]==str(1)):
       		lines[i]=str(0)
       	elif (lines[i]==str(0)):
       		lines[i]=str(1)

#      	for i in range(len(lines)):
#      		r=random.random()
#      		if (r>uniformDistributionCutOff):
#      			if (lines[i]==str(1)):
#      				lines[i]=str(0)
#      			elif (lines[i]==str(0)):
#      				lines[i]=str(1)
       	return lines

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

if __name__ == "__main__":

       	iteration=0

       	oldFilename=inputfilename
       	lines_value=readData(inputvaluefilename)
       	lines_0_1=readData(oldFilename)
       	currentScore=calcTestScores(lines_0_1[0],lines_value[0])

       	rejectFlag=0

       	while (True):
       		iteration+=1

       		new_lines=doMCMC(lines_0_1[0])
       		newScore=calcTestScores(new_lines,lines_value[0])

       		flagAcceptReject=checkAcceptReject(currentScore,newScore)

       		print currentScore
       		print newScore
       		print flagAcceptReject

       		if flagAcceptReject=="Accept":
       			rejectFlag=0
       			oldFilename="old-0-1-iter"+str(iteration)+'.txt'
       			newFilename="new-0-1-iter"+str(iteration)+'.txt'
       			cmd="cp "+inputfilename+" "+oldFilename
       			os.system(cmd)
       			f=open(newFilename,'wb')
       			for i in range(len(new_lines)):
       				f.write(new_lines[i]+'\t')
       			f.close()
       			currentScore=newScore
       		else:
       			rejectFlag+=1
       			if (rejectFlag==iterationsForConvergence):
       				break;

       	print "Final score: "+str(currentScore)
