#Accept range from user and print all such no's which are divisible by 3
#input 1,16
#output 3,6,9,12,15

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    
    for i in range(iNo1,iNo2+1):
        if i%3==0:
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
