 import random
 from word import word_list
 
 def get_word():
   word=random.choice(word_list)
   return word.upper()

def play(word):
  word_completion="_"*len(word)
  guessed=False
  guessed_letters = []
  guessed_words = [] 
  tries=6
  print(" HANGMAN ")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries>0:
    guess = input(" Guess a letter ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print(" Already guessed this letter", guess)
      elif guess not in word:
        print(guess,"is not in the word.")
        tries -=1 
        guessed_letters.append(guess)
      else:
        print("good job ",guess, " is in the word")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i,letter in enumerate(word) if letter==guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed=True     
    elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_letters:
            print(" Already guessed this letter", guess)
         elif guess != word:
            print(guess,"is not in the word.")
            tries -=1
            guessed_words.append(guess)
         else:
          guessed = True
          word_completion = word
    else:
        print(" Invalid Input ")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

  if guessed:
        print("noice wp")
  else:
        print("No more tries mwopmwop the answer was " + word)
 
def display_hangman(tries):
  stages = [ """
  
  0
  
  """,
  """
  
  0 1 
  
  """,
  """
  
  0 1 2 
  
  """,
  """
  
  0 1 2 3
  
  """,
  """
  
  0 1 2 3 4
  
  """,
  """
  
  0 1 2 3 4 5
  
  """,
  """
  
  0 1 2 3 4 5 6
  
  """
  ]
  return stages[tries]

def main():
  word=get_word()
  play(word)
  while input("play agn y/n").upper()=="Y":
    word= get_word()
    play(word)

 if __name__ == "__main__":
  main()  
