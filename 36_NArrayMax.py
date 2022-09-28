#Accpet N nos from user and return maximun no
#input 1 2 4 8 5 6 11
#Output 11

#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    iMax=0;
    
    for i in range(len(brr)):
        if(iMax <= brr[i]):
            iMax = brr[i];
    return iMax;
    
#===============================
#    Entry point function
#===============================  
def main():
    arr=[];
    
    iNo=int(input("How many no you want to enter...\n"));
    
    print("Enter nos..");
    for i in range(0,iNo):
        iValue=int(input(f"Enter {i+1} no: "))
        arr.append(iValue);
       
    iRet=arrAddition(arr);  
    print("Maximum no is:",iRet);
    
#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();



