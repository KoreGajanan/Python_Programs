# Accept N no from user and replace every duplicate occurence of no with zero
# input 5 4 0 5 8 2 5 8
# output 5 4 0 0 8 2 0 0

#===============================
#   This function contains actual logic
#===============================
def duplicateRemove(brr):
    
    for i in range(len(brr)-1):
        if (brr[i]==0):
            continue;
        for j in range(i+1,len(brr)):
            if (brr[j]==0):
                continue;
            if (brr[i]==brr[j]):
                brr[j]=0;

    return brr;

#===============================
#    Entry point function
#===============================
def main():
    
    iNo=int(input("How many no you want to enter...\n"));
    arr=[];
    
    for iValue in range(iNo):
        iCnt=int(input(f"Enter {iValue+1} no: "));
        arr.append(iCnt);
    
    iResult=duplicateRemove(arr);
    
    print(f"After remove duplicate element: {iResult}");


#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();