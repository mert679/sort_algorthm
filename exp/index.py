#C-COM-Sorting (2 points) Sorting algorithm

FILE="inputfile.txt"

with open(FILE) as file:

    num =file.read().split("\n")
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]<num[j]:
                num[i],num[j]=num[j],num[i]
    
    with open("outputfile.txt","w") as f:
        for i in num:
            f.write("%s\n" % i)
  
    
