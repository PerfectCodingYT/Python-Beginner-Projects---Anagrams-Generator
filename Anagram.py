import random
file_obj = open("words.txt")
file_data = file_obj.read()
lines = file_data.splitlines()
test = True
while test == True:
    pick = lines[random.randrange(0, 976)]
    letter = list(pick)
    random.shuffle(letter)
    print("".join(letter))
    print("Enter endLoop to stop.")
    userInp = input("Your guess: ")
    if userInp == pick:
        print("You got it right!")
    elif userInp == "endLoop":
        break
    else:
        print("You got it wrong! The correct answer was ", pick, ".")