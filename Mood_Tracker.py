mood=input("How are you feeling today")
with open("mood.txt","w") as file:
    file.write(mood)

with open("mood.txt","r") as file:
    saved_mood = file.read()
print("Your feeling mood is", saved_mood)