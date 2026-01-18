import random

easy_words = ["cat", "dog", "apple", "car", "house"]
medaium_words = ["bicycle", "computer", "elephant", "giraffe", "mountain"]
hard_words = ["xylophone", "quizzical", "juxtapose","photosynthesis", "onomatopoeia"]

print("Welcome to the Guessing Game!")
print("Choose a difficulty level:") 
print("1. Easy")
print("2. Medium")  
print("3. Hard")
difficulty = input("Enter 1, 2, or 3: ")
if difficulty == '1':
    word_list = easy_words
elif difficulty == '2':
    word_list = medaium_words
elif difficulty == '3':
    word_list = hard_words
else:
    print("Invalid choice. Defaulting to Easy level.")
    word_list = easy_words
selected_word = random.choice(word_list)
attempts = 6    
guessed_letters = []
print(f"You have {attempts} attempts to guess the word.")
while attempts > 0:
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in selected_word])
    print("Word to guess:", display_word)
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in selected_word:
        print("Good guess!")
        if all(letter in guessed_letters for letter in selected_word):
            print(f"Congratulations! You've guessed the word: {selected_word}")
            break
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")
        if attempts == 0:
            print(f"Game over! The word was: {selected_word}")
            