from SimpleStack import Stack

stack = Stack(10)

for word in ['May', 'the', 'force', 'be', 'with', 'you']:
    stack.push(word)

print('Afert pushing ', len(stack), 'Words on the stack, it contains: \n', stack)

print ('Is stack full? ', stack.isFull())

print('Popping items of the stack: ')
while not stack.isEmpty():
    print(stack.pop(), end=' ')

print()
