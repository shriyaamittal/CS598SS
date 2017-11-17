setwd("/Users/shriyaa/Desktop/CS598SS/project/check-MCMC")

inputfile <- "test.txt"
outputfile <- "mydata_new.txt"

R <- 35

# Use the both below variables as 1 in case of actual MCMC
num_rows <- R
num_cols <- R


mydata = read.table(inputfile,sep="\t", fill = TRUE)
mydata= mydata[, start_num_1:35]
mydata_new=mydata
for ( i in R-num_cols:R)
{
  for ( j in R-num_rows:R)
  {
    if ( !is.na(mydata[i,j]) && runif(1) >= 0.99 && mydata[i,j] == 0 )
      mydata_new[i,j] = 1
      else if (!is.na(mydata[i,j]) && runif(1) >= 0.99 && mydata[i,j] == 1)
      mydata_new[i,j] = 0
  }
}

write.table(mydata_new, outputfile, sep="\t", col.names=FALSE, row.names = FALSE)
