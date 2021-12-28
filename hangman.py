import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
stage = 7
word_list = ["ardvark", "baboon", "camel", "catepillar"]
word = list(random.choice(word_list))
word_length = len(word)
guessed_word = []

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxx  |-|   |-|    /---\\    |--\\  |-|    /-/----\\   |--\\      /--|    /---\\    |--\\  |-|  xxxx")
print("xxxx  | |   | |   / / \\ \\   | | \\ | |   / /------/  |   \\    /   |   / / \\ \\   | | \\ | |  xxxx")
print("xxxx  | ===== |  | |===| |  | |\\ \\| |  | |    ___   | |\\ \\  / /| |  | |===| |  | |\\ \\| |  xxxx")
print("xxxx  | |   | |  | |   | |  | | \\ | |   \\ \\___ / /  | | \\ \\/ / | |  | |   | |  | | \\ | |  xxxx")
print("xxxx  |_|   |_|  |_|   |_|  |_|  \\__|    \\_\\____/   |_|  \\  /  |_|  |_|   |_|  |_|  \\__|  xxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

for _ in range(word_length):
    guessed_word.append("_")

while not end_of_game:
    print(f"\n{' '.join(guessed_word)}\n")
    guessed_letter = input("Guess a letter: ")

    if word.count(guessed_letter) > 0:
        for position in range(0, word_length):
            if word[position] == guessed_letter:
                guessed_word[position] = guessed_letter
    else:
        stage -= 1
        print(stages[stage])

    if stage == 0:
        end_of_game = True
        print ("He died :(")
    elif guessed_word.count("_") == 0:
        print(f"\n{' '.join(guessed_word)}\n")
        end_of_game = True
        print("You won!")

