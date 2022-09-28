# Accept array from user and check whether array is sorted in increasing order or not
# input 2 4 6 5 5 8
# Output Array is not sorted
# input 2 4 6 8 9 11
# Output Array is sorted

#===============================
#   This function contains actual logic
#===============================
def arraySorted(brr):
    
    for i in range(len(brr)-1): 
        
        if brr[i] > brr[i+1]:
            break;
    
    if i==len(brr)-2:
        return True;
    else:
        return False;


#===============================
#    Entry point function
#===============================  
def main():
    
    iNo = int(input("How many no you want to enter.....\n"))
    
    arr = [];
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);
    
    bRet = arraySorted(arr);
    
    if bRet==True:
        print("Array is sorted..!");
    else:
        print("Array is not sorted..!");

#===============================
#      Starter
#===============================

if __name__ == "__main__":
    main();