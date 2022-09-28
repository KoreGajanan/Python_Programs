# Accept two nos from user and print largest common factors.
# input 21,28
# output 7

#===============================
#   This function contains actual logic
#===============================
def commonLargestFactor(iValue1,iValue2):
    iCnt=1;factor=0;
    
    # while((iCnt <= int(iValue1/2))and(iCnt <=int(iValue2/2))):
        
        # if(iValue1%iCnt == 0 and iValue2%iCnt==0):
            # factor=iCnt;
        
        # iCnt+=1;
    
    for i in range(1,int((iValue1/2)+1 and int(iValue2/2)+1)):
        if(iValue1%iCnt == 0 and iValue2%iCnt==0):
            factor=iCnt;
        
        iCnt+=1;
    
    return factor;

#===============================
#    Entry point function
#===============================
def main():
    iNo1=int(input("Enter First no: "));
    iNo2=int(input("Enter Second no: "));
    
    iResult=commonLargestFactor(iNo1,iNo2);
    
    print("Largest common factor is: ",iResult);


#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();


