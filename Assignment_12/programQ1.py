##########################################################
##
##  File name   : Assigment12Question1.py
##  Descreption : Accepts one character and checks whether it is vowel or consonant
##  Author      : Kartik Ganesh Jare
##  Date        : 19/1/26
##
##########################################################

# Input: a
# Output: Vowel

def ChkVowel(ch):

    if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' or
       ch == 'a' or ch == 'e' or  ch == 'i' or ch == 'o' or ch == 'u'):
        return True
    else:
        return False

def main():

    bRet = False

    print("Enter String : ")
    Value = input()

    bRet = ChkVowel(Value)

    if(bRet == True):
        print("Vowel")
    else:
        print("consonant")   

if __name__ == "__main__":
    main()        