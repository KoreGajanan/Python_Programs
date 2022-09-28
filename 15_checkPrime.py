# Accept no from user and check whether that no is prime or not
#input 7
#output It is a prime no
#input 12
#output It is not a prime no

#===============================
#   This function contains actual logic
#===============================
def checkPrime(iNo):
    
    flag=False;
    for i in range(2,int(iNo/2)+1):
        if(iNo%i == 0):
            flag=True;
            break;
    return flag;


#===============================
#    Entry point function
#===============================  
def main():
    
    iNo = int(input("Enter one number:  \n"));
    
    bRes = checkPrime(iNo);
    if(bRes == True):
        print("Entered no is not prime...");
    else:
        print("Entered no is prime...");


#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
    