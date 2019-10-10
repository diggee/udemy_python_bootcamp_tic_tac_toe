from IPython.display import clear_output

def print_example_board():
    print('Number scheme of the tic tac toe board is given below')
    print('Each number corresponds to the position on the board where an entry will be made by typing that number')
    print('Please do not give an input outside the number range shown. Specially alphabets. It will crash the program.\n')

def print_board(dict1):
    print('Number scheme on board')
    print('\n7|8|9\n4|5|6\n1|2|3\n\n')
    print(dict1[7]+'|'+dict1[8]+'|'+dict1[9]+'\n'+dict1[4]+'|'+dict1[5]+'|'+dict1[6]+'\n'+dict1[1]+'|'+dict1[2]+'|'+dict1[3])

def update_board(turn_no):
    if turn_no%2==0:
        return 'O'
    else:
        return 'X'

def winner_check(dict1):
    rO = (dict1[1]=='O' and dict1[2] =='O' and dict1[3] =='O') or (dict1[4]=='O' and dict1[5] =='O' and dict1[6] =='O') or (dict1[7]=='O' and dict1[8] =='O' and dict1[9] =='O')
    rX = (dict1[1]=='X' and dict1[2] =='X' and dict1[3] =='X') or (dict1[4]=='X' and dict1[5] =='X' and dict1[6] =='X') or (dict1[7]=='X' and dict1[8] =='X' and dict1[9] =='X')
    cO = (dict1[1]=='O' and dict1[4]=='O' and dict1[7]=='O') or  (dict1[2]=='O' and dict1[5]=='O' and dict1[8]=='O') or (dict1[3]=='O' and dict1[6]=='O' and dict1[9]=='O')
    cX = (dict1[1]=='X' and dict1[4]=='X' and dict1[7]=='X') or  (dict1[2]=='X' and dict1[5]=='X' and dict1[8]=='X') or (dict1[3]=='X' and dict1[6]=='X' and dict1[9]=='X')
    dO = (dict1[3]=='O' and dict1[5]=='O' and dict1[7]=='O') or (dict1[1]=='O' and dict1[5]=='O' and dict1[9]=='O')
    dX = (dict1[3]=='X' and dict1[5]=='X' and dict1[7]=='X') or (dict1[1]=='X' and dict1[5]=='X' and dict1[9]=='X')
    P1_win_check = rX or cX or dX
    P2_win_check = rO or cO or dO
    if ' ' in dict1.values():
        draw_check = False
    else:
        draw_check = True
    return P1_win_check,P2_win_check,draw_check

def total_score(player_win_check):
    P1_score = 0
    P2_score = 0
    draw_score = 0
    if player_win_check[0]==True:
        P1_score=1
    elif player_win_check[1] ==True:
        P2_score=1
    elif player_win_check[2]==True:
        draw_score=1
    return P1_score,P2_score,draw_score

def playtime():
    game_no = 1
    response = input('Do you want to play again? Press Y for yes and N for no: ')
    if response.lower()=='y' or response.lower()=='yes':
        game_no = 1
        clear_output()
    elif response.lower()=='n' or response.lower()=='no':
        game_no = -10000
    else:
        print('Enter Y or N please')
        playtime()
    return game_no

def print_final_scores(results):
    clear_output()
    print('Total games - {}'.format(sum(results)))
    print('\nGames won by player 1 - {}'.format(results[0]))
    print('\nGames won by player 2 - {}'.format(results[1]))
    print('\nGames tied - {}'.format(results[2]))

def start_game():
    game_no = 1
    print("Welcome to diggee's tic tac toe\n")
    print_example_board()
    P1_score = 0
    P2_score = 0
    draw_score = 0
    win_counter = [0,0,0]
    while game_no>0:
        player_win_check = [False,False,False]
        dict1 = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        print_board(dict1)
        turn = 1
        win_check = False
        while win_check == False:
            number = int(input('enter number'))
            clear_output()
            dict1[number] = update_board(turn)
            turn+=1
            player_win_check = winner_check(dict1)
            win_check = True in player_win_check
            print_board(dict1)
            win_counter = total_score(player_win_check)
        game_no+= playtime()

        P1_score+=win_counter[0]
        P2_score+=win_counter[1]
        draw_score+=win_counter[2]

    final_scores = [P1_score,P2_score,draw_score]
    print_final_scores(final_scores)

start_game()
