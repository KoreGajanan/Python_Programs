#Accpet N nos from user and return addition of all even nos
#input 1 2 4 8 5 6 
#Output 20

#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    iSum=0;
    for i in range(len(brr)):
        if(brr[i]%2==0):
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
    print("Addition of Even no is: ",iRet);
    
    
#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();



