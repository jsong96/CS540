'''
Name: Jiwon Song
class: CS 540
File name: torus_puzzle.py
'''
import copy

''' author: hobbes
source: cs540 canvas
TODO: complete the enqueue method
'''


class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.max_len = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, state_dict):
        """ Items in the priority queue are dictionaries:
        -  'state': the current state of the puzzle
        -  'h': the heuristic value for this state
        -  'parent': a reference to the item containing the parent state
        -  'g': the number of moves to get from the initial state to this state, the "cost" of this state
         -  'f': the total estimated cost of this state, g(n)+h(n)
         For example, an item in the queue might look like this:
        {'state':[1,2,3,4,5,6,7,8,0], 'parent':[1,2,3,4,5,6,7,0,8],
        'h':0, 'g':14, 'f':14}
        Please be careful to use these keys exactly so we can test your
        queue, and so that the pop() method will work correctly.
        """

        # initialize in_open
        in_open = False
        # iterate through priority queue
        for item in self.queue:
            # if there is a state that is already present
            if state_dict['state'] == item['state']:
                # set in_open to True
                in_open = True
                if state_dict['g'] < item['g']:
                    # update the cost g
                    item['g'] = state_dict['g']
                    # update the parent
                    item['parent'] = state_dict['parent']

        if not in_open:
            self.queue.append(state_dict)
        # track the maximum queue length
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def requeue(self, from_closed):
        """ Re-queue a dictionary from the closed list (see lecture slide 21)"""
        self.queue.append(from_closed)
        # track the maximum queue length
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def pop(self):
        """ Remove and return the dictionary with the smallest f(n)=g(n)+h(n)"""
        minf = 0
        for i in range(1, len(self.queue)):
            if self.queue[i]['f'] < self.queue[minf]['f']:
                minf = i
        state = self.queue[minf]
        del self.queue[minf]
        return state


def heuristic_count(state):
    # goal state
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # heuristic value count
    h = 0
    for i in range(len(state)):
        # if the tiles are not in their goal state
        if state[i] != 0:
            if state[i] != goal[i]:
                # increase the heuristic value
                h += 1
    return h


# this function generates succ states
def generate_succ(state):
    # variable declaration for 2-D array
    blank_idx = 0
    succ_lst = []

    # create a 2-D array based on 8-puzzle format
    second_dimensional = oneD_to_twoD(state)

    # find the index of blank state
    for row in second_dimensional:
        for c in row:
            if c == 0:
                blank_idx = (second_dimensional.index(row), row.index(c))

    # row idx and col idx for testing every possible case
    x = blank_idx[0]
    y = blank_idx[1]

    # if row idx is 0
    if x == 0:
        # create a duplicate state for right shift
        right = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = right[x][y]
        # exchange values
        right[x][y] = right[x + 1][y]
        right[x + 1][y] = tmp
        succ_lst += [twoD_to_oneD(right)]

        # create a duplicate state for left shift
        left = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = left[x][y]
        # exchange values
        left[x][y] = left[x + 2][y]
        left[x + 2][y] = tmp
        succ_lst += [twoD_to_oneD(left)]

    # if row idx is 1
    elif x == 1:
        # create a duplicate state for right shift
        right = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = right[x][y]
        right[x][y] = right[x + 1][y]
        right[x + 1][y] = tmp
        succ_lst += [twoD_to_oneD(right)]

        # create a duplicate state for left shift
        left = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = left[x][y]
        # exchange values
        left[x][y] = left[x - 1][y]
        left[x - 1][y] = tmp
        succ_lst += [twoD_to_oneD(left)]

    # if row idx is 2
    else:
        # create a duplicate state for right shift
        right = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = right[x][y]
        right[x][y] = right[x - 2][y]
        right[x - 2][y] = tmp
        succ_lst += [twoD_to_oneD(right)]

        # create a duplicate state for left shift
        left = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = left[x][y]
        # exchange values
        left[x][y] = left[x - 1][y]
        left[x - 1][y] = tmp
        succ_lst += [twoD_to_oneD(left)]

    # if col idx is 0
    if y == 0:
        # create a duplicate state for top shift
        top = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = top[x][y]
        # exchange values
        top[x][y] = top[x][y + 2]
        top[x][y + 2] = tmp
        succ_lst += [twoD_to_oneD(top)]

        # create a duplicate state for down shift
        down = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = down[x][y]
        # exchange values
        down[x][y] = down[x][y + 1]
        down[x][y + 1] = tmp
        succ_lst += [twoD_to_oneD(down)]

    # if col idx is 1
    elif y == 1:
        # create a duplicate state for top shift
        top = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = top[x][y]
        # exchange values
        top[x][y] = top[x][y - 1]
        top[x][y - 1] = tmp
        succ_lst += [twoD_to_oneD(top)]

        # create a duplicate state for down shift
        down = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = down[x][y]
        # exchange values
        down[x][y] = down[x][y + 1]
        down[x][y + 1] = tmp
        succ_lst += [twoD_to_oneD(down)]

    # if col idx is 2
    else:
        # create a duplicate state for top shift
        top = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = top[x][y]
        # exchange values
        top[x][y] = top[x][y - 1]
        top[x][y - 1] = tmp
        succ_lst += [twoD_to_oneD(top)]

        # create a duplicate state for down shift
        down = copy.deepcopy(second_dimensional)
        # temporary variable to store the value at blank space
        tmp = down[x][y]
        # exchange values
        down[x][y] = down[x][y - 2]
        down[x][y - 2] = tmp
        succ_lst += [twoD_to_oneD(down)]

    return succ_lst


# this function changes oneD list to twoD list
def twoD_to_oneD(twoD):
    list = []
    for row in twoD:
        for element in row:
            list.append(element)
    return list


# this function changes twoD list to oneD list
def oneD_to_twoD(state):
    second_dimensional = []
    first_wrap = []
    for s in state:
        if state.index(s) == 2 or state.index(s) == 5 or state.index(s) == 8:
            first_wrap += [s]
            second_dimensional += [first_wrap]
            first_wrap = []
        else:
            first_wrap += [s]
    return second_dimensional


def print_succ(state):
    # generate successors
    succ_lst = generate_succ(state)
    # sort the list
    succ_lst = sorted(succ_lst)
    # print out successors with heuristic values
    for state in succ_lst:
        print(state, ' ', "h=", heuristic_count(state), sep='')


def solve(state):
    # closed state list
    closed = []
    # open a priority queue
    opened = PriorityQueue()
    # g = 0
    g = 0
    # initialize the starting node
    start = {'state': state, 'h': heuristic_count(state), 'g': g, 'parent': None, 'f': g + heuristic_count(state)}
    # put the start node in the pq
    opened.enqueue(start)
    # if pq is empty, exit
    while not opened.is_empty():
        # pop one with minimum f(n)
        n = opened.pop()
        # place it on closed
        closed += [n]
        # if n is the goal state, stop
        if n['h'] == 0:
            parent = successor['parent']
            path = []
            path += [{'state': successor['state'], 'h': successor['h'], 'g': successor['g']}]
            while parent is not None:
                path += [{'state': parent['state'], 'h': parent['h'], 'g': parent['g']}]
                parent = parent['parent']
            path = reversed(path)
            for p in path:
                # print(p)
                print(p['state'], 'h=', p['h'], 'moves: ', p['g'], sep='')

            #print('Max queue length:', opened.max_len)
            return
        # expand n, generates all of its successors
        succ_lst = generate_succ(n['state'])
        # for each successor in the list
        for s in succ_lst:
            # calculate h(n')
            h = heuristic_count(s)
            # update the cost
            g = n['g'] + 1
            # form a dict with one of successors
            successor = {"state": s, "h": h, 'g': n['g'] + 1, "parent": n, 'f': g + h}
            # if successor is the goal, stop search
            if h == 0:
                parent = successor['parent']
                path = []
                path += [{'state': successor['state'], 'h': successor['h'], 'g': successor['g']}]
                while parent is not None:
                    path += [{'state': parent['state'], 'h': parent['h'], 'g': parent['g']}]
                    parent = parent['parent']
                path = reversed(path)
                for p in path:
                    print(p['state'],' ','h=', p['h'],' ', 'moves: ', p['g'], sep='')

                #print('Max queue length:', opened.max_len)
                return

            # check closed list
            for node in closed:
                # if n exists in closed list
                if node['state'] == successor['state']:
                    # if g(n') is lower for the new version of n'
                    if node['g'] > successor['g']:
                        # redirect pointers backward from n'
                        opened.enqueue(node)
                        # if not, do nothing

            # put successor in open
            opened.enqueue(successor)
    # if fail, terminate by printing max length of queue
    print('Max queue length:', opened.max_len)
