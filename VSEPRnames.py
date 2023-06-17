from random import randint

print("Instructions:\nIn this game, you will be given the number of electron clouds and lone pairs present.")
print("You must determine the VSEPR name of the molecule's shape. Be careful with spelling!!")
print("Each correct answer gives you +1 points, each incorrect gives -1 points. If your score becomes negative, the game stops.")
print("If you skip a question or answer incorrectly, it will be saved to a study list you will access later.")
game_difficulty = int(input("Enter a difficulty - 1 (Easy - O Lone Pairs), 2 (Medium - 0/1 Lone Pairs), or 3 (Hard - 0/1/2/3 Lone Pairs) - to start: ")) # starts game

while game_difficulty not in [1,2,3]: # invalid difficulty
    game_difficulty = int(input("Invalid input. Enter a difficulty to start: "))

study_list = [] # the list of skipped/incorrect questions
play_again = True
if game_difficulty == 1: # player's starting score
    score = 4
elif game_difficulty == 2:
    score = 2
else:
    score = 0
print("\nBased off the difficulty you selected, you have " + str(score) + " point(s) to start.") # start score

while play_again == True: # loop runs while player "plays again"
    electron_clouds = randint(2,6) # generate number of electron clouds
    if electron_clouds == 2: # generate possible values of lone pairs based on number of electron clouds
        lone_pairs = 0
    elif electron_clouds == 3:
        if game_difficulty == 1:
            lone_pairs = 0
        else:
            lone_pairs = randint(0,1)
    elif electron_clouds == 4:
        if game_difficulty == 1:
            lone_pairs = 0
        elif game_difficulty == 2:
            lone_pairs = randint(0,1)
        else:
            lone_pairs = randint(0,2)
    elif electron_clouds == 5:
        if game_difficulty == 1:
            lone_pairs = 0
        elif game_difficulty == 2:
            lone_pairs = randint(0,1)
        else:
            lone_pairs = randint(0,3)
    elif electron_clouds == 6:
        if game_difficulty == 1:
            lone_pairs = 0
        elif game_difficulty == 2:
            lone_pairs = randint(0,1)
        else:
            lone_pairs = randint(0,2)
    values = (electron_clouds,lone_pairs) # save number of electron clouds and lone pairs in a tuple
    if values == (2,0): # generate correct answers based on values previously generated
        answer = ["linear"]
    elif values == (5,3):
        answer = ["linear"]
    elif values == (3,0):
        answer = ["trigonal planar"]
    elif values == (3,1):
        answer = ["bent"]
    elif values == (4,2):
        answer = ["bent"]
    elif values == (4,0):
        answer = ["tetrahedral"]
    elif values == (4,1):
        answer = ["trigonal pyramidal"]
    elif values == (5,0):
        answer = ["trigonal bipyramidal", "trigonal bi-pyramidal"]
    elif values == (5,1):
        answer = ["see-saw", "seesaw", "see saw", "asymmetrical tetrahedron"]
    elif values == (5,2):
        answer = ["t-shaped", "t shaped"]
    elif values == (6,0):
        answer = ["octahedral"]
    elif values == (6,1):
        answer = ["square pyramidal"]
    elif values == (6,2):
        answer = ["square planar"]
    if score == 0:
        print("\nYou have no points! If you answer incorrectly, the game will end!")
        print("This VSEPR shape has " + str(electron_clouds) + " electron clouds, and " + str(lone_pairs) + " lone pair(s).")
    else:
        print("\nThis VSEPR shape has " + str(electron_clouds) + " electron clouds, and " + str(lone_pairs) + " lone pair(s).")
    guess = str(input("What do you think this is called (enter s to skip): ")) # input from user
    if guess.lower() in answer: # correct
        print("Thats correct! The correct answers are: " + str(answer) + ".")
        score += 1
        if values in study_list: # removes correct answer from study list
            study_list.remove(values)
    elif guess.lower() == str("s"): # skips question
        if values not in study_list:
            study_list.append(values)
            print("Question saved to study list.")
        else:
            print("Question is already in study list.")
    else: # incorrect
        print("Sorry, thats not correct. The correct answers were: " + str(answer) + ".")
        score -= 1
        if values not in study_list:
            study_list.append(values)
    if score >= 0:
        print("Your score is currently " + str(score) + ".")
        play_again = str(input("Would you like try another question? (y/n): ")) # reassign play again value
        if play_again.lower() == str("y"):
            play_again = True
        elif play_again.lower() == str("n"):
            play_again = False
        else:
            play_again = str(input("Invalid input. Please enter y or n, or game will end: "))
            if play_again.lower() == str("y"):
                play_again = True
            else:
                play_again = False
    else:
        break
    
if score >= 0:
    print("\nThank you for playing! Your ending score is: " + str(score) + ".")
else:
    print("You have lost all points. Game over.")

if len(study_list) != 0: # prints questions player answered wrong/skipped
    print("\nThe shapes you had issues with are: " + str(study_list) + ".")
    print("The first number represents the # of electron clouds, the second number represents the # of lone pairs.")
