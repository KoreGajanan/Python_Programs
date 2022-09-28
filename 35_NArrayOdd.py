#Accpet N nos from user and display Odd nos
#input 1 2 4 8 5 6 11
#Output 1 5 11

#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    
    print("Odd no is:");
    for i in range(len(brr)):
        if(brr[i]%2==1):
            print(brr[i]);

#===============================
#    Entry point function
#===============================  
def main():
    arr=[];
    
    iNo=int(input("How many no you want to enter...\n"));
    
    print("Enter nos");
    for i in range(0,iNo):
        iValue=int(input(f"Enter {i+1} no: "))
        arr.append(iValue);
       
    arrAddition(arr);    
    
#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();



