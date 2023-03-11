#Accept Two numbers from user and return maximum number

#===============================
#   This function contains actual logic
#===============================
def maximum(iNo1,iNo2):
    if iNo1 > iNo2 :
        return iNo1;
    else:
        return iNo2;


#===============================
#    entry point function
#===============================
def main():
    
    iNo1 = int(input("Enter First number..\n"));
    iNo2 = int(input("Enter Second number..\n"));
    
    iResult = maximum(iNo1,iNo2);
    
    print("Maximum number is ", iResult);

#===============================
#      starter
#===============================
if __name__=="__main__":
	main();