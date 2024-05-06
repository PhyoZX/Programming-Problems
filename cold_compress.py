# get input from line
n = int(input())
lines = []

for _ in range(n) :
    lines.append(input())

# solve problem
for line in lines : # for each input
    line = line.strip() # remove \n from line

    newStr = ""
    last = line[0]
    count = 1

    for char in line[1:] : # for every character except the first because we already handled it above
        if char == last :  # if the next character is equal to last
            count += 1
        else : # if the next character is different
            newStr += str(count) + " " + last + " "
            count = 1
            last = char
    newStr += str(count) + " " + last 
    print(newStr)
