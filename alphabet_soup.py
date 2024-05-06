def alphabetSoup(str) :
    li = sorted(list(str))
    liLower = sorted(list(str.lower()))
    caps = []
    newStr = ""

    for char in li :
        if char.isupper() :
            caps.append(char)

    for letter in liLower :
        if caps.count(letter.upper()) != 0 :
            newStr += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else :
            newStr += letter

    return newStr
    

str = input("Enter a string: ")
print(alphabetSoup(str))