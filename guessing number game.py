import random


score = 10
randomnumber = random.randint(1,3)
print('This a game of guessing\n')
print('You have to choose a random number\n')
print('If you guess correct,you win')

while True:
    UserNumberInput = int(input('Guess:'))

    if UserNumberInput == randomnumber:
        print ('you won')
        break
    else:
        print('better luck next time')
        score -=1
        print('your score is' + str(score))
