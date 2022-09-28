# Accpet n no from user and check whether that array is palindrom or not
# input 10 20 30 30 20 10
# output list is palindrom

#===============================
#   This function contains actual logic
#===============================
def palindrom(brr):
    
    i=0;j=len(brr)-1;
    
    while(i<j):
        if brr[i]!=brr[j]:
            break;
        
        i+=1;
        j-=1;
    
    if(i>=j):
        return True;
    else:
        return False;

#===============================
#    Entry point function
#===============================
def main():

    iNo=int(input("Enter how many no you want to search....\n"));
    
    arr=[];
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);

    iResult=palindrom(arr);
    
    if iResult==True:
        print("Array is Palindrom...!");
    else:
        print("Array is not Palindrom...!");


#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
