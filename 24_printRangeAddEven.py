#Accept range from user and print addition of even no's
#input 1,16
#output 72

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    iSum=0;
    for i in range(iNo1,iNo2+1):
        if i%2==0:
            iSum=iSum+i;
    
    print("Addition of even no is:",iSum);
              

#===============================
#    Entry point function
#===============================  
def main():
    iNo1 = int(input("Enter Start no \n"));
    iNo2 = int(input("Enter End no \n"));
    
    printRange(iNo1,iNo2);  
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
