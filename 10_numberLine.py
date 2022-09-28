# Accept no from user and print its no line
# input 3
# output -3 - 2 -1 0 1 2 3

#===============================
#   This function contains actual logic
#===============================

def numberLine(iNo):

    for i in range(-iNo,iNo+1):
        print(i,end=" ");

#===============================
#    Entry point function
#===============================

def main():
    
    iNo = int(input("Enter one no: \n"));
    numberLine(iNo);

#===============================
#      Starter
#===============================

if __name__=="__main__":
    main();