import random

while True:
    Roll = int(input("How many times do you wish to roll the dice? "))
    for i in range(Roll):
        Round_1 = input("Roll a dice (y/n): ").lower()
        if Round_1 == "y":
            choice_1 = random.randint(1, 6)
            print(f"{choice_1}")
        elif Round_1 == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")
    else:
        break
