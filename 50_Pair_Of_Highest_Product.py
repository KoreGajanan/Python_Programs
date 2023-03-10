# write a program for finding pair of highest product

# input =[5,3,1,4,3,7,6,9,2]
# output = Maximum product pair is: (7,9)

# input=[0,-2,-1,-4,5,-8,7,-8,8]
# output= Maximum product pair is:  (-8,-8)


#===============================
#   This function contains actual logic
#===============================

def maxProduct(arr):
    iValue1=arr[0]
    iValue2=arr[1]

    for i in range(0,len(arr)):
        
        for j in range(i+1,len(arr)):
            
            if arr[i]*arr[j] > (iValue1*iValue2) :
                iValue1=arr[i]
                iValue2=arr[j]
              
    return iValue1,iValue2

#===============================
#    Entry point function
#===============================

def main():
    iNo=int(input("How many number you want to enter in a list: "))
    
    arr=[]
    print("Enter No's: \n")
    
    for i in range(iNo):
        iValue=int(input(f"Enter {i+1} no: "))
        arr.append(iValue)
    
    iResult=maxProduct(arr)
    print(f'Max prduct pair is: { iResult}')


#===============================
#      Starter
#===============================

if __name__=="__main__":
    main()