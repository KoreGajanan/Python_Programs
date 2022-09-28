# Accept two numbers from user and find maximum number

#===============================
#   This function contains actual logic
#===============================

def maxNumber(iNo1,iNo2):
    
    if(iNo1 < 0 or iNo2 < 0):
        return;
    
    if(iNo1 > iNo2):
        return iNo1;
    else:
        return iNo2;

#===============================
#    Entry point function
#===============================
def main():
    iNo1 = int(input("Enter one number \n"));
    iNo2 = int(input("Enter second number  \n"));
    
    iRet = maxNumber(iNo1,iNo2);
    
    print("Maximum number is: ",iRet);


#===============================
#      Starter
#===============================

if __name__ == "__main__" :
    main();
    
    