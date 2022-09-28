#Accept range from user and print all the no in reverse order
#input 1,5
#output 5,4,3,2,1

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    
    for i in range(iNo2,iNo1-1,-1):
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
