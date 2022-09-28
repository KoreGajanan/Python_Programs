#Accept 10 nos from user and return addition of all nos
#input 1 2 3 4 5 6 7 8 9 10
#output 55


#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    iSum=0;
    for i in range(len(brr)):
        iSum=iSum+brr[i];

    return iSum;


#===============================
#    Entry point function
#===============================  
def main():
    arr=[];
    
    iNo=int(input("How many no you want to enter...\n"));
    
    print("Enter nos");
    for i in range(0,iNo):
        iValue=int(input(f"Enter {i+1} no: "))
        arr.append(iValue);
       
    iRet=arrAddition(arr);
    print("Addition is: ",iRet);
    
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();



