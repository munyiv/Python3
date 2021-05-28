print("Hello and welcome to my world")
name=input("Lets have a chat.Tell me what is your name?")
age=input("How old are you?")

tries=10

if age >="10":
    print("Hello",name, "You are old enough to play this game")

play=input("Do you want to play?")
if play=="yes":
    print(name, "You have ",tries,"to start the game")
    print("Let the games begin")

left_or_right=input("Here is your first choice..left or right (left/right)")
if left_or_right== "left":
    ans=input("Great you can either take the river route...Do you want to go round or swim")

left_or_right=input("You choose the wrong route")
if left_or_right == "right":
    ans=input("Thank you for playing you've reached the end")