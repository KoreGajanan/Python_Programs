#Accept range from user  and perform summetion of even no from that range

#===============================
#   This function contains actual logic
#===============================
def printFactors(iStart,iEnd):

    iSumFactors=0;
    
    for i in range(iStart,iEnd+1):
        if(i%2 == 0):
            iSumFactors+=i;
        
    return iSumFactors;



#===============================
#    Entry point function
#===============================  
def main():
    iNo1 = int(input("Enter Start no \n"));
    iNo2 = int(input("Enter End no \n"));
    
    iResult=printFactors(iNo1,iNo2);  
    print("Summetion of Even no is:",iResult);
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
