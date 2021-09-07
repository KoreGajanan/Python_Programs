# Accept One numbers from user and check whether that number is even or odd

#===============================
#   This function contains actual logic
#===============================

def checkEven(iNo):
    if(iNo % 2 == 0 ):
        return True;
    else:
        return False;


#===============================
#    entry point function
#===============================
def main():
    iNo = int(input('Enter one number .\n'));
    
    bRet = checkEven(iNo);
    
    if(bRet == True):
        print('Number is even..');
    else:
        print('Number is odd..');


#===============================
#      starter
#===============================
if __name__=="__main__":
	main();