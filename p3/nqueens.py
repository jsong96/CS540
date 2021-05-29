# Name: Jiwon Song
# NetID: jsong99
# course: Spring 2020 CS 540
import random
import numpy as np
import copy



def succ(state, boulderX, boulderY):
    '''
     given a state of the board, return a list of all valid successor states
    :param state: current state
    :param boulderX: x coordinate of the boulder
    :param boulderY: y coordinate of the boulder
    :return: list of successors of the current state
    '''
    n = len(state)
    # create a column-major 2d array
    chess = np.zeros(shape=(n, n))
    # mark the boulder location
    chess[boulderX][boulderY] = 1
    # list to hold successors
    succ_list = []
    # generate successors: one queen move at a time
    for i in range(n):
        for j in range(n):
            tmp = copy.copy(state)
            if chess[j][i] != 1:
                tmp[i] = j
                if state[i] != tmp[i]:
                    succ_list += [tmp]
    return succ_list


def f(state, boulderX, boulderY):
    '''
    given a state of the board, return an integer score such that the goal state is the highest score
    :param state: a state of a board
    :param boulderX: x coordinate of the boulder
    :param boulderY: y coordinate of the boulder
    :return: f (the number of queen being attacked
    '''
    # check the size of the board
    n = len(state)
    # create a 2D array
    chess = np.zeros(shape=(n, n), order='F')
    # mark the location of boulder
    chess[boulderX][boulderY] = 1
    # f() value to return
    f = 0
    # index value to iterate the state and the chess board
    i = 0
    for s in state:
        # mark the location of queens
        chess[s][i] = 2
        i += 1
    # reinitialize the index
    i = 0
    # checking process, if it encounters queen, erase it to mark it is already being attacked
    for s in state:
        attacked = False
        # if the queen is at the leftmost side of the board, check only right
        if i == 0:
            if not attacked:
                # check right
                for j in range(1, n):
                    # if it meets another queen in the same row, update f and break
                    if chess[s][i + j] == 2:
                        attacked = True
                        f += 1
                        break
                    # if it meets the boulder, do not need to check rest of the row
                    if chess[s][i + j] == 1:
                        break
            if not attacked:
                # check upper right diagonal
                for j in range(1, n):
                    if (s - j) >= 0 and (i + j) < n:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s - j][i + j] == 1:
                            break
                        if chess[s - j][i + j] == 2:
                            attacked = True
                            f += 1
                            break
            if not attacked:
                # check lower right diagonal
                for j in range(1, n):
                    if (s + j) < n and (i + j) < n:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s + j][i + j] == 1:
                            break
                        if chess[s + j][i + j] == 2:
                            attacked = True
                            f += 1
                            break
        # if the queen is at the rightmost side of the board, check only left
        elif i == (n - 1):
            if not attacked:
                # check left
                for j in range(1, n):
                    # if it meets another queen in the same row, update f and break
                    if chess[s][i - j] == 2:
                        attacked = True
                        f += 1
                        break
                    # if it meets the boulder, do not need to check rest of the row
                    if chess[s][i - j] == 1:
                        break
            if not attacked:
                # check upper left diagonal
                for j in range(1, n):
                    if (s - j) >= 0 and (i - j) >= 0:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s - j][i - j] == 1:
                            break
                        if chess[s - j][i - j] == 2:
                            attacked = True
                            f += 1
                            break
            if not attacked:
                # check lower left diagonal
                for j in range(1, n):
                    if (s + j) < n and (i - j) >= 0:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s + j][i - j] == 1:
                            break
                        if chess[s + j][i - j] == 2:
                            attacked = True
                            f += 1
                            break
        # 0 < i < n
        else:
            if not attacked:
                # check left
                for j in range(1, n):
                    if (i - j) >= 0:

                        # if it meets another queen in the same row, update f and break
                        if chess[s][i - j] == 2:
                            attacked = True
                            f += 1
                            break
                        # if it meets the boulder, do not need to check rest of the row
                        if chess[s][i - j] == 1:
                            break
            if not attacked:
                # check right
                for j in range(1, n):
                    if (i + j) < n:
                        # if it meets another queen in the same row, update f and break
                        if chess[s][i + j] == 2:
                            attacked = True
                            f += 1
                            break
                        # if it meets the boulder, do not need to check rest of the row
                        if chess[s][i + j] == 1:
                            break
            if not attacked:
                # check upper right diagonal
                for j in range(1, n):
                    if (s - j) >= 0 and (i + j) < n:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s - j][i + j] == 1:
                            break
                        if chess[s - j][i + j] == 2:
                            attacked = True
                            f += 1
                            break
            if not attacked:
                # check lower right diagonal
                for j in range(1, n):
                    if (s + j) < n and (i + j) < n:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s + j][i + j] == 1:
                            break
                        if chess[s + j][i + j] == 2:
                            attacked = True
                            f += 1
                            break
            if not attacked:
                # check upper left diagonal
                for j in range(1, n):
                    if (s - j) >= 0 and (i - j) >= 0:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s - j][i - j] == 1:
                            break
                        if chess[s - j][i - j] == 2:
                            attacked = True
                            f += 1
                            break
            if not attacked:
                # check lower left diagonal
                for j in range(1, n):
                    if (s + j) < n and (i - j) >= 0:
                        # if it meets the boulder, do not need to check rest of the diagonal
                        if chess[s + j][i - j] == 1:
                            break
                        if chess[s + j][i - j] == 2:
                            attacked = True
                            f += 1
                            break

        # update index
        i += 1
    return f


def choose_next(curr, boulderX, boulderY):
    '''
    given the current state, use succ() to generate the successors and return the selected next state
    :param curr: current state
    :param boulderX: x coordinate of boulder
    :param boulderY: y coordinate of boulder
    :return: a possible state with the lowest score, None if the selected state is same as the current state
    '''
    # create a successor list
    succ_list = succ(curr, boulderX, boulderY)
    # include current state
    succ_list += [curr]
    # temporary variable to store minimum value and state with the minimum value
    min_succ = []
    minimum = 100
    # to verify there is an unique minimum val or not
    num_min = 1
    succ_tmp = []
    # traverse the list of successors
    for successor in succ_list:
        # get the f() value for each successor
        f_val = f(successor, boulderX, boulderY)
        # update the minimum value
        if minimum > f_val:
            minimum = f_val
            min_succ = successor
    # remove the minimum value for double checking
    succ_list.remove(min_succ)
    # check if there is another minimum value
    for successor in succ_list:
        f_val = f(successor, boulderX, boulderY)
        if f_val <= minimum:
            num_min += 1
            succ_tmp += [successor]
    succ_tmp += [min_succ]
    # if there are more than one unique minimum value
    if num_min > 1:
        # sort the states
        succ_tmp = sorted(succ_tmp)
        # select the lowest state and return
        # for s in succ_tmp:
        #    print(s, f(s, boulderX, boulderY))
        # print('===============================')
        if succ_tmp[0] == curr:
            return None
        else:
            return succ_tmp[0]
    else:
        # if the state is same as the current state
        if min_succ == curr:
            # return none
            return None
        else:
            # else return the unique low state
            return min_succ


def nqueens(initial_state, boulderX, boulderY):
    '''
    run the hill-climbing algorithm from a given initial state, return the convergence state
    :param initial_state: a given initial state
    :param boulderX: x coordinate of the boulder
    :param boulderY: y coordinate of the boulder
    :return: the convergence state
    '''
    # Pick t in neighbors(s) with the largest f(t)
    # IF f(t) <= f(s) THEN stop, return s
    # s = t. GOTO 2.
    state = initial_state
    while state is not None:
        tmp = state
        state = choose_next(state, boulderX, boulderY)
        if state is None:
            return tmp
        f_val = f(state, boulderX, boulderY)
        print(state, ' - ', 'f=', f_val, sep='')


def nqueens_restart(n, k, boulderX, boulderY):
    '''
    run the hill-climbing algorithm on an n*n board with random restarts
    :param n:
    :param k: number of times to generate random initial states
    :param boulderX: x coordinate of the boulder
    :param boulderY: y coordinate of the boulder
    :return: None
    '''
    # If you find a solution before you reach k, print the solution and terminate.
    # If you reach k before finding a solution, print the best solution(s) in sorted order.
    for i in range(k):
        state = []
        for j in range(n):
            rand = random.randint(0, n-1)
            state += [rand]
        #print(state)
        if check_boulder(state, boulderX, boulderY):
            solution = nqueens(state, boulderX, boulderY)
            if f(solution, boulderX, boulderY) == 0:
                print(solution)
                return


def check_boulder(state, boulderX, boulderY):
    # check the size of the board
    n = len(state)
    # create a 2D array
    chess = np.zeros(shape=(n, n), order='F')
    # mark the location of boulder
    chess[boulderX][boulderY] = 1
    i = 0
    for s in state:
        # check if the queen is occupying the same space as the boulder
        if chess[s][i] == 1:
            # if it does, the state is invalid
            return False
        i += 1
    # if it passes, it is a valid state
    return True

