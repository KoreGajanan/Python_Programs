# Accept 'N' no from user and print such no from array whoes 
# magnitude is eqaul to multiplication of its immidiate neighour
# Input: 3 2 4 2 12 6 4 40 10
# output 2*2=4 2*6=12 4*10=40


#===============================
#   This function contains actual logic
#===============================
def patternMultiply(brr):
    
    print("\nPairs of magnitude are...\n");
    for i in range(len(brr)-2):
        if(brr[i]*brr[i+2]==brr[i+1]):
            print(f"{brr[i]}*{brr[i+2]}=={brr[i+1]}");

#===============================
#    Entry point function
#===============================
def main():
    
    iNo = int(input("How many no you want to search...\n"))
    
    arr=[]
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "));
        arr.append(iValue);

    patternMultiply(arr);

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();


