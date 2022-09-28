#Accept 10 nos from user and print all prime no
#input 12 2 4 5 7 9 10 13 17 19
#output 2 5 7 13 17 19


#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    Flag=False;
    print("Prime nos is:");
    for i in range(len(brr)):
        for j in range(2,int(brr[i]/2)+1):
            if(brr[i]%j==0):
                Flag=True;
                break;
        if(Flag==False):
            print(brr[i]);
        Flag=False;
        

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



