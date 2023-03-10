#Accept marks from user and calculate the percentage


#========================
#entry point function 
#========================
def main():
    iMarks = int(input("Enter marks \n"));
    
    fResult = calPerc(iMarks,1000);
    
    displayRes(fResult);


#================================
#This function calculate percentage

def calPerc(iObtain,iTotal):
    
    fAns = float(iObtain)/float(iTotal) *100;
    
    return fAns;

#===============================
#This function display result as per class 

def displayRes(fInput):
    if(fInput >= 70):
        print("Distinction \n");
    elif(fInput >= 60):
        print("Firs class \n");
    elif(fInput >= 50):
        print("Second class \n");
    elif(fInput >= 40):
        print("Pass class \n");
    else:
        print("Fail");


#===========================
#           starter
#===========================
if __name__=="__main__":
    main();