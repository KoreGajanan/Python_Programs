# Accept no from user and print all the digits from 1 to that no

#this function contains logic
def printDigit(iNo):
    
    for i in range(1,iNo+1):
        print(i,end=" ");


#entry point function
def main():
    iNo =int(input("Enter number  \n"));
    
    printDigit(iNo);


#========================
#starter
#=======================
if __name__=="__main__":
    main();