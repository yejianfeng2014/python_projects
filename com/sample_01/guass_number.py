
# This is a guess the number game.
import  random

scretNumber = random.randint(1,20)

print(" i  think a number is 1 to 20")

# 让猜6次

for guessess in range(1,7):

    print('take a guess')
    msg = 'input number please: '
    s = input(msg)

    i = int(s)

    if i > scretNumber :
        print('your guess is too big')

    elif i < scretNumber:
        print('you guess is two low')

    else:
        break

if i == scretNumber :
    print('Good job! You guessed my number in ' + str(guessess) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(guessess))


