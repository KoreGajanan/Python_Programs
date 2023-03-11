# Write a program which prints five star on screen

#===============================
#this function contains actual logic
#======================

def printStar(iNo):
    print("\n")
    for ivalue in range(0,iNo):
        print(" * ",end=" ");
  
  
#========================
#entry point function 
#========================
def main():
    
    iNo = int(input("How many start you want to print   \n"));
    
    printStar(iNo);
 

 
#===========================
#           starter
#===========================
if __name__=="__main__":
    main();