#hint, need to use at least 2 collection data types in my solution
number_range = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}

print(number_range) #check to see randomizer is working

numbers_list = list(number_range)

# This is to pick the first number from the set list.
target_number = int(numbers_list[0])

# Initialize the guessing loop
print("Welcome to the guessing game!")
print("I have selected a number between 1 and 20. Try to guess it!")

guess_count = 0
guessed_numbers = []

while True:
    # Get user input
    guess = int(input("Enter your guess: "))

    guessed_numbers.append(guess) #to save the numbers entered
    guess_count += 1 #to count the increment of the guess count

    # Check the guess input
    if guess < target_number:
        print("Higher! Try again.")
    elif guess > target_number:
        print("Lower! Try again.")
    else:
        print("Congratulations! You've guessed the number:", target_number)
        break

print(f"You took {guess_count} guesses.")
print("Your guesses were:", guessed_numbers)

if guess_count < 5:
    print("You're awesome!")
#Bonus: Keep track of number of guesses, collect all guessed numbers and print at end
#Bonus2: more than 5 guesses, print "You're awesome" / make program safe for non-numeric input
