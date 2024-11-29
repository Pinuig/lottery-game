import random

lottery = random.randint(0, 99)

lottery1 = lottery // 10
lottery2 = lottery % 10

guess = eval(input("Input your lucky value: "))

guess1 = guess // 10
guess2 = guess % 10

print(lottery)

if guess == lottery:
    print("you won $10000")
    
elif guess1 == lottery1 or guess2 == lottery2 and guess2 == lottery1 or guess1 == lottery2:
    print("you won $3000")
    
elif guess1 == lottery2 or guess2 == lottery1 or lottery == guess1 or guess == lottery1:
    print('print you won $1000')
    
else:
    print("you loose try again next time")