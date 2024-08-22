# A program to reverse the letters of a word

from SimpleStack import Stack


stack = Stack(100)

word = input("word to reverse: ")

for letter in word:
    if not stack.isFull():
        stack.push(letter)

reverse = ''

while not stack.isEmpty():
    reverse += stack.pop()

print('The reverse of', word, 'is ', reverse)
