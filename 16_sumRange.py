#Accept range from user and perform addition of all the element in that range
#input 1,10
#output 55


#===============================
#   This function contains actual logic
#===============================

def sumRange(iNo1,iNo2):
    
    if(iNo1 > iNo2):
        return -1;
    
    iSum=0;
    
    for i in range(iNo1,iNo2+1):
        iSum=iSum+i;
    
    return iSum;
    

#===============================
#    Entry point function
#===============================  
def main():
    iNo1 = int(input("Enter Start no \n"));
    iNo2 = int(input("Enter End no \n"));
    
    iRet=sumRange(iNo1,iNo2);
    
    print("Addition of that range is:",iRet);
    
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();