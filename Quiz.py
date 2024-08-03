print("Welcome to the Blessed Quiz")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay Lets start the Game!")


name = input("whats your name ? ")
print("Welcome " + name)

print("Lets GO!!!")
score = 0

Answer = input("What is the capital of India? ")
if Answer.lower() == "delhi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer1 = input("What is the capital of France? ")
if Answer1.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer2 = input("What is the capital of Japan? ")
if Answer2.lower() == "tokyo":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer3 = input("What is the capital of Australia? ")
if Answer3.lower() == "canberra":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer4 = input("What is the capital of Canada? ")
if Answer4.lower() == "ottawa":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer5 = input("What is the capital of Germany? ")
if Answer5.lower() == "berlin":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer6 = input("What is the capital of Italy? ")
if Answer6.lower() == "rome":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer7 = input("What is the capital of Russia? ")
if Answer7.lower() == "moscow":
    print("Correct")
    score += 1
else:
    print("Incorrect")

Answer8 = input("What is the capital of Brazil? ")
if Answer8.lower() == "brasília":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your total Score is : " + str(score))