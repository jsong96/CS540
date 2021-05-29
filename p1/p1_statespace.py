####################################
# Name: Jiwon Song
# Class: Spring 2020 CS 540
# Instructor: Jerry Zhu
####################################
import copy


###
# returns a copy of state which fills the jug corresponding to the index in which (0 or 1) to its maximum capacity.
# Do not modify state
###
def fill(state, max, which):
    # make a copy of a state
    temp_state = copy.copy(state)
    # fill the right index of the state
    temp_state[which] = max[which]
    return temp_state


###
# return a copy of state which empties the jug corresponding to the index in which (0 or 1). Do not modify state.
###
def empty(state, max, which):
    # make a copy of a state
    temp_state = copy.copy(state)
    # empty the jug corresponding to the index which
    temp_state[which] = 0
    return temp_state


###
# return a copy of state which pours the contents of the jug at index source into the jug at index dest,
# until source is empty or dest is full.
# Do not modify state.
###
def xfer(state, max, source, dest):
    # make a copy of a state
    temp_state = copy.copy(state)

    # if source is not empty and destination is not full
    if not (temp_state[source] == 0) or not temp_state[dest] == max[dest]:

        # if the input or sum of input and current state exceeds the maximum level
        if temp_state[source] > max[dest] or (temp_state[source] + temp_state[dest]) > max[dest]:
            # offset to calculate remaining water in a jug
            offset = max[dest] - temp_state[dest]
            # destination state is set to max (full)
            temp_state[dest] = max[dest]
            # to prevent the water level in jug to go negative
            if (temp_state[source] - offset) < 0:
                temp_state[source] = 0
            # subtract the offset on source side
            else:
                temp_state[source] -= offset

        else:
            temp_state[dest] += temp_state[source]
            temp_state[source] = 0

    return temp_state


# display the list of unique successor states of the current state in any order.
def succ(state, max):
    # list of possible cases
    # 1 current state
    # 2 add max value to index 0
    # 3 add max value to index 1
    # 4 empty a value in index 0
    # 5 empty a value in index 1
    # 6 add value in index 0 to index 1
    # 7 add value in index 1 to index 0

    # declaring an empty list for return value
    succ_lst = []
    # make a copy of current state
    tmp_state = copy.copy(state)
    # 1 add the current state
    succ_lst += [tmp_state]

    # 2 a state with max value in index 0
    c1 = fill(tmp_state, max, 0)
    if c1 not in succ_lst:
        succ_lst += [c1]

    # 3 a state with max value in index 1
    c2 = fill(tmp_state, max, 1)
    if c2 not in succ_lst:
        succ_lst += [c2]

    # 4 a state with empty value in index 0
    c3 = [0, tmp_state[1]]
    if c3 not in succ_lst:
        succ_lst += [c3]

    # 5 a state with empty value in index 1
    c4 = [tmp_state[0], 0]
    if c4 not in succ_lst:
        succ_lst += [c4]

    # 6 add the value in index 0 to that of index 1
    c5 = xfer(tmp_state, max, 0, 1)
    if c5 not in succ_lst:
        succ_lst += [c5]

    # 7 add the value in index 1 to that of index 0
    c6 = xfer(tmp_state, max, 1, 0)
    if c6 not in succ_lst:
        succ_lst += [c6]

    # print out the elements in the list
    for s in succ_lst:
        print(s)
