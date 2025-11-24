import random

print("===== GUESS THE NUMBER GAME =====")
print("Choose Difficulty Level:")
print("1. Easy   (1–10, unlimited attempts)")
print("2. Medium (1–50, 7 attempts)")
print("3. Hard   (1–100, 5 attempts)")

choice = int(input("Enter level (1/2/3): "))

if choice == 1:
    max_num = 10
    attempts = None
elif choice == 2:
    max_num = 50
    attempts = 7
elif choice == 3:
    max_num = 100
    attempts = 5
else:
    print("Invalid choice! Defaulting to Easy.")
    max_num = 10
    attempts = None

secret = random.randint(1, max_num)
count = 0

print(f"\nI'm thinking of a number between 1 and {max_num}.")

while True:
    guess = int(input("Your guess: "))
    count += 1

    if guess == secret:
        print(f"🎉 Correct! You guessed it in {count} attempts!")
        break

    if attempts is not None and count == attempts:
        print("\n❌ Out of attempts!")
        print(f"The correct number was {secret}.")
        break
