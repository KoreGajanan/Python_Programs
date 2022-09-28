#Accpet N nos from user and display all such consqutive pairs 
#of nos whoes addition is  equal to next no.
#Input: 7 2 8 10 -19 -9 1 50 51 101 80
#Output 2+8=10,      1+50=51 
#      10+(-19)=-9,  50+51=101

#===============================
#   This function contains actual logic
#===============================
def pairSum(brr):
        
    for i in range(len(brr)-2):
        
        if brr[i]+brr[i+1]==brr[i+2]:
            print(F"Addition of {brr[i]} + { brr[i+1]}=={brr[i+2]} \n");

#===============================
#    Entry point function
#===============================
def main():
    
    iNo=int(input("How many number you want to enter...\n"));
    
    arr=[];
    
    for i in range(iNo):
        iValue=int(input(F"Enter {i+1} no: "));
        arr.append(iValue);
    
    pairSum(arr);    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
