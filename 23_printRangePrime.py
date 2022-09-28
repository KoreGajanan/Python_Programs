#Accept range from user and print all prime no
#input 1,30
#output 1,2,3,5,7,11,13,17,19,23,29

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    Flag=False;
    for i in range(iNo1,iNo2+1):
        for j in range(2,int(i/2)+1):
            if i%j ==0:
                Flag=True;
                break;
        if Flag==False:
            print(i)
        Flag=False;
   
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
