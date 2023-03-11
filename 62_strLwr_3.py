# Accept string from user and convert every capital case character into small case character


#===============================
#   This function contains actual logic
#===============================
def searchCharacter(str2):
              
    for i in str2:
        if(i >='A' and i <= 'Z' ):
            str2=str2+str(32);
        
   
    return str2;

#===============================
#    Entry point function
#===============================
def main():
    str1=input("Enter string....\n");
    
    iResult=searchCharacter(str1);
    
    print(f"Convert string is:{iResult}");
    

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();
