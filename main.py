print("Welcome to my game!")
name = input("What is your name? ")
age = int(input("That is your age? "))

health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Yuo are starting with", health, "health")
        print("Les's play then!")
        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nic, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went a round and reached the other said of the lake")

            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5


            ans = input("You notice a house and a river, Which do you go to? (river/house)? ")

            if ans == "house":
                print("You go to the house and greted by the owner... He doesn't like you and you lose 5 health ")
                health -= 5

                if health <= 0:
                 print("You now have 0 health and you lose the game...")
                else:
                    print("You have survived... You win")
            else:
                print("You fell in the river and lost...")
        else:
            print("You fell dowm and lost...")

    elif wants_to_play == "no":
         print("Ok, maybe next time when you be ready.")
         print("Thank you for your time.")

    elif age >= 14:
        print("Ok, you are able to play.")
else:
        print("You are young, you can't play, sorry.")
        print("Thank you for your time.")
