#Accept marks from user and calculate the percentage 
#Dispaly result as
# % > 70 Distinction
# % > 60 First Class
# % > 50 Second Class
# % > 40 Pass Class
# % < 40 Fail

#===============================
#   This function calculate percentage of marks
#===============================

def calculatePercentage(iNo,iTotal):
    
    fAns=(iNo/iTotal*100);
    return fAns;

#===============================
#   This function display class
#===============================

def displayResult(fInput):
    
    if(fInput >= 70):
        print("Distinction...");
    elif(fInput >= 60):
        print("First Class...");
    elif(fInput >= 50):
        print("Second Class");
    elif(fInput >= 40):
        print("Pass Class");
    else:
        print("Fail...")
    
#===============================
#    Entry point function
#===============================

def main():
    
    iNo = int(input("Enter Marks:  \n"));
    
    fResult=calculatePercentage(iNo,1000);
    
    displayResult(fResult);
    

#===============================
#      Starter
#===============================

if __name__ == "__main__":
    
    main();