import random

print("Number guessing game!!")

def random_check():
    iterations =0

    while (True):
        random_number = random.randint(1,10)
        guess_number = int(input("Enter your guessing number: "))
        if(guess_number==random_number):
            print("Your guess is correct atfer",iterations,"iterations")
            print()
            yes_no = input("Do you want to play this again? ").lower()
            if(yes_no=="yes"):
                random_check()
            else:
                exit()

        else:
            print("Your guess is wrong")
            iterations = iterations+1
            if(iterations>=5):
                print("Your chance is over!!")
                yes_no = input("Do you want to play this again? ").lower()
                if(yes_no=="yes"):
                    random_check()
                else:
                    exit()
            else:
                continue
yes_no = input("Do you want to play this? ").lower()


if(yes_no=="yes"):
    random_check()
else:
    exit()

