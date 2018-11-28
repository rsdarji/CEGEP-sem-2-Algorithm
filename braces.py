def match(symbolStr):
    stack = []
    balanced = True
    index = 0
    while index < len(symbolStr) and balanced:
        symbol = symbolStr[index]
        if symbol == "(":
            stack.append(symbol)
        else:
            if stack=="":
                balanced = False
            elif len(stack)!=0:
                stack.pop()

        index = index + 1

    if balanced and len(stack)==0:
        return True
    else:
        return False


print(match("(()))"))