# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:41:31 2021

@author: javid
"""


# Display function
def display(game_board):

    l1 = game_board['l1']
    l2 = game_board['l2']
    l3 = game_board['l3']

    print('    THE BOARD  ')
    print('    0   1   2')
    print(f'0 | {l1[0]} | {l1[1]} | {l1[2]} |')
    print(f'1 | {l2[0]} | {l2[1]} | {l2[2]} |')
    print(f'2 | {l3[0]} | {l3[1]} | {l3[2]} |')


# Player1 iloc(the location player1 wanna play(i = row, j = column))
def player1_iloc():
    print('#PLAYER1# Please enter your location you wanna play: ')
    while True:
        i = input('ROW: (0-1-2)')
        if i not in ['0', '1', '2']:
            print('Please input correct number: (0-1-2)')
        else:
            break
    while True:
        j = input('COLUMN: (0-1-2)')
        if j not in ['0', '1', '2']:
            print('Please input correct number: (0-1-2)')
        else:
            break

    return int(i), int(j)


# Player2 iloc(the location player2 wanna play(i = row, j = column))
def player2_iloc():
    print('#PLAYER2# Please enter your location you wanna play: ')
    while True:
        i = input('ROW: (0-1-2)')
        if i not in ['0', '1', '2']:
            print('Please input correct number: (0-1-2)')
        else:
            break
    while True:
        j = input('COLUMN: (0-1-2)')
        if j not in ['0', '1', '2']:
            print('Please input correct number: (0-1-2)')
        else:
            break

    return int(i), int(j)


# convert player1 location choice to the game_board location
# check if the location player1 wanna play is full or empty
# if empty: replace the location with 'X' for player1
def player1_update_board(game_board, i, j):

    game_board_index = ['l1', 'l2', 'l3']
    choice_i = game_board_index[i]

    if game_board[choice_i][j] == '-':
        game_board[choice_i][j] = 'X'
        full_cell = False
    else:
        print('SORRY, NOT EMPTY CELL!, Please Try again')
        full_cell = True

    return full_cell


# convert player2 location choice to the game_board location
# check if the location player2 wanna play is full or empty
# if empty: replace the location with 'O' for player2
def player2_update_board(game_board, i, j):

    game_board_index = ['l1', 'l2', 'l3']
    choice_i = game_board_index[i]

    if game_board[choice_i][j] == '-':
        game_board[choice_i][j] = 'O'
        full_cell = False
    else:
        print('SORRY, NOT EMPTY CELL!, Please Try again')
        full_cell = True

    return full_cell


# check all options if player1 is winning the game
# return 1 for player1 wins, return false for not
def victory_player1_check(game_board):

    a = game_board['l1'][0] == game_board['l1'][1] == game_board['l1'][2] == 'X'
    b = game_board['l2'][0] == game_board['l2'][1] == game_board['l2'][2] == 'X'
    c = game_board['l3'][0] == game_board['l3'][1] == game_board['l3'][2] == 'X'

    d = game_board['l1'][0] == game_board['l2'][0] == game_board['l3'][0] == 'X'
    e = game_board['l1'][1] == game_board['l2'][1] == game_board['l3'][1] == 'X'
    f = game_board['l1'][2] == game_board['l2'][2] == game_board['l3'][2] == 'X'

    g = game_board['l1'][0] == game_board['l2'][1] == game_board['l3'][2] == 'X'
    h = game_board['l1'][2] == game_board['l2'][1] == game_board['l3'][0] == 'X'

    if a or b or c or d or e or f or g or h:
        victory_mod = 1
    else:
        victory_mod = False

    return victory_mod


# check all options if player2 is winning the game
# return 2 for player2 wins, return false for not
def victory_player2_check(game_board):

    a = game_board['l1'][0] == game_board['l1'][1] == game_board['l1'][2] == 'O'
    b = game_board['l2'][0] == game_board['l2'][1] == game_board['l2'][2] == 'O'
    c = game_board['l3'][0] == game_board['l3'][1] == game_board['l3'][2] == 'O'

    d = game_board['l1'][0] == game_board['l2'][0] == game_board['l3'][0] == 'O'
    e = game_board['l1'][1] == game_board['l2'][1] == game_board['l3'][1] == 'O'
    f = game_board['l1'][2] == game_board['l2'][2] == game_board['l3'][2] == 'O'

    g = game_board['l1'][0] == game_board['l2'][1] == game_board['l3'][2] == 'O'
    h = game_board['l1'][2] == game_board['l2'][1] == game_board['l3'][0] == 'O'

    if a or b or c or d or e or f or g or h:
        victory_mod = 2
    else:
        victory_mod = False

    return victory_mod


# check if all locations are empty or not
# if anyone didn't win and the board_game is full, then the game is draw!
def draw_analyz(game_board):

    a = '-' not in game_board['l1']
    b = '-' not in game_board['l2']
    c = '-' not in game_board['l3']

    return a and b and c


# just have fun
def tic_tac_toe_have_fun():

    # import clear_output for clearing out every game round
    from IPython.display import clear_output

    # Welcome message
    print('\nHello Welcome to Two-player Tic-tac-toe game.\n')

    # Initial game_list
    game_board = {'l1': ['-', '-', '-'],
                  'l2': ['-', '-', '-'], 'l3': ['-', '-', '-']}

    # Initial victory mod and draw analyz state for starting while loop
    victory_mod = False
    draw_analyz_state = False

    # Displaying first view of the game_board
    display(game_board)

    # Starting while loop for maintaing game rounds
    # Until a player victory the game or be draw
    while (victory_mod is False) and (draw_analyz_state is False):

        # full_cell assigned true to starting while loop
        full_cell = True

        # while loop keep asking player for location
        # until player select an empty location
        while full_cell is True:

            i1, j1 = player1_iloc()

            clear_output()

            full_cell = player1_update_board(game_board, i1, j1)

            display(game_board)

        # cheking victory mod after player1 made a choice
        victory_mod = victory_player1_check(game_board)

        # cheking draw states after player1 made a choice
        # because player1 is the last player who make a choice
        draw_analyz_state = draw_analyz(game_board)

        # for cheking victory mod and draw analyz after player1 makes a move
        # if not, player2 will start to play
        if (victory_mod is False) and (draw_analyz_state is False):

            full_cell = True

            while full_cell is True:

                i2, j2 = player2_iloc()

                clear_output()

                full_cell = player2_update_board(game_board, i2, j2)

                display(game_board)

            victory_mod = victory_player2_check(game_board)

    # after ending while loop for game rounds, it's time to check the state
    if victory_mod == 1:
        print('  ******* ****\n  PLAYER1 WINS\n  ******* ****')
    elif victory_mod == 2:
        print('  ******* ****\n  PLAYER2 WINS\n  ******* ****')
    elif draw_analyz_state is True:
        print('  ******* ****\n  ___DRAW!___ \n  ******* ****')

    # have fun


tic_tac_toe_have_fun()


# for exit after game is done with press any key
input('press any key for exit')
