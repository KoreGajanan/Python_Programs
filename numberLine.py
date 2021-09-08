#//Accept no from user and print its number line 
#// input 3
#// output -3 -2 -1 0 1 2 3


#this function contains logic
def numberLine(iNo):
    for i in range((-iNo),iNo+1):
        print(i,end=" ");


#entry point function
def main():
    iNo =int(input("Enter number  \n"));
    
    numberLine(iNo);


#========================
#starter
#=======================
if __name__=="__main__":
    main();