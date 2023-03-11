#Accept no from user and prints its factors

#this function contains logic
def printFactors(iNo):
    for iCnt in range(1,int(iNo/2+1)):
        if(iNo % iCnt == 0 ):
            print(iCnt,end=" ");
    

#entry point function
def main():
    iNo =int(input("Enter number  \n"));
    
    printFactors(iNo);

#========================
#starter
#=======================
if __name__=="__main__":
    main();