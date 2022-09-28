#Accept 10 nos from user and print all nos which are greater than 20 and less than 40
#input 20 40 50 30 12 25 35 40 21 39
#output 30 25 35 21 39


#===============================
#   This function contains actual logic
#===============================

def arrAddition(brr):
    
    print("Nos which are greater than 20 and less than 40 is:");
    for i in range(len(brr)):
        if(brr[i] > 20 and brr[i]<40):
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



