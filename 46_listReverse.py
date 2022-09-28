#Accept N no from user and reverse that array in place...
# input  10 20 30 40 50
# output 50 40 30 20 10


#===============================
#   This function contains actual logic
#===============================
def arrayReverse(brr):
    temp=0;
    i=0;
    j=len(brr)-1;
    
    while(i<j):
        temp=brr[i];
        brr[i]=brr[j];
        brr[j]=temp;
        i+=1;
        j-=1;
    
    return brr;

#===============================
#    Entry point function
#===============================
def main():

    iNo=int(input("Enter how many no you want to search....\n"));
    
    arr=[];
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);

    
    
    iResult=arrayReverse(arr);
    
    print(f"Reverse array is:{iResult}");

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();