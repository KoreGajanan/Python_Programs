# Accept two numbers from user and check whether that 1st number is completely divisible by 2nd or not

#===============================
#   This function contains actual logic
#===============================
def checkDivisible(iNo1,iNo2):
    if(iNo1 % iNo2 == 0):
        return True;
    else:
        return False;
        
#===============================
#    entry point function
#===============================

def main():
    iNo1 = int(input("Enter first no.  \n"));
    iNo2 = int(input("Enter second no.  \n"));
    
    bRet = checkDivisible(iNo1,iNo2);
    
    if(bRet == True):
        print("First no is completely divisible by second no..");
    else:
        print("First no is not divisible by second no.....");

#===============================
#      starter
#===============================

if __name__=="__main__":
	main();