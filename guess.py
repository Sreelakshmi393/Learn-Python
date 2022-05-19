import random
real = random.randint(0,100)
#print('Guess the number')
while True:
    num = int(input('Guess the number between 0 an 100 '))
    if(num > real):
        print("You guessed a higher number.")
    elif(num<real):
        print("You guessed a smaller number.")
    else:
        print("Yay!!You won.")
        break