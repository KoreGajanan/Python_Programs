# Accept N no from user and return 2nd max no 
#Input: 10,52,32,99,19,36
#Output: 52

#===============================
#   This function contains actual logic
#===============================
def secMax(brr):
    
    fMax=brr[0];
    sMax=brr[1];
    
    for i in range(len(brr)):
        if fMax < brr[i]:
            sMax=fMax;
            fMax=brr[i];
        elif(sMax < brr[i] and fMax != brr[i]):
            sMax=brr[i];

    return sMax;

#===============================
#    Entry point function
#===============================

def main():
    iNo=int(input("How many no you want to enter....\n"));
    
    arr=[];
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);

    iRes=secMax(arr);
    print("Second maximum no is: ",iRes);


#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();