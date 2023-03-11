#Accept no from user and print table of that number (10 multiple of that number)

#this function contains logic
def printTable(iNo):
    
    for iCnt in range(1,11):
        iMult = iCnt*iNo;
        print(iMult,end=" ");


#entry point function
def main():
    iNo =int(input("Enter number  \n"));
    
    printTable(iNo);


#========================
#starter
#=======================
if __name__=="__main__":
    main();