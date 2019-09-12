import turtle
import spaceship

def draw_background(bg):
    '''
        name: draw_background
        parameters: turtle object
        does: draws a sweet space background with
            a big planet that the spaceship is on
            and a smaller planet in the background.
    '''

    # set background color to dark purple
    turtle.colormode(255)
    turtle.bgcolor('#18101F')

    # Draw the big planet
    bg.pensize(2)

    # set pen color to dark purple
    bg.pencolor(68, 37, 92)
    bg.penup()
    bg.goto(0, -40)
    bg.pendown()
    bg.fillcolor(169, 106, 217)
    bg.begin_fill()
    bg.speed(0)

    # to get a big curve, draw a big circle
    bg.circle(-1500, 360)
    bg.end_fill()
    bg.speed(10)
    bg.penup()

    # background planets
    # essentially setting fill and pen colors
    # going to where the planet should be
    # and drawing circles of different sizes
    bg.pencolor(111, 77, 143)
    bg.pensize(1)
    bg.goto(-300, 300)
    bg.pendown()
    bg.begin_fill()
    bg.fillcolor(146, 119, 172)
    bg.circle(15, 360)
    bg.end_fill()
    bg.penup()
    bg.goto(-270, 330)
    bg.begin_fill()
    bg.fillcolor(200, 119, 172)
    bg.circle(5, 360)
    bg.end_fill()

def draw_body(ship, line_color, fill_color):
    '''
        name: draw_body
        parameters: ship -- a turtle object
                    line_color -- a tuple of rgb values (r, g, b)
                    fill_color -- a tuple of rgb values (r, g, b)
        does: draws the sweet rocket body using straight lines and
            curves using the given color tuple, then fills the body with
            the tuple color given.
    '''

    ship.speed(10)
    ship.pensize(3)
    ship.begin_fill()
    turtle.colormode(255)
    ship.pencolor(line_color)
    ship.fillcolor(fill_color)

    ship.penup()
    ship.goto(-100, -100)
    ship.pendown()

    # draw the bottom curve
    ship.setheading(-10)

    # in 5 steps, go forward 35
    # and turn left 5
    for _ in range(5):
        ship.forward(35)
        ship.left(5)

    ship.setheading(90)
    # drawing right edge
    ship.forward(200)

    # drawing the nose-cone
    ship.circle(87, 180)

    # drawing the left edge
    ship.forward(200)

    ship.end_fill()

def draw_left_fin(ship, line_color, fill_color):
    '''
        name: draw_left_fin
        parameters: ship -- a turtle object
                    line_color -- a tuple of r, g, b values (r, g, b)
                    fill_color -- a tuple of r, g, b values (r, g, b)
        does: draws a left fin that goes out way too much from
            the base of the rocket using circles with inverted radii.
            The line color is set with line_color, and the fill color
            set with fill_color.
    '''

    ship.speed(10)
    ship.penup()
    ship.goto(-100.33, -30)
    ship.setheading(200)
    ship.pencolor(line_color)
    ship.pensize(3)
    ship.pendown()

    ship.begin_fill()
    ship.fillcolor(fill_color)
    ship.circle(130, 90)
    ship.setheading(70)
    ship.circle(-200, 36.5)
    ship.setheading(90)
    ship.forward(72)
    ship.end_fill()

def draw_right_fin(ship, line_color, fill_color):
    '''
        name: draw_right_fin
        parameters: ship -- a turtle object
                    line_color -- a tuple of r, g, b values (r, g, b)
                    fill_color -- a tuple of r, g, b values (r, g, b)
        does: draws a right fin that goes out way too much from
            the base of the rocket using circles with inverted radii
    '''

    ship.speed(10)
    ship.penup()
    ship.goto(73.67, -30)
    ship.setheading(-20)
    ship.pencolor(line_color)
    ship.pensize(3)
    ship.pendown()

    ship.begin_fill()
    ship.fillcolor(fill_color)
    ship.circle(-130, 90)
    ship.setheading(110)
    ship.circle(200, 36.5)
    ship.setheading(90)
    ship.forward(72)
    ship.end_fill()

def draw_window(ship, line_color, fill_color):
    '''
        name: draw_window
        parameters: ship -- a turtle object
                    line_color -- a tuple of r, g, b values (r, g, b)
                    fill_color -- a tuple of r, g, b values (r, g, b)
        does: draws a really quaint window on the ship that reminds
            you of home. The home you never were able to get back to
            and are now stuck on planet Guessaword
    '''

    ship.speed(10)
    ship.penup()
    ship.goto(-30, 90)
    ship.pendown()
    ship.pencolor(line_color)
    ship.pensize(4)

    ship.begin_fill()
    ship.fillcolor(fill_color)
    ship.circle(15, 360)
    ship.end_fill()

def draw_fire(ship, line_color, fill_color):
    '''
        name: draw_fire
        parameters: ship -- a turtle object
                    line_color -- a tuple of r, g, b values (r, g, b)
                    fill_color -- a tuple of r, g, b values (r, g, b)
        does: draws a really cool flame under the rocket using the given
            color tuples and the turtle object.
            It makes you feel like going "PSSSHHHH"
    '''

    ship.speed(0)
    ship.pensize(3)
    ship.penup()
    ship.goto(73.67, -100)
    ship.setheading(270)
    ship.pendown()
    ship.pencolor(line_color)

    ship.begin_fill()
    ship.fillcolor(fill_color)
    ship.circle(100, 30)
    ship.circle(-100, 60)

    ship.setheading(90)
    ship.circle(100, 60)

    ship.setheading(230)
    ship.circle(100, 40)
    ship.circle(-100, 40)

    ship.setheading(90)
    ship.circle(100, 40)
    ship.circle(-100, 30)

    ship.setheading(250)
    ship.circle(100, 20)
    ship.circle(-100, 30)

    ship.setheading(90)
    ship.circle(100, 40)
    ship.circle(-70, 70)
    ship.circle(40, 30)
    ship.goto(-100, -100)

    ship.setheading(-10)
    for _ in range(5):
        ship.forward(35)
        ship.left(5)

    ship.end_fill()
    ship.speed(10)

def draw_underscores(ship, word):
    '''
        name: draw_underscores
        parameters: ship -- a turtle object
                    word -- the word the user is trying to guess (a string)
        does: draws an underscore for each letter in the given string (word)
                it draws these in the bottom right of the screen
    '''
    # word = spaceship._remove_nonalpha(word)

    ship.penup()
    ship.pencolor(255, 255, 255)
    ship.goto(300, -300)
    ship.setheading(180)
    ship.pendown()
    for letter in word:
        ship.forward(20)
        ship.penup()
        ship.forward(10)
        ship.pendown()

def write_good_letter(ship, letter, word_bank):
    '''
        name: write_good_letter
        parameters: ship -- a turtle object
                    letter -- the letter that the user has guessed (a string)
                    word_bank -- a list of strings keeping track of the
                                current status of the game.
        does: writes the correct letters in the correct spaces. It iterates
            over the word_bank and tries to match the letter with the
            element in the word_bank. If the two match, the turtle moves
            forward (to the right) 30 * the index of the letter in word_bank.
            For example: if the word_bank looks like ['_', '_', 'f', '_'],
            the turtle will start at (90, -300) and, since 'f' is in the
            third slot (or index 2), it adds 30 * 2 = 60 to the x coordinate
            of the turtle object and writes the letter at (150, -300).
    '''

    ship.penup()
    ship.pensize(5)
    ship.pencolor(255, 255, 255)
    for index in range(len(word_bank)):
        if word_bank[index] == letter:
            ship.goto(290 - (30 * ((len(word_bank) - 1) - index)), -300)
            ship.pendown()
            ship.write(letter, False, 'center',
                        font=('Arial', 16, 'normal'))
            ship.penup()

def write_bad_letter(ship, letter, wrong_guess_list):
    '''
        name: write_bad_letter
        parameters: ship -- a turtle object
                    letter -- the letter the user has guessed (a string)
                    wrong_guess_list -- a list of letters (strings) the user
                                        has guessed incorectly
        does: writes a letter in the bottom left corner of the turtle window.
            It iterates over the list of wrong guesses and tries to match the
            letter with the element in the list. If the two match,
            the turtle moves forward (to the right) 30 * the index of the
            letter in list.

            For example: if the list looks like ['x', 'b', 'f'],
            the turtle will start at (-300, -300) and, since 'f' is in the
            third slot (or index 2), it adds 30 * 2 = 60 to the x coordinate
            of the turtle object and writes the letter at (-240, -300).
    '''

    ship.penup()
    ship.speed(6)
    ship.goto(-300, -300)
    ship.pencolor(255, 255, 255)
    for index in range(len(wrong_guess_list)):
        if wrong_guess_list[index] == letter:
            ship.goto(-300 + (30 * index), -300)
            ship.pendown()
            ship.write(letter, False, 'center',
                        font=('Arial', 16, 'normal'))
            ship.penup()

def write_non_alpha(ship, word, word_bank):
    '''
        name: write_non_alpha
        parameters: ship -- a turtle object
                    word -- a string (the word to guess)
                    word_bank -- list of strings (current game progress)
        does: searches the word for a non-alpha character
            and writes it in the appropriate space.
    '''

    for character in word:
        if not character.isalpha():
            write_good_letter(ship, character, word_bank)
