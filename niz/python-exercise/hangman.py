# Randomword
word = 'halo' # randomize csv......
# Try
count = 6 
# single char from user 
user_input = input() 
# int x, 'asdfasdf' x, check for used char, print answer

# return Answer, word compare
answer = ''

# while
if user_input in word:
    print('GOOD GUESS!')
    answer+=user_input
else:
    print('DIE!!!')
    count -=1

if sorted(answer) == sorted(word):
    print('good')
