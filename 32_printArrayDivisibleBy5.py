#Accept 10 nos from user and print all nos which are which are divisible by 5 and greater than 50
#input 55 50 49 100 99 25 35 90 80 84
#output 50 100 90 80


#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    
    print("Nos which are divisible by 5 and greater than 50 is:");
    for i in range(len(brr)):
        if(brr[i]%5==0 and brr[i]>50):
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



