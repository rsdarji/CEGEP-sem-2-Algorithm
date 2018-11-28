def match(str):
    count = 0
    for i in str:
        if(count < 0):
            break
        if(i=="("):
            count+=1
        elif(i==")"):
            count-=1

    return count==0
print(match("(()"))

#https://stackoverflow.com/questions/538346/iterating-each-character-in-a-string-using-python