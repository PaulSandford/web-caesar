#class caesar:
    #def __init__():
        
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    answer = ""

    for a in text:
        if a.isalpha():
            answer += rotate_character(a, rot)
        else:
            answer += a
        
    return answer

def main():
    string = input("Give me something to scramble!")
    num = int(input("How much scrambling will take place?"))
    
    print(encrypt(string, num))
if __name__ == "__main__":
    main()
