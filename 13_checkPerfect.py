# Accept no from user and check whether that no is perfect no or not
# input 6
# output It is a perfect no
# input 13
# output It is not a perfect no


#===============================
#   This function contains actual logic
#===============================
def checkPerfect(iNo):
    
    if(iNo <= 0):
        return False;
    iSum=0;
    
    for i in range(1,iNo):
        if(iNo%i == 0) and (iSum <= iNo):
            iSum=iSum+i;
    
    if(iSum == iNo):
        return True;
    else:
        return False;
        
        
#===============================
#    Entry point function
#===============================          
def main():
    
    iNo=int(input("Enter one no: \n"));
    
    bResult=checkPerfect(iNo);
    if(bResult == True):
        print("It is a perfect no..");
    else:
        print("It iS not a perfect no..");

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();