# Accept 'N no from user and accept one no from user.check whether that no is present in array or not
# If that no is present in a array then we have to return nearest number
# Input 6 15 8 18 20 44
# No is 16
# Output:Nearest no is 15

#===============================
#   This function contains actual logic
#===============================
def searchNearest(brr,iNo1):
    
    diff=0;
    minDiff=brr[0]-iNo1;
    nearest=0;
    
    if minDiff < 0:
        minDiff=-minDiff;
    
    for i in range(len(brr)):
        
        diff=brr[i]-iNo1;
        
        if (diff < 0):
            diff=-diff;
        
        if(diff==0):
            nearest=brr[i];
            break;
        else:
            if (diff <= minDiff):
                minDiff=diff;
                nearest=brr[i];
    
    return nearest;

#===============================
#    Entry point function
#===============================
def main():
    arr=[];
    iNo=int(input("How many element you want ot enter...\n"));
    
    for i in range(iNo):
        iValue=int(input(F"Enter {i+1} No:"));
        arr.append(iValue);
        
    
    iNo1=int(input("Enter number you want to search in list..\n"));
    
    iResult=searchNearest(arr,iNo1);
   
    print(f"Nearest number is:{ iResult }");
    
#===============================
#      Starter
#===============================   
if __name__=="__main__":
    main();
