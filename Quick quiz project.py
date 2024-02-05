welcome = 'Welcome to my game!'
print (welcome)
player = input ('Would you like to begin? ')

adios = 'goodbye'
if player.lower() != "yes":
    print(adios) + quit()

print("let's do it!")
score = 0

answer = input("what is the Capital of France? ")
if answer.lower() == "paris":
        print('Correct! Great job!')
        score += 1
else:
        print("Sorry, that's wrong!'")

answer = input("what is the 12 x 10? ")
if answer.lower() == "120":
        print('Correct! Great job!')
        score += 2
else:
        print("Sorry, that's wrong!'")

answer = input("Where is the city of Lagos located? ")
if answer.lower() == "nigeria":
        print('Correct! Great job!')
        score += 2
else:
    print("Sorry, that's wrong!'")

answer = input("Who is the greatest and most merciful? ")
if answer.lower() == "allah":
    print('Correct! Great job!')
    score += 3
else:
    print("Sorry, that's wrong!'")

answer = input("Who is the orange cat that eats lasanga? ")
if answer.lower() == "garfield":
    print('Correct! Great job!')
    score += 2
else:
    print("Sorry, that's wrong!'")

answer = input("Who was the first president of The U.S.A? ")
if answer.lower() == "george washington":
    print('Correct! Great job!')
    score += 1
else:
    print("Sorry, that's wrong!'")
print("Your score was " + str(score))
print("your had a " + str((score / 11) * 100) + "%!.")