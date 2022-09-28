#Accept range from user and print all the no from that range
#input 1,10
#output 1,2,3,4,5,6,7,8,9,10

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    
    for i in range(iNo1,iNo2+1):
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
