def bracket_validator():

    str = input("Enter a string of brackets: ")

    stack = []
    brackets = {'{': '}', '[': ']', '(': ')'}

    for i in str:
        if i in brackets.keys():
            stack.append(i)
        elif i in brackets.values():
            if brackets[stack.pop()] != i:
                return False
            
    return len(stack) == 0

print(bracket_validator())    
