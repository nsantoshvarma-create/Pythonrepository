ch=input("Enter The Character to Verify, Whether it is Vowel: \n")
 
match ch:
    case 'A':
        print("A is a Vowel")
    case 'E':
        print("E is a Vowel")
    case 'I':
        print("I is a Vowel")
    case 'O':
        print("O is a Vowel")
    case 'U':
        print("U is a Vowel")
    case _:
        print(ch," is not a Vowel")