import random
import time
import os

random.seed(time.time())

#fileSizes=[2,3,4,5,10,15]
fileSizes=[2,3,4,5]
numCasesEachFileSize=5

if __name__ == "__main__":

       	for i in range(len(fileSizes)):
       		for j in range(numCasesEachFileSize):
       			test_case_num=j+1
       			test_case_size=fileSizes[i]

       			print test_case_num, test_case_size

       			dirname="data_size"+str(test_case_size)+"_"+str(test_case_num)
       			cmd="mkdir "+dirname
       			os.system(cmd)
       			os.chdir("./"+dirname)

       			f=open('test.txt','wb')

       			for m in range(test_case_size-1):
       				x=random.randint(0,1)
       				f.write(str(x)+'\t')

       			x=random.randint(0,1)
       			f.write(str(x)+'\n')
       			f.close()

       			f=open('values.txt','wb')

       			for m in range(test_case_size-1):
       				x=random.randrange(0,20)
       				f.write(str(x)+'\t')

       			x=random.randrange(0,20)
       			f.write(str(x)+'\n')
       			f.close()

       			os.chdir("../")
