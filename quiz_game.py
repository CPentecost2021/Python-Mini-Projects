print("Welcome to My Pop Quiz!")

playing = input("Do you want to Play? ")

if playing.lower() != "yes": 
    quit()
    
print("Okay! Let's play :)")
score = 0

answer = input("What does CPU Stand for? ").lower()
if answer == "central processing unit":
    print("Correct answer!")
    score += 1
else: 
    print("Invalid answer!")

answer = input("What does GPU Stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct answer!")
    score += 1
else: 
    print("Invalid answer!")

answer = input("What does RAM Stand for? ").lower()
if answer == "random access memories":
    print("Correct answer!")
    score += 1
else: 
    print("Invalid answer!")

answer = input("What does PSU Stand for? ").lower()
if answer == "power supply":
    print("Correct answer!")
    score += 1
else: 
    print("Invalid answer!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%!")