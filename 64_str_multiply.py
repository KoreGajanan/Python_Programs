## Accept one string from user and print below pattern/output
# input-abcaba
# output-abcaabbaaa

#===============================
#   This function contains actual logic
#===============================
def string_multiply(str1):
    fString=''
    dict1={};
    for char in str1:
        if char not in dict1:
            dict1[char]=1
            fString=fString+char
        else:
            dict1[char]+=1
            fString=fString+char*dict1[char];
    return fString
    
#===============================
#    Entry point function
#===============================
def main():
    string = input("Enter one string: \n");
    
    sResult=string_multiply(string);
    
    print(f"Output is: \n{sResult}");

#===============================
#      Starter
#===============================
if __name__=="__main__":
    main();