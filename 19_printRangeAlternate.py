#Accept range from user and print alternate no 
#input 1,5
#output 1,3,5

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    
    for i in range(iNo1,iNo2+1,2):
        print(i,end=" ")
              

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
