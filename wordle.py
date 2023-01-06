#This is a program that simulates the game Wordle where users have to guess the five
#letter word which is the word of the day (the program provides 2 play modes: 1 player mode
#and 2 player mode).

#Author: YunShan Nong

#import
import random
import wordle_utils

#Global variables
WORLDE_WORD_LENGTH = 5
MAX_NUM_OF_GUESSES = 6
CHAR_GREEN = '\x1b[6;30;42m'
CHAR_YELLOW = '\x1b[6;30;43m'
CHAR_GRAY = '\x1b[6;30;47m'
CHAR_END = '\x1b[0m'

#helper functions
def is_valid_word(word, list_words):
    """ (str, list) -> Bool
    takes two inputs – a word as string and list of string as a list of words.
    Returns True if the word is a five letter word and belongs to the given list
    of words, otherwise the function returns False.
    
    >>> is_valid_word('about', ['abounds', 'about', 'abouts', 'above', 'aboveboard'])
    True
    
    >>> is_valid_word('hello', ['bonjour', 'allo', 'salut'])
    False
    
    >>> is_valid_word('coco', ['coco', 'chocho', 'cocwo'])
    False
    
    """
    if len(word) == WORLDE_WORD_LENGTH:
        return word in list_words
    
    else:
        return False
    
def print_string_list(list_words):
    """ (list) -> str
    takes a list of strings and prints each string in the list on a new line
    
    >>> print_string_list(['abounds', 'about', 'abouts', 'aboveboard', 'abovedeck'])
    abounds
    about
    abouts
    aboveboard
    abovedeck
    
    >>> print_string_list(['Hello', 'How are you?'])
    Hello
    How are you?
    
    >>> print_string_list(['1', '2', '3', '4'])
    1
    2
    3
    4
    
    """
    for elements in list_words:
        print(elements)
        
def color_string(word, color):
    """(str, str) -> str

    Takes two strings: a word to be colored, and a color. The function returns
    the “colored” string (a new string where the word to be colored is concatenated
    in between the corresponding ANSI code of the color and CHAR_END.) If the color string
    is incorrect, the function prints 'Invalid color.' and returns the original word string.

    >>> color_string('about', 'green')
    '\x1b[6;30;42mabout\x1b[0m'
    
    >>> color_string('green', 'rose')
    Invalid color.
    'green'
    
    >>> color_string('green', 'gray')
    '\x1b[6;30;47mgreen\x1b[0m'
    
    """
    green_word = CHAR_GREEN + word + CHAR_END
    gray_word = CHAR_GRAY + word + CHAR_END
    yellow_word = CHAR_YELLOW + word + CHAR_END
    
    if color == 'green':
        return green_word
    elif color == 'gray':
        return gray_word
    elif color == 'yellow':
        return yellow_word
    else:
        print('Invalid color.')
        return word
    
def get_all_5_letter_words(list_words):
    """(list) -> list

    Takes a list of strings representing a list of words and returns a new list
    consists of only WORDLE_WORD_LENGTH(5) length words.

    >>> get_all_5_letter_words(['abs', 'about', 'abouts', 'above', 'aboveboard', 'aloft'])
    ['about', 'above', 'aloft']
    
    >>> get_all_5_letter_words(['abs', 'abb', 'bab', 'did'])
    []
    
    >>> get_all_5_letter_words(['hello', 'salut', 'dance'])
    ['hello', 'salut', 'dance']

    """
    new_list = []
    for word in list_words:
        if len(word) == WORLDE_WORD_LENGTH:
            new_list += [word]
            
    return new_list

#functions for the game
def main():
    """() -> NoneType

    The function first loads the list of all words. Then, from that list it filters and 
    keeps only 5 letter words. Then finally it calls the function play passing as 
    parameter the list of 5 letter words. As a result, the main function prints what
    play prints when calling it.
    
    """
    full_list = wordle_utils.load_words()

    list_words = get_all_5_letter_words(full_list)
    
    play(list_words)
    
def play(list_words):
    """(list) -> NoneType

    Takes a list of strings as input which represents the list of all words. The function lets
    users to choose the play mode and get the wordle. The functions lets the users to play
    the game and prints a final message telling whether they have won or not.
    
    """
    wordle = choose_mode_and_wordle(list_words)
    
    num_guess = play_with_word(wordle, list_words)
    
    print_final_message(num_guess, wordle)
    
    
def choose_mode_and_wordle(list_words):
    """(list) -> str
    takes  a  list  of  strings  as  input  which  represents  the  list  of  all  words  and 
    returns  the  wordle  –  the  word  which  is  going  to  be  solution  of  the  game.
    
    >>> random.seed(20)
    >>> choose_mode_and_wordle(['about', 'above', 'aloft', 'aeons'])
    Enter the number of players: 1
    'above'
        
    >>> choose_mode_and_wordle(['today', 'hello', 'salut'])
    Enter the number of players: 2
    ***** Player 1's turn. *****
    ***** Player 2's turn. *****
    'today'
        
    >>> choose_mode_and_wordle(['hello'])
    ***** Player 1's turn. *****
    ***** Player 2's turn. *****
    'hello'
    """
    
    mode = int(input("Enter the number of players: "))
        
    if mode == 1:
        wordle = generate_random_wordle(list_words)
        return wordle
        
    elif mode == 2:
        print("\n***** Player 1's turn. ***** \n")
        wordle = input_wordle(list_words)
        print("\n***** Player 2's turn. ***** \n")
        return wordle
        
    else:
        print("Wordle can be played with 1 or 2 players. Please only enter 1 or 2.")
        choose_mode_and_wordle(list_words)

def input_wordle(list_words):
    """(list) -> str
   
    takes a list of strings as input which represents the list of
    all words and returns the wordle if the wordle entered by the user
    is a valid word. Otherwise, the function asks for another input.
    
    """
    
    wordle_input = wordle_utils.input_and_hide("Input today's word: ")
    
    wordle = wordle_input.lower()
    
    while (not is_valid_word(wordle, list_words)): #if the word is not valid
        print('Not a valid word, please enter a new one.')
        wordle_input = wordle_utils.input_and_hide("Input today's word: ")
        wordle = wordle_input.lower()
      
    return wordle
        
   
def generate_random_wordle(list_words):
    """(list) -str
    takes a list of strings as input which represents the list of all words. The
    function picks a random string from the list and returns it.

    >>> random.seed(100)
    >>> generate_random_wordle(['about', 'above', 'aloft', 'aeons'])
    'above'
    
    >>> random.seed(1000)
    >>>generate_random_wordle(['fruit', 'apple', 'aloft'])
    'aloft'
    
    >>>generate_random_wordle(['balad'])
    'balad'
    """
    
    i = random.randint(0, len(list_words)-1) 
    wordle = list_words[i]
    
    return wordle

def play_with_word(wordle, list_words):
    """(str, list) -> int
    takes the solution word as string and a list of words as a list of strings. The
    function asks the player to input a guess word. If it’s not the right word, the function
    continues to ask the user for input. it interrupts early if the player guesses the solution.
    The function returns the number of words the player entered the right word
    
    >>> play_with_word('caper', ['cable', 'cater', 'crane', 'carve', 'caper', 'calls'])
    Enter a guess: Crane
    c ra n e
    Enter a guess: cArvE
    c ra n e
    ca r v e
    Enter a guess: caper
    c ra n e
    ca r v e
    caper
    3
    
    >>> play_with_word('hello', ['hello', 'salut', 'alloo'])
    Enter a guess: bonjour
    Not a valid word, please enter a new one.
    Enter a guess: hello
    hello
    1
    
    >>> play_with_word('leave', ['about', 'ladle', 'plate', 'plane', 'click',
    'guess', 'world', 'leave'])
    Enter a guess: about
    about
    Enter a guess:ladle
    about
    ladle
    Enter a guess:plate
    about
    ladle
    plate
    Enter a guess:plane
    about
    ladle
    plate
    plane
    Enter a guess:click
    about
    ladle
    plate
    plane
    click
    Enter a guess:guess
    about
    ladle
    plate
    plane
    click
    guess
    Enter a guess:world
    7
    
    """
    wordle = wordle.lower() 
    
    guess = input("Enter a guess: ").lower()
    
    num_guess = 1
    
    display_word = []
    
    while guess != wordle and num_guess < MAX_NUM_OF_GUESSES: 
        
        if not is_valid_word(guess, list_words):
            print('Not a valid word, please enter a new one.')
            
        else:
            num_guess += 1
            colored = compare_and_color_word(guess, wordle)
            display_word.append(colored) #adding colored word to the list
            print_string_list(display_word)
            
        guess = input('Enter a guess:').lower() #ask for input again
                    
    if guess == wordle: #if right answer
        display_word.append(compare_and_color_word(guess, wordle))
        print_string_list(display_word)
        return num_guess
    
    else: #if no chance left for guessing
        return MAX_NUM_OF_GUESSES + 1
    
def compare_and_color_word(guess, wordle):
    """(str, str) -> str
    takes two strings, the first one is the guessed word and the second one the
    solution word. The function compares the guessed word to the solution word
    letter by letter and color each letter accordingly.

    >>> compare_and_color_word('mount', 'about')
    '\x1b[6;30;47mm\x1b[0m\x1b[6;30;43mo\x1b[0m\x1b[6;30;43mu\x1b[0m\x1b[6;30;47mn\x1b
    [0m\x1b[6;30;42mt\x1b[0m'
        
    >>> compare_and_color_word('hello', 'bello')
    '\x1b[6;30;47mh\x1b[0m\x1b[6;30;42me\x1b[0m\x1b[6;30;42ml\x1b[0m\x1b[6;30;42ml\x1b[0m
    \x1b[6;30;42mo\x1b[0m'
    
    >>> compare_and_color_word('ultra', 'tralu')
    '\x1b[6;30;43mu\x1b[0m\x1b[6;30;43ml\x1b[0m\x1b[6;30;43mt\x1b[0m\x1b[6;30;43mr\x1b[0m
    \x1b[6;30;43ma\x1b[0m'

    """
    display_str = ""
    
    #letters that are not guessed
    left_letters = wordle 
    
    for char in range(len(guess)):
        
        if wordle[char] == guess[char]: #letter at the right index
            display_str += color_string(guess[char], 'green')
            left_letters = left_letters.replace(guess[char],'',1) #to exclude the guessed letter
            
        else:
            display_str += color_string(guess[char], 'gray')
          
    for c in range(len(guess)): #color letters in yellow
        
        if (guess[c] != wordle[c]) and (guess[c] in left_letters): 
            
            colored = color_string(guess[c], 'yellow')
            gray_letter = CHAR_GRAY + guess[c] + CHAR_END
            display_str = display_str.replace(gray_letter, colored ,1)
            left_letters = left_letters.replace(guess[c], '', 1)
            
    return display_str

def print_final_message(num_guess, wordle):
    """(str, str) -> NoneType

    The function returns nothing. It prints the final message of the game indicating
    whether the player has lost or won. The function decides whether the player has
    won or lost according to the guessed words.
     
    >>> print_final_message(4, 'hello')
    You won! It took you 4 guesses.
    
    >>> print_final_message(7, 'about')
    You lost! The word was about
    
    >>> print_final_message(7, 'salut')
    You lost! The word was salut
    
    """
    if num_guess <= MAX_NUM_OF_GUESSES:
        print('You won! It took you', num_guess, 'guesses.')
        
    else:
        answer = color_string(wordle, 'green')
        print('You lost! The word was', answer)
        
        
#start playing
main()
    