# Accept string and one character from user and return the first occurence of that character


#===============================
#   This function contains actual logic
#===============================
def searchCharacter(str2,ch2):
    iPos=1;
    if str2=='':
        return -1;
        
    for i in str2:
        if(i==ch2):
            break;
        iPos+=1;
    
    
    if iPos==len(str2)+1:
        return -1;
    else:
        return iPos;

#===============================
#    Entry point function
#===============================
def main():
    str1=input("Enter string....\n");
    
    ch=input("Enter character...\n");
    
    iResult=searchCharacter(str1,ch);
    
    if iResult==-1:
        print("There is no such character");
    else:
        print(f"First Occurence of character {ch}:{iResult} index");
    
#===============================
#      Starter
#===============================

if __name__=="__main__":
    main();
