#Accpet no from user and print all the digits from 1 to that no

#===============================
#   This function contains actual logic
#===============================

def displayDigit(iNo):
    
    if(iNo <= 0):
        return;
    
    print("Digit 1 from",iNo,"\n");
    for i in range(1,iNo+1):
        print(i);

#===============================
#    Entry point function
#===============================

def main():
    
    iNo = int(input("Enter one no:  \n"));
    
    displayDigit(iNo);

#===============================
#      Starter
#===============================

if __name__=="__main__":
    
    main();
    