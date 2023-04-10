import random

def main():
    while True:
        try:
            player_dice = int(input("Select dice type: "))
            if player_dice < 1:
                print("It's only accepts whole number larger than 0.")
                continue  
        except ValueError:
            print("It's only accepts whole number.")
            continue  
                  
        try:
            dice_number = int(input("Number of dice rolls: "))
            if player_dice < 1:
                print("It's only accepts whole number larger than 0.")
                continue  
        except ValueError:
            print("It's only accepts whole number.")
            continue 

        print(f"{dice_number}D{player_dice}",
        random.randint(1, player_dice)*dice_number)

        if str.lower(input("Wanna quit?")) == "yes":
            break
        else:
            continue

if __name__ == "__main__":
    main()


