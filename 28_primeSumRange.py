# Accept range from user and return summetion of prime no's from that range


#===============================
#   This function contains actual logic
#===============================
def printPrime(iStart,iEnd):
    
    iSum=0;
    Flag=False;
    for i in range(iStart,iEnd+1):
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                Flag=True;
                break;
        
        if(Flag==False):
            iSum=iSum+i;
        
        Flag=False;
    
    return iSum;

#===============================
#    Entry point function
#===============================  
def main():
    iNo1 = int(input("Enter Start no \n"));
    iNo2 = int(input("Enter End no \n"));
    
    iResult=printPrime(iNo1,iNo2);  
    print("Summetion of all Prime no is:",iResult);
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
