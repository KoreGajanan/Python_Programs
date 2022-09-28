# Accept 'N' no from user and findout diff bet largest and smallest no


#===============================
#   This function contains actual logic
#===============================
def arrayDifference(brr):
    
    iMax=0;
    iMin=brr[0];
    
    for i in range(len(brr)):
        if iMax < brr[i]:
            iMax=brr[i];
        
        if iMin > brr[i]:
            iMin=brr[i];

    return iMax-iMin;

    
#===============================
#    Entry point function
#===============================  
def main():
    
    iNo = int(input("How many no you want to enter....\n"));
    
    arr=[];
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);
        
    
    iRet=arrayDifference(arr);
    print("Diff between Max no and Min No is: ",iRet);

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();