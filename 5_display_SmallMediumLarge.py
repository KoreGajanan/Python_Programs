#Accept no from user and display below output
# if no is less than 50 then display small
# if no is greater than 50 and less than 100 then display medium
# if no is greater than 100 then display large


#===============================
#   This function contains actual logic
#===============================

def displayResult(iNo):
    
    if(iNo < 50 ):
        print("Small");
    elif(iNo >= 50 and iNo <= 100 ):
        print("Medium");
    else:
        print("Large");


#===============================
#    Entry point function
#===============================
def main():
    
    iNo=int(input("Enter one no: \n"));
    displayResult(iNo);


#===============================
#      Starter
#===============================
if __name__ =="__main__":
    main();