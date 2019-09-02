import random

comp_num= random.randint(1,50)
#print(comp_num)
to_add= comp_num + random.randint(1,5)
#print(to_add)
to_sub= comp_num - random.randint(1,5)
#print(to_sub)

print("Press 1 to Play Game. \nPress 2 to Exit.")
choice= int(input("Choose option to select: "))

if choice is 1:
    player_num = int(input("Enter number between 1 and 50: "))
    #print(player_num)

    while True:
        if comp_num == player_num:
            print("Congratulations! You gussed the correct number.")

        elif player_num < comp_num:
            print("Your number is less than computer number. Guess again!")
            if comp_num > 1 and comp_num < 50:
                print("HINT: The number is between {} and {}".format(to_sub, to_add))
                player_num = int(input("Guess another number: "))

            elif comp_num == 1 or comp_num < 1:
                print("HINT: The number is between {} and {}".format(1, to_add))
                player_num = int(input("Guess another number: "))

            elif comp_num is 50:
                print("HINT: The number is between {} and {}".format(to_sub, 50))
                player_num = int(input("Guess another number: "))

        elif player_num > comp_num:
            print("Your number is greater than computer number. Guess again!")
            if comp_num > 1 and comp_num < 50:
                print("HINT: The number is between {} and {}".format(to_sub, to_add))
                player_num = int(input("Guess another number: "))

            elif comp_num == 1 or comp_num < 1:
                print("HINT: The number is between {} and {}".format(1, to_add))
                player_num = int(input("Guess another number: "))

            elif comp_num is 50:
                print("HINT: The number is between {} and {}".format(to_sub, 50))
                player_num = int(input("Guess another number: "))

elif choice is 2:
    exit()
