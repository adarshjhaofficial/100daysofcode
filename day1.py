#Day 1
import random
rand = random.randint(1, 30)
print(rand)
chance = 10
attempt = 0

while(chance, attempt):
    print("Guess a number between 1 to 30 in 10 chances")
    user = int(input("Enter the number: "))
    attempt +=1
    if rand==user:
        print(f"You won in {attempt} attempt")
        ask = input("Do You want to play again:\ny to play again\nn to quit: ")
        if ask=="y":
            continue
        else:
            break
    elif user>rand:
        chance = chance-1
        print(f"Lesser, You have {chance} chances left")
    elif user<rand:
        chance = chance-1
        print(f"greater, You have {chance} chances left")
    if  chance==0:
        print("Game over")
        break
print("Thanks For playing")
