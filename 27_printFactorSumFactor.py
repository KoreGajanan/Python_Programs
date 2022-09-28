# Accept no from user and return diff between summetion of all factors no's and non factors nos

#===============================
#   This function contains actual logic
#===============================
def printFactors(iNo):

    iSumFactors=0;
    iSumFactors1=0;
    
    for i in range(1,iNo+1):
        if(iNo%i== 0):
            iSumFactors+=i;
        else:
            iSumFactors1+=i;
    return iSumFactors-iSumFactors1;



#===============================
#    Entry point function
#===============================  
def main():
    iNo = int(input("Enter Start no \n"));
    
    
    iResult=printFactors(iNo);  
    print("Summetion of Even no is:",iResult);
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
