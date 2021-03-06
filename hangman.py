# Name: Divyanshu Sharma
# Collaborators: None

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed1):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    #print('Status of ''.join(letters_guessed[1:])',letters_guessed1)
    return letters_guessed1 == secret_word
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: string (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    lst2=[None]*len(secret_word)
    for i in range(len(letters_guessed)):
        for j in range(len(secret_word)):
            if letters_guessed[i]==secret_word[j]:
                lst2[j]=secret_word[j]

    for j in range(len(secret_word)):
        if lst2[j]==None:
            lst2[j]='_ '

    return ''.join(lst2)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    lst1=list(string.ascii_lowercase)
    set1=set(letters_guessed)
    result=[x for x in lst1 if x not in set1]
    return ''.join(result)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[None]
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.') 
    
    # Comment out the next line when testing ends
    print('word: ',secret_word)
    i=0
    warnings=3
    lose=1
    while i<len(secret_word): uncomment
        print('-------------')
        print('You have',warnings,'warnings left.')
        print('You have',len(secret_word)-i,'guesses left.')
        print('Available letters: ',get_available_letters(letters_guessed))
        entry=input('Please guess a letter: ')

        if not str.isalpha(entry):
            print('Please enter an alphabet only!')
            if warnings==0:
                i+=1
            else:
                warnings-=1
            continue
        elif entry in get_guessed_word(secret_word, letters_guessed) and entry in 'aeiou':
            print('You have already entered this Vowel. Penalty of 2 guesses!')
            i+=2
            continue
        elif entry in get_guessed_word(secret_word, letters_guessed):
            print('You have already guessed this alphabet. Please see the Available Letters ')
            if warnings==0:
                i+=1
            else:
                warnings-=1
            continue
        else:
            str.lower(entry)

        
        letters_guessed.append(entry)
        if entry in secret_word:
          print('Good guess: ',get_guessed_word(secret_word, letters_guessed))
          if is_word_guessed(secret_word, get_guessed_word(secret_word, letters_guessed)):
              print('Congratulations,You won')
              print('Your Score for this game is: ',(len(secret_word)-i)*len(set(secret_word)) )
              lose=0
              break
        else:
          print('Oops! That letter is not in my word:',get_guessed_word(secret_word, letters_guessed))
        input('Press Return')
        i+=1

    if lose:
        print('No more Guesses left. Game over!')
        print('The word was:',secret_word)
          
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
