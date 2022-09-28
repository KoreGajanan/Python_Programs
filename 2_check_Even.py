#Accept one number from user and we have to check whether our no is even or odd


#===============================
#   This function contains actual logic
#===============================

def checkEvenOdd(iNo):
           
    if(iNo % 2 == 0):
        return True;
    else:
        return False;
    
#===============================
#    Entry point function
#===============================

def main():
    
    iNo=int(input("Enter one number: \n"));
    
    bRet=checkEvenOdd(iNo);
    
    if(bRet==True):
        print("Entered No is Even...");
    else:
        print("Entered No is Odd...");

#===============================
#      Starter
#===============================

if __name__=="__main__":
    main();