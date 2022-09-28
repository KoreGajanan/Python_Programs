# Accept two nos from user and print smallest common factors.
# input 21,28
# output 7

#===============================
#   This function contains actual logic
#===============================
def commonSmallestFactor(iValue1,iValue2):
    iCnt=2;
    
    while((iCnt <= int(iValue1/2))and(iCnt <=int(iValue2/2))):
        
        if(iValue1%iCnt == 0 and iValue2%iCnt==0):
            break;
        
        iCnt+=1;
    
    if iCnt==int(iValue1/2)+1 or iCnt==int(iValue2/2)+1:
        return 0;
    else:
        return iCnt;
#===============================
#    Entry point function
#===============================
def main():
    iNo1=int(input("Enter First no: "));
    iNo2=int(input("Enter Second no: "));
    
    iResult=commonSmallestFactor(iNo1,iNo2);
    
    print("Smallest common factor is: ",iResult);


#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();


