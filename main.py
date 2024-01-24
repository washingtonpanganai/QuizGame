print("Welcome to my game!")

introduction = input("Do you want to play? ")

if introduction == "yes":
    print("pick a number between 1 and 5")
elif introduction == "no":
    quit()

for _ in range(3):  # Allow the user to try three times
    number = input()

    if number in ["1", "2", "3", "4", "5"]:
        if number == "1":
            print("You selected Naruto")
        elif number == "2":
            print("You selected Dragon Ball Z")
        elif number == "3":
            print("You selected One Piece")
        elif number == "4":
            print("You selected Jujutsu Kaisen")
        elif number == "5":
            print("You selected Hunter X Hunter")

        break  # exit the loop if a valid number is selected
    else:
        print("Your number is out of bounds. Please pick another number.")

if number == "1":
    print("Im thinking of a character you have 1 hint")
elif number == "2":
    print("Im thinking of a character you have 1 hint")
elif number == "3":
    print("Im thinking of a character you have 1 hint")
elif number == "4":
    print("Im thinking of a character you have 1 hint")
elif number == "5":
    print("Im thinking of a character you have 1 hint")

for _ in range(3):  # Allow the user to try three times
    hint = input()
    # hint2 = input()

    if hint in ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"]:
        if hint == "hint 1":
            print("hes from the hidden leaf")

        answer = input()

        if answer == "naruto":
            print("You win")
            break

        elif hint == "hint 2":
            print("hes a saiyan")

            answer = input()

            if answer == "goku":
                print("You win")
                break

        elif hint == "hint 3":
            print("hes a pirate")

            answer = input()

            if answer == "luffy":
                print("You win")
                break

        elif hint == "hint 4":
            print("hes a jujutsu sorceror")

            answer = input()

            if answer == "yuji":
                print("You win")
                break

        elif hint == "hint 5":
            print("hes a hunter")

            answer = input()

            if answer == "gon":
                print("You win")
                break


#     elif hint == "hint 2":
#             print("hes a saiyan")
#
#             answer = input()
#
#             if answer == "goku":
#                 print("You win")
#
#             break
#
#         # elif hint == "hint 2":
#         #     print("hes the hokage")
#         #
#         #     answer = input()
#         #
#         #     if answer == "naruto":
#         #         print("You win")
#         #
#         #         break
#         #
#         # elif hint == "hint 3":
#         #     print("he has the 9 tails")
#         #
#         # # break  # exit the loop if a valid number is selected
#         #
#         # answer = input()
#         #
#         # if answer == "naruto":
#         #     print("You win")
#         # else:
#         #     print("You lose")
#         # break
#
#     elif number == "2":
#         print("Im thinking of a character you have 1 of 3 hints")
#
#
#     # break
#
#     # if number == "2":
#     #     print("Im thinking of a character you have 1 of 3 hints")
#
# for _ in range(3):  # Allow the user to try three times
#     hint2 = input()
#
#     if hint2 in ["hint 1", "hint 2", "hint 3"]:
#             if hint2 == "hint 1":
#                 print("hes a saiyan")
#
#                 answer2 = input()
#
#                 if answer2 == "goku":
#                     print("You win")
#
#                     break
#
#             elif hint2 == "hint 2":
#                 print("hes the hokage")
#
#                 answer2 = input()
#
#                 if answer2 == "naruto":
#                     print("You win")
#
#                     break
#
#             elif hint2 == "hint 3":
#                 print("he has the 9 tails")
#
#             # break  # exit the loop if a valid number is selected
#
#             answer2 = input()
#
#             if answer2 == "naruto":
#                 print("You win")
#
#     break