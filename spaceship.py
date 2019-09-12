'''
    CS5001
    Fall 2018
    Jake Mittleman
    HW 5
'''

import random

def generate_word_list(filename):
    '''
        name: generate_word_list
        parameters: filename -- a string
        returns: a list of strings
        does: Reads a file of words and generates a list where each element
            is a word
    '''
    try:
        infile = open(filename, 'r')
        all_words = infile.read()
        word_dictionary = all_words.splitlines()
        for index in range(len(word_dictionary)):
            word_dictionary[index] = word_dictionary[index].strip()
        infile.close()

    except OSError:
        return []

    return word_dictionary

def lower_case_letters(dictionary):
    '''
        name: lower_case_letters
        parameters: dictionary -- a list of strings
        returns: nothing
        does: iterates over the dictionary and makes the string lowercase
    '''

    for index in range(len(dictionary)):
        dictionary[index] = dictionary[index].lower()

def _get_letter_indexes(letter, word):

    indexes = []

    for character in range(len(word)):
        if word[character] == letter:
            indexes.append(character)

    return indexes


def build_blank_word_bank(word):
    '''
        name: build_blank_word_bank
        parameters: word -- a string (the word the user is trying to guess)
        returns: a list
        does: takes the word the player is trying to guess and builds a
            list of the same length with as many underscores as there are
            letters in word. A blank word bank could look like this:
            ['_', '_', '_', '_']. The underscores represent letters the
            player hasn't guessed yet.
    '''

    word_bank = []
    for letter in range(len(word)):

        # skips any non-alphabetic characters
        '''
        if not word[letter].isalpha():
            continue

        else:
        '''
        word_bank.append('_')

    return word_bank

def add_to_word_bank(letter, word, word_bank):
    '''
        name: add_to_word_bank
        parameters: letter (a string) -- the player's guess
                    word (a string) -- the word the player's trying to guess
                    word_bank (a list) -- a list that's the current
                                        status of the game
        returns: nothing
        does: adds the letter to the word bank. Calls hidden function
            _get_letter_indexes which returns a list of ints and each
            is an index where the letter is present. Then the function
            iterates over the list of indexes and changes the word bank
            at those indexes to the guessed letter.

            For example: if the word was 'baby' and the player guessed 'b',
            _get_letter_indexes would return [0, 2]. Then the word bank
            changes as such: ['_', '_', '_', '_'] ---> ['b', '_', 'b', '_']
    '''

    indexes = _get_letter_indexes(letter, word)

    for index in indexes:
        word_bank[index] = letter

def check_end_game(word_bank, word):
    '''
        name: check_end_game
        parameters: word_bank -- a list of strings
                    word -- a string (the word the user is trying to guess)
        returns: True or False. True if the game is won, False if the game
                is still being played.
        does: compares the word_bank to the word. The word is what the
                player is trying to guess. The word bank is a list of
                either alphabetic characters or underscores. It keeps
                track of the game.
    '''

    for index in range(len(word)):
        if word_bank[index] == word[index]:
            continue
        else:
            return False
    return True

def validate_unique_guess(guess, word_bank, wrong_guess_list):
    '''
        name: validate_unique_guess
        parameters: guess -- a string (the user's guess)
                    word_bank -- a list of already guessed letters
                    wrong_guess_list -- a list of incorrect guesses
        does: returns True if the letter hasn't been guessed already
                and returns False if it has.
    '''
    if guess.isalpha() and len(guess) == 1:
        return guess not in word_bank and \
                guess not in wrong_guess_list
    else:
        return False

def is_valid_guess(guess):

    return len(guess) == 1

def add_wrong_guess(letter, wrong_guess_list):
    '''
        name: add_wrong_guess
        parameters: letter -- (a string)
                    list -- (a list of wrong guesses)
        does: appends a wrong guess to a list
    '''
    return wrong_guess_list.append(letter)


def play_again():
    '''
        name: play_again
        parameters: none
        returns: True or False
        does: asks the player if they want to play again.
                if so, return True. If not, return False.
    '''

    user_input = input('Want to play again? Y/N\n')
    user_input = user_input.upper()

    if user_input in ('Y', 'YES'):
        return True
    elif user_input in ('N', 'NO'):
        return False

def read_scores(filename):
    '''
        name: read_scores
        parameters: filename -- a string
        returns: a list
        does: reads the file and generates a list of the following structure:
            [['Name'], [Score].....['Name'], [Score]]. Name is a string
            and Score is an int. If the file can't be found, returns
            an empty list.
    '''

    try:
        # open the file and process the file
        infile = open(filename, 'r')
        all_lines = infile.read()
        lines = all_lines.splitlines()

        # create the list to store the data
        scores = []

        # for each item in lines (a line is like 'Name Score'
        # or 'Firstname Lastname Score')...
        # split from the right-most space
        for item in lines:
            if lines != '':
                temp_list = item.rsplit(' ', 1)

                # create a temporary list with the structure ['Name', 'Score']
                # or ['First Name', 'Score']
                scores.append(temp_list[0])
                scores.append(temp_list[1])
        infile.close()
        return scores

    except OSError:
        return []

def check_high_score(score, filename):
    '''
        name: check_high_score
        parameters: score -- an int
                    filename -- a string
        returns: True or False
        does: checks if the player's score is a high score.
            If read_scores comes back with an empty list, it is considered
            a high score and the function returns True. Otherwise if
            the score is higher than the current high score, returns True.
            Otherwise, return False
    '''

    scores = read_scores(filename)

    if not scores:
        return True

    elif score >= int(scores[1]):
        return True

    return False

def write_high_score(user, score, filename):
    '''
        name: write_high_score
        parameters: user -- a string (the player's name)
                    score -- an int (the player's number of wins)
                    filename -- a string (the scores filename)
        returns: nothing
        does: Writes a high score to the filename. If read_scores returns
            an empty list, it merely writes the high score and closes the
            file. If scores has a length > 0, it writes the rest of the
            scores to the file.
    '''

    scores = read_scores(filename)
    index = 0

    try:
        outfile = open(filename, 'w')
        outfile.write(user + ' ' + str(score) + '\n')
        if len(scores) > 0:

            # we iterate through scores by 2 (name and score)
            # and write the name + score to the file.
            while index < len(scores):
                outfile.write(scores[index] + ' ' + scores[index + 1] + '\n')
                index += 2

        outfile.close()

    except OSError:
        print('Sorry, technical difficulties')

def write_low_score(user, score, filename):
    '''
        name: write_low_score
        parameters: user -- a string (the player's name)
                    score -- an int (the number of wins)
                    filename -- a string (the scores file)
        returns: nothing
        does: writes the user and their score to the file
    '''

    try:
        outfile = open(filename, 'a')
        outfile.write(user + ' ' + str(score) + '\n')
        outfile.close()

    except OSError:
        print('There seems to be an error.')


###################
# Console Testing #
###################
def print_word_bank(word_bank):

    for index in range(len(word_bank)):
        if index == len(word_bank) - 1:
            print(word_bank[index], sep = '', end = '')
        else:
            print(word_bank[index], '  ', sep = '', end = '')

    print('\n')
