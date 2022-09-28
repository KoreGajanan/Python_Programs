#Accpet two numbers from user and check whether first no is completely divisible by second no or not

#===============================
#   This function contains actual logic
#===============================

def checkDivisible(iNo1,iNo2):

    if(iNo2 > iNo1):
        return False;
    
    if(iNo1 % iNo2 == 0):
        return True;
    else:
        return False;


#===============================
#    Entry point function
#===============================

def main():
    iNo1=int(input("Enter 1st No: \n"));
    iNo2=int(input("Enter 2nd No: \n"));
    
    bRet=checkDivisible(iNo1,iNo2);
    
    if(bRet==True):
        print("No is divisible");
    else:
        print("No is not divisible");
        
        
#===============================
#      Starter
#===============================

if __name__ =="__main__":
    main();







