# A program to check that delimiters are balanced in an expression

from SimpleStack import Stack

stack = Stack(100)

expr = input('Expression to check: ')
errors = 0      # Assume no errors in expression

for pos, letter in enumerate(expr):     # Loop over letters in expression
    if letter in '{[(':                 # Look for starting delimiters
        if stack.isFull():
            raise Exception('Stack overflow on expression')
        else:
            stack.push(letter)
    elif letter in ')]}':               # Look for closing delimiters
        if stack.isEmpty():
            print('Error: ', letter, ' at position ', pos, ' has no matching left delimiter')
            errors += 1
        else:
            left = stack.pop()  # Get left delimiter from stack
            if not (left == '{' and letter == '}' or
                    left == '[' and letter == ']' or
                    left == '(' and letter == ')'):
                print('Error:',  letter, ' at position ', pos, ' does not match left delimiter ', left)
                errors += 1

# After going through entire expression, check if stack empty
if stack.isEmpty() and errors == 0:
    print("Delimiters balance in expression", expr)
elif not stack.isEmpty():
    print('Expression missing right delimiters for ', stack)
