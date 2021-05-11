import re


def init_game():
    return [[0,0,0],[0,0,0],[0,0,0]]


def check_win(ttt):
    wincases = ('hor', 'ver', 'ltr', 'rtl')
    win = {}
    dimsize = 3
    diff = -dimsize+1
    winner = 0
    availsq = dimsize ** 2
    for i in wincases:
        win[i] = 0
    for i in range(0, dimsize):
        for j in range(0, dimsize):
            win['hor'] = ttt[i][j] if ttt[i][j] == win['hor'] or j == 0 else 0
            win['ver'] = ttt[j][i] if ttt[j][i] == win['ver'] or j == 0 else 0
            if i==j:
                win['ltr'] = ttt[i][j] if ttt[i][j] == win['ltr'] or i == 0 else 0
            if i - j == diff:
                win['rtl'] = ttt[i][j] if ttt[i][j] == win['rtl'] or i == 0 else 0
            if ttt[j][i] > 0:
                availsq -= 1
        diff += 2
        if i < dimsize - 1:
            validcases = ('hor', 'ver')
        else:
            validcases = wincases
        for j in validcases:
            winner = win[j] if winner == 0 else 0
            if winner > 0:
                return winner
    winner = -availsq
    return winner


def show_game(ttt):
    dimen = 3
    print('  | 0 | 1 | 2 |')
    print('  |-----------|')
    for i in range(0, dimen):
        line = '%s |' % i
        for j in range(0, dimen):
            line += ' %s |' % ttt[i][j]
        print(line)
        if i < dimen - 1:
            print('  |---+---+---|')
        else:
            print('  |-----------|')
    return 0


def user_input(ttt, user):
    x = ''
    while len(x) == 0:
        print('Enter your pos (x,y):')
        x = input()
        if re.search('^[0-2],[0-2]$', x):
            if ttt[int(x[0])][int(x[2])] == 0:
                ttt[int(x[0])][int(x[2])] = user
                winner = check_win(ttt)
                show_game(ttt)
                if winner > 0:
                    print('Winner is player %s' % winner)
                    return True
                elif winner < 0:
                    return False
                else:
                    print('It is a draw game.')
                    return True
            else:
                print('It is not spare.')
                x = ''
        else:
            x = ''


def tic_tac_toe():
    finish = False
    ttt = init_game()
    print('Initialise a new game.')
    show_game(ttt)
    while not(finish):
        for i in range(1,3):
            print('Player %s...' % i)
            finish = user_input(ttt, i)
            if finish:
                break
    print('End game.')        


def __main__():
    tic_tac_toe()


__main__()
