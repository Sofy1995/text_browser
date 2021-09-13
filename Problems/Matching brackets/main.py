smth = input()
stack = []
answer = ''
for let in smth:
    if let == "(":
        stack.append(let)
    elif let == ")":
        if len(stack) > 0:
            stack.pop()
        elif len(stack) == 0:
            answer = "ERROR"
            break

if answer == '' and len(stack) == 0:
    print("OK")
elif answer or len(stack) > 0:
    print("ERROR")
