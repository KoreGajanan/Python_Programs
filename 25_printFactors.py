#Accept range from user  and perform summetion of all such nos which are factors of that nos as well as summetion
# of all such nos which are not factors of that no. and return diff bet both the summetion

#===============================
#   This function contains actual logic
#===============================
def printFactors(iStart,iEnd):

    iSumFactors=iSumFactors1=0;
    
    for i in range(iStart,iEnd+1):
        for j in range(1,i+1):
            if(i%j == 0):
                iSumFactors+=j;
            else:
                iSumFactors1+=j;
    
    print("Addition of factors is:",iSumFactors);
    print("Addition of non-factors is:",iSumFactors1);
    return iSumFactors-iSumFactors1;



#===============================
#    Entry point function
#===============================  
def main():
    iNo1 = int(input("Enter Start no \n"));
    iNo2 = int(input("Enter End no \n"));
    
    iResult=printFactors(iNo1,iNo2);  
    print("Difference between Factors and Non-Factors is:",iResult);
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
