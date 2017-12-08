k=10
case2_itr_mtrx_595=matrix(0,50,5)

for(j in 1:5){
rundatasize=paste0("data_size595_",j)
wd1=paste0("C:\\Users\\Zainab\\Desktop\\CS598\\BigData\\",rundatasize)
setwd(wd1)
values=read.table('values.txt')
max_sum={}
for(m in 1:k)
{
  max_sum[m]=max(values)
  values=values[-which.max(values)]
}

for(i in 1:10){
runfile=paste0("run_",i)
wd=paste0( wd1,"\\output_files\\",runfile)
setwd(wd)
itr=read.table('iterations.txt', sep = " ",header = F )
case2_itr_mtrx_595[10*(j-1)+i,2:4]=t(itr[,2])
case2_itr_mtrx_595[10*(j-1)+i,1]=i
case2_itr_mtrx_595[10*(j-1)+i,5]=sum(max_sum)
}
}
case2_itr_mtrx=rbind(case2_itr_mtrx_5,case2_itr_mtrx_10,case2_itr_mtrx_15,case2_itr_mtrx_20)
case2_itr_mtrx=data.frame(case2_itr_mtrx)

###checkforconverge
case2_itr_mtrx[,6]=case2_itr_mtrx[,5]-case2_itr_mtrx[,4]


###col7
for(i in 1:4)
{case2_itr_mtrx[(1+(i-1)*50):(50+(i-1)*50),7]=len[i]

}
len=seq(5,20,5)
restriction=seq(2,4,2)
array_4=matrix(0,length(len),2)

for (j in 1:length(len)){
  count=0
for (i in 1: nrow(Book2)){ 

  if((Book2$k[i]==4 && Book2$length[i]==len[j] && Book2$converge[i]==1)==TRUE)
   count=count+1
}
 
array_4[j,1]=len[[j]]
array_4[j,2]=count
}
   max(array_2[,2])
  plot(array_2[,1],array_2[,2]/max(array_2[,2]), pch=1, col=1,xlab = "Length of the array", ylab ="Frequency of number of times converged to maximum sum", ylim=c(0,1))
  points(array_2[,1],array_4[,2]/max(array_4[,2]),pch=2, col=2,xlab = "Length of the array", ylab ="Frequency of number of times converged to maximum sum")
  title("Convergence to correct sum")
  leg.txt=c("k=2", "k=4")
  legend( 17, 1,legend = leg.txt, col = 1:2, pch = 1:2,
         lty = 1, merge = TRUE)   #, trace = TRUE)
  
###iterations
  array_4_itr=matrix(0,sum(Book2$k==4),2)
  
  for (j in 1:length(len)){
    for (i in 1: nrow(Book2)){ 
      
      if((Book2$k[i]== 4 && Book2$length[i]==len[j] && Book2$converge[i]==1)==TRUE)
        {
        array_4_itr[i-200,2]=Book2$iteration[i]
        array_4_itr[i-200,1]=len[[j]]
        }
      }
   
  }
  hist(array_4_itr[array_4_itr[,1]==20,][,2], xlim=c(0,50000) ,ylim=c(0,5),xlab="Number of iterations to convergence", main ="k=4, length=20")

  array_4_itr_mean=matrix(0,length(len),2)
  for(i in 1:length(len))
  {  array_4_itr_mean[i,1]=len[i]
    array_4_itr_mean[i,2]=sum((array_4_itr[array_4_itr[,1]==len[i],][,2]))/sum(array_4_itr[,1]==len[i])
  }

  plot(array_2[,1], array_2_itr_mean[,2],pch=1, col=1,xlab = "Length of the array", ylab ="Frequency of number of times converged to maximum sum", ylim= c(0,30000)) 
  points(array_2[,1], array_4_itr_mean[,2],pch=2, col=2,xlab = "Length of the array", ylab ="Frequency of number of times converged to maximum sum") 
  title("Mean number of iterations to convergence")
  leg.txt=c("k=2", "k=4")
  legend( 17, 30000,legend = leg.txt, col = 1:2, pch = 1:2,
          lty = 1, merge = TRUE)   #, trace = TRUE)
  
  
  setwd("C:\\Users\\Zainab\\Desktop\\CS598\\BigData")
  colnames(case2_itr_mtrx_595)=c("run","iterations", "k", "sum", "max_sum")
  write.table(case2_itr_mtrx_595,'595run.txt')
  ##########
  
  colnames(case2_itr_mtrx)=c("run","iterations", "k", "sum", "max_sum","converge", "lenght_array")
  case2_itr_mtrx$converge=ifelse(case2_itr_mtrx$converge==0,0,1)
  mydata=case2_itr_mtrx[1:200,]
  case3_plots=matrix(0, length(len),4)
  for(i in 1:length(len))
  {
    case3_plots[i,1]=len[i]
    case3_plots[i,4]=length(which(mydata$converge==0)[mydata$lenght_array==len[i]])/length(which(mydata$lenght_array==len[i]))
  }
  setwd("C:\\Users\\Zainab\\Desktop\\CS598\\TestCaseData")
  for( i in 2:4)
  {  
  plot(case3_plots[,1],case3_plots[,i], ylim=c(0,1.2), ylab="Frequency", xlab= "Array length")
  ttle=paste0("k=",i)
  title(ttle)
  savePlot(filename=ttle,type=c("jpg"),device=dev.cur())
  }
  
  case2_plots=matrix(0,length(len),4)
  names(mydata)
  for(i in 1:length(len)){
  case2_plots[i,1]=len[i]
  case2_plots[i,2]=mean(mydata[mydata$length==len[i],]$iteration)
  case2_plots[i,3]=mean(mydata[mydata$length==len[i],]$k)
  case2_plots[i,4]=mean(mydata[mydata$length==len[i],]$score)
  }
  plot(case2_plots[,1],case2_plots[,2], pch="#", col=2, xlab="length of array", ylab="mean iterations")
  title("Mean Iterations")
  plot(case2_plots[,1],case2_plots[,3], pch="#", col=2, xlab="length of array", ylab="mean k value")
  title("Mean k")
  plot(case2_plots[,1],case2_plots[,4], pch="#", col=2, xlab="length of array", ylab="mean score")
  title("Mean score")
  
  
  
  
  ####
  case2_itr_mtrx_595=data.frame(case2_itr_mtrx_595)
  case2_itr_mtrx_595[,6]=case2_itr_mtrx_595[,4]/case2_itr_mtrx_595[,5]
  for(i in 1:5)
  case2_itr_mtrx_595[(1+(i-1)*(10)):(i*10),7]=i
  colnames(case2_itr_mtrx_595)=c("run","iterations", "k", "sum", "max_sum","converge", "array")
  par( mfrow = c( 2, 3 ) )
  mydata=case2_itr_mtrx_595
  
  #plot(mydata$run[mydata$array==1], mydata$converge[mydata$array==1], col=1,xlim=c(1,10), ylim=c(0,1), xlab="Run", ylab= "Sum of run/Maximum Sum")
  for (i in 1:5)
  {
    plot(mydata$run[mydata$array==i], mydata$converge[mydata$array==i], col=i  ,xlim=c(1,10), ylim=c(0,1), xlab="Run", ylab= "Sum of run / Maximum Sum")
    points(which.max(mydata$converge[mydata$array==i]), max(mydata$converge[mydata$array==i]), pch=19, col=1)
    tle=paste0("Array ", i)
    title(tle)
  }
 
  legend(8,0.4, legend = 1:5, col=1:5, pch="__") 
  title("Run with maximum return sum ")
  