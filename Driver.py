from spaceship import *
from graphics import *
import turtle
import random

SHIP_FUNCTIONS = [draw_body, draw_window, draw_left_fin,
                    draw_right_fin, draw_fire]

SHIP_COLORS = [(85, 0, 0), (170, 57, 57)]
FIRE_COLORS = [(85, 0, 0), (255, 206, 0)]
WINDOW_COLORS = [(111, 77, 143), (146, 119, 172)]

def draw_ship_parts(ship, wrong_guess_list):
    '''
        name: draw_ship_names
        parameters: ship -- a turtle object
                    wrong_guess_list -- a list of strings (wrong guesses)
        returns: nothing
        does: checks which part of the rocket to draw and draws that part
    '''
    if len(wrong_guess_list) == 2:
        SHIP_FUNCTIONS[len(wrong_guess_list) - 1](ship, WINDOW_COLORS[0],
                                                    WINDOW_COLORS[1])

    elif len(wrong_guess_list) == 5:
        SHIP_FUNCTIONS[len(wrong_guess_list) - 1](ship, FIRE_COLORS[0],
                                                    FIRE_COLORS[1])

    else:
        SHIP_FUNCTIONS[len(wrong_guess_list) - 1](ship, SHIP_COLORS[0],
                                                    SHIP_COLORS[1])

def main():

    # generate the word dictionary from the file
    # wordlist.txt
    dictionary = generate_word_list('wordlist.txt')

    # call the function that makes them all lowercase
    lower_case_letters(dictionary)

    wins = 0
    ship = turtle.Turtle()

    while True:
        # clear the screen for each loop
        # and hide the turtle object
        ship.clear()
        ship.reset()
        ship.hideturtle()

        # draw the background (not part of a wrong guess)
        draw_background(ship)

        # choose a random word from the dictionary
        word = random.choice(dictionary)

        # generate a list keeping track of current game
        word_bank = build_blank_word_bank(word)

        # initialize the wrong guess list
        wrong_guess_list = []

        # draw the blank underscores in turtle
        draw_underscores(ship, word)

        # iterate over the word
        # if the word has a non-alpha character
        # add it to the word bank and write it in turtle
        for character in word:
            if not character.isalpha():
                add_to_word_bank(character, word, word_bank)
                write_non_alpha(ship, word, word_bank)

        # loop the game while the user hasn't lost
        # the user loses when they guess 5 wrong guesses
        while len(wrong_guess_list) < 5:
            guess = ''

            # keep prompting if the string is < 0 or > 1
            while not is_valid_guess(guess):
                guess = input('Which letter?\n')

            # if they give a unique guess
            # (not a correct or incorrect guess)...
            if validate_unique_guess(guess, word_bank, wrong_guess_list):

                # if the letter is in the word,
                # add it to the word bank and write the guess
                # to the terminal
                if guess in word:
                    add_to_word_bank(guess, word, word_bank)
                    write_good_letter(ship, guess, word_bank)

                # if it's not, add the guess to the wrong guess list
                # write the letter to turtle
                # and draw a ship part.
                else:
                    add_wrong_guess(guess, wrong_guess_list)
                    write_bad_letter(ship, guess, wrong_guess_list)
                    draw_ship_parts(ship, wrong_guess_list)

            # if the guess is not unique
            # (it was guessed already)...
            else:
                # add the guess to the wrong guess list
                # write the letter to turtle
                # and draw a ship part.
                add_wrong_guess(guess, wrong_guess_list)
                write_bad_letter(ship, guess, wrong_guess_list)
                draw_ship_parts(ship, wrong_guess_list)

            # check if the game is over
            # (if the word bank matches the word)
            if check_end_game(word_bank, word):

                # increment wins and print to the terminal
                wins += 1
                print('Yay! You won!')
                print('You\'ve won', wins, 'games so far!')
                break

        # now that the loop is over (either by winning or losing)
        # check if it was a loss. If so, print to the terminal.
        if len(wrong_guess_list) == 5:
            print('Sorry, you lost. The word was ', word, '.', sep = '')
            print('You won', wins, 'games.')

        # ask the user if they want to play again
        # if not, break out of the loop. If yes,
        # the loop continues.
        if not play_again():
            print('Come back soon!')
            break

    # ask the user for their name to update the scores file
    user = input('Hey space cowboy, what\'s your name?\n')

    # check if the player's score is a high score.
    # if it is, overwrite the scores file
    # if not, append the score to the bottom
    if check_high_score(wins, 'scores.txt'):
        write_high_score(user, wins, 'scores.txt')

    else:
        write_low_score(user, wins, 'scores.txt')


main()
