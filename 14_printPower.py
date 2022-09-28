# #Accept no as x & y,and generate the result as x**y
# input 2,4 =2*2*2*2
# output 16


#===============================
#   This function contains actual logic
#===============================
def power(iNo1,iNo2):
    
    iMult=1;
    for i in range(0,iNo2):
        iMult = iMult*iNo1;
    return iMult;


#===============================
#    Entry point function
#===============================  
def main():
    
    iNo1 = int(input("Enter First No: \n"));
    iNo2 = int(input("Enter Second No: \n"));
    
    iResult=power(iNo1,iNo2);
    
    print(f"Power of {iNo1} and {iNo2} is {iResult}");
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();