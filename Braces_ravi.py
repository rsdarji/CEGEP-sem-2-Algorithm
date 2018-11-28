def match(symbolStr):
    stack = []
    counter = 0
    print(len(stack))
    for char in symbolStr:
        stack.append(char)
        print(stack)

    while len(stack) !=0:
        item = stack.pop()
        if counter<0:
            break
        if item =="(":
            counter+=1
            print(stack)
        elif item ==")":
            counter-=1
            print(stack)
    print("counter : ",counter)

    return counter!=0
print(match("((((((()))))))"))