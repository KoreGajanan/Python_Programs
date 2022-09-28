#Accpet N nos from user and return minimum no
#input 1 2 4 8 5 6 11
#Output 1


#===============================
#   This function contains actual logic
#===============================
def arrMinimum(brr):
    
    iMin=brr[0];
    
    for i in range(len(brr)):
        if(iMin > brr[i]):
            iMin=brr[i];

    return iMin;

    
#===============================
#    Entry point function
#===============================  
def main():
    arr=[];
    
    iNo = int(input("How many many no you want to enter... \n"))
    
    print("Enter nos...");
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);

    iRet=arrMinimum(arr);
    print("Minimum no is:",iRet);

#===============================
#      Starter
#===============================
if __name__ =="__main__":
    main()