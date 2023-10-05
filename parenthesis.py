test_string = "((())())()"
bad_test = ")()("
ok = "(((()))"

stack = []

def parentheses(test_string):
    for i, p in enumerate(test_string):
        if p == "(":
            stack.append(i)
        elif p == ")":
            if stack:
                stack.pop()
            else:
                return i
        

    if stack:
        return stack[0]
    
    return "valid string"

print(parentheses(bad_test))