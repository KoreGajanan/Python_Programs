# Accept no from user and print its factors
# input 36
# output 1,2,3,4,6,9,12,18

#===============================
#   This function contains actual logic
#===============================

def printFactor(iNo):
    
    if(iNo <= 0):
        return;
    print("Factors of {} is:".format(iNo),"\n");
    for i in range(1,int(iNo/2)+1):
        if(iNo%i == 0):
            print(i,end=" ");
  
#===============================
#    Entry point function
#===============================  

def main():
    
    iNo=int(input("Enter one no: \n"));
    
    printFactor(iNo);
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
    
    
    
