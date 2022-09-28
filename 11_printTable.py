# # Accept no from user and print table of that number (10 multiple of that no)
# input 5
# output 5 10 15 20 25 30 . ....

#===============================
#   This function contains actual logic
#===============================

def printTable(iNo):

    print("Table of {} is:".format(iNo),"\n");
    for i in range(1,11):
        iMult=iNo * i;
        print(iMult,end=" ");

#===============================
#    Entry point function
#===============================
def main():
    iNo = int(input("Enter one no: \n"));
    
    printTable(iNo);

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();