# MASTERMIND COMPUTER GAME
# 3 menu options - start, instructions, statistics (using if-elif-else statements)
# developer password: lilian (to print code before game start as usual)
# a random 4 color code is generated (repetition in the code is allowed)
# the maximum number of tries is 10. if the user guesses within 10 tries they win.
# answer example: W,B,G,R (seperated by commas & not case sensitive)
# after each round, they can view their statistics.
# user can also choose to play again. the statistics will be retained & can be seen if they choose menu input 3.

## double hashes refer to a continuation of the comment in the next line.

import random

### DEFINING SUBPROGRAMS ###

# FUNCTION TO PRINT GAME MENU
def menu():
    print('''
============================== M A S T E R M I N D ==============================
                                    Welcome!

                             Guess the 4 colour code
                                  in 10 tries!

                           Enter (1) to start the game.
                      Enter (2) for How To Play & Colour List.
                           Enter (3) for Game Statistics.
    ''')

# FUNCTION TO PRINT 'HOW TO PLAY'
def howtoplay():
    print('''
                H O W   T O   P L A Y                   |     Colour List     |
                                                        |                     |
(1) The computer will generate a random 4 colour        |     (W) White       |
    code (repetition allowed) which you will            |                     |
    have to guess in 10 tries.                          |     (B) Blue        |
                                                        |                     |
(2) Enter your guess as a sequence of 4 letters from    |     (G) Green       |
    the given list which represents the colours.        |                     |
    Answer example: W,B,G,R (not case sensitive)        |     (R) Red         |
                                                        |                     |
(3) Use the number of 'correct colours in the correct   |     (P) Purple      |
    place' and correct colours but in the wrong place'  |                     |
    to help you guess!                                  |     (C) Cyan        |
                                                        |                     |
(4) If all the colours you chose are in the correct     |                     |
    positions, you win!                                 |                     |

=================================================================================
''')

# FUNCTION TO GENERATE STATISTICS
stats_list = [0]                    ## 0 is in the list by default as the user may choose to view their stats before
def stats(win, lose):               ## starting or winning the game, thus displaying their average tries as 0.
    if (len(stats_list) - 1) == 0:      # The -1 in the counting of the list length is to accomodate for the 0 already in the list.
        average = 0                 # The if-else statement is used to avoid error from dividing a number by 0.
    else:                       
        average = sum(stats_list) // ((len(stats_list) - 1))
    print(' ' * 30 + 'S T A T I S T I C S')
    print('\nOn average, you took', average, 'tries to guess the code.')
    print('Games Won = ', win)
    print('Games Lost = ', lose)

# FUNCTION TO GENERATE RANDOM CODE
def generate_code():
    global colors
    colors = ['W', 'B', 'G', 'R', 'P', 'C']
    code = []
    for i in range(4):
        code.append(random.choice(colors))
    return code

# FUNCTION TO CHECK THE USER'S GUESS
def check(code, guess):
    correctplace = 0    
    wrongplace = 0       
    code_copy = list(code)      # Create a copy of the code list from which we can remove elements which the user has guessed to avoid double counting.
    if len(guess) == len(code):
        for i in range(len(guess)):
            if guess[i] == code[i]:     ## If the element at the same index of the generated code and the user's guess match, 
                correctplace += 1       ## count it as a correct colour in the correct place.
            if code_copy.count(guess[i]) > 0:   ## If an element of the user's guess appears at least once in the generated code,
                wrongplace += 1                 ## count it as a correct colour in the wrong place & remove it to avoid double counting.
                code_copy.remove(guess[i])
        wrongplace -= correctplace              ## Minus the number of correct places from wrong places because the wrong places
    return(correctplace, wrongplace)            ## counted guesses present in the [code list] which includes correct places.

### START PROGRAM ###

# Variable initiation outside of the replay loop.
play_again = 'Y'
win = 0
lose = 0
maxattempts = 10

# REPLAY WHILE LOOP
while play_again == 'Y':

# Variable initiation inside the replay loop.
    tries = 1
    guess = []

# Call the function to generate the randomized code and obtain the user's start menu input.
    code = generate_code()
    menu()
    start = input(' ' * 30 + 'Enter 1, 2 or 3 = ')
    print('=' * 81)

# Display respective outputs from start menu options.

    # If statement for is user chooses to start the game (1 or 'lilian').
    if start == '1' or start == 'lilian':

        # If input is the developer password to display the code before the game starts.
        if start == 'lilian':
            print(code)

        # While loop for the game rounds which runs a maximum of 10 times.
        while guess != code and tries <= maxattempts:
            guess = []
            print()
            print('-'* 32 + ' Attempt ' + str(tries) + ' ' + 'of 10' + ' ' + '-'*32)
            print()
            print('Pick between [W, B, G, R, P, C]. Repetition is allowed. \n')

            # User's guess input.
            raw_guess = str.upper(input('Enter 4 colours seperated by commas (Eg: W,W,W,W): '))
            guess = raw_guess.split(',') # Splits the elements of the user's guess between the commas into a list of 4 elements.

            # Only class it as a guess if all these conditions are fulfilled. The else part will print the error message.
            if len(raw_guess) == 7 and (guess[0] in colors) and (guess[1] in colors) and (guess[2] in colors) and (guess[3] in colors):
            
            # Call the function to check if the guess is the same as the code.
                correctplace, wrongplace = check(code, guess)

                # Output if user wins.
                if guess == code:
                    print('\nYou won! The code is', code)
                    try_plural = 'tries.'         ## To ensure that the singular and plural form
                    if tries == 1:                ## of the word 'try' is used appropriately.
                        try_plural = 'try.'
                    print('You took', tries, try_plural, '\n')
                    win += 1
                    stats_list.append(tries)        # Append number of tries to stats list if user wins.

                # Output if user's guess is incorrect, allowing them to try again.
                elif guess != code:
                    try_plural = 'tries'    # Ensures that try/tries are used correctly.
                    if maxattempts - tries == 1:
                        try_plural = 'try'
                    print('Correct colour in the correct place: ', correctplace)
                    print('Correct colour but in the wrong place: ', wrongplace)
                    print('You have', maxattempts - tries, try_plural, 'remaining.')
                    print()
                    # Increment counter for the number of attempts.
                    tries += 1

            # Error handling for invalid user input for the guess.
            else:
                print('Invalid Input. Please enter 4 colours from the list ONLY and seperate them with commas.')

        # Output if user loses (10 attempts exceeded without guessing the code).
        if tries > maxattempts:
            print('Sorry, you lose. The code was', code)
            print()
            lose += 1

        # Allow the user to choose to view their statistics after each game.
        show_stats = str.upper(input('Would you like to view your Game Statistics? [Y/N] '))
        if show_stats == 'Y':
            print('=' * 79)
            print()
            average = stats(win, lose)
            print()

        # Allow the user to play again or exit the program.
        play_again = str.upper(input('Play Again? [Y/N] '))
        if play_again != 'Y':
            print('\nBye bye!')

    # If user chooses to display 'How to Play'.
    elif start == '2':
        howtoplay()
        back = input('\nEnter any key to return to the main menu.')

    # If user chooses to display game statistics.
    elif start == '3':
        print()
        stats(win, lose)
        back = input('\nEnter any key to return to the main menu.')

    # Error handling for invalid user input in the start menu.
    else:
        print('Invalid input. Choose 1, 2 or 3 only.')

# PROGRAM END
