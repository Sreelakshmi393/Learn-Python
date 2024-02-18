import random

def choose():
    words = ['diamond','bicycle','journey','weather','library','sunset','elephant','cupcake','pumpkin','weather','rainbow','octopus','beaker','chicken','airplane','vehicle','popcorn','mystery','dolphin','hotdog']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word, len(word)))
    return jumbled

def thank(p1name,p2name,p1s,p2s):
    print(p1name,",your score is ",p1s)
    print(p2name,",your score is ",p2s)
    print("THANK YOU ",p1name, " & ", p2name, ". YOU GUYZ DID A GREAT JOB:)")

def play():
    p1name = input("Enter player 1 name : ")
    p2name = input("Enter player 2 name : ")
    p1score = 0
    p2score = 0
    turn = 0
    while(1):
        word = choose()
        qn  = jumble(word)
        print(qn)
        if turn%2==0:
            print(p1name,"'s turn ")
            ans = input("What's in my mind ? ")
            if ans==word:
                print("HURRAYYY!!!! YOU GUESSED IT RIGHT")
                p1score+=1
                print("Your new score is ",p1score)
            else:
                print("BETTER LUCK NEXT TIME! THE WORD WAS ", word)
            c = int(input("Press 1 to continue / 0 to quit"))
            if c==0:
                thank(p1name,p2name,p1score,p2score)
                break
        else:
            print(p2name,"'s turn ")
            ans = input("What's in my mind ? ")
            if ans==word:
                print("HURRAYYY!!!! YOU GUESSED IT RIGHT")
                p2score+=1
                print("Your new score is ",p2score)
            else:
                print("BETTER LUCK NEXT TIME! THE WORD WAS ", word)
            c = int(input("Press 1 to continue / 0 to quit"))
            if c==0:
                thank(p1name,p2name,p1score,p2score)
                break
        turn+=1
play()


    

