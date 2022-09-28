#Accept range from user and print all perfect no
#input 1,30
#output 6,28

#===============================
#   This function contains actual logic
#===============================
def printRange(iNo1,iNo2):
    iSum=0;
    for i in range(iNo1,iNo2+1):
        for j in range(1,int(i/2)+1):
            if i%j ==0:
                iSum=iSum+j;
        if iSum==i:
            print(i)
        iSum=0;
   
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
