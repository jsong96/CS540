'''
    Name: Jiwon Song
    Student ID: 9074018707
    NetID: jsong99
    Class: Spring 2020 CS540
    Project: p4
    Filename: envelope_sim.py
'''

import numpy


def pick_envelope(switch, verbose):
    '''
    This function expects two boolean parameter and returns True or False based on whether you selected the correct
    envelope
    :param switch: a boolean parameter that decides whether this function switch envelopes or not
    :param verbose: whether the user wants to see the printed explanation of the simulation
    :return: True or False
    '''
    envelope_one = []
    envelope_two = []

    red = 'r'
    black = 'b'
    red_black = [1, 2]
    ball_pool = []

    # randomly distribute the three black/one red balls into two envelopes
    for i in range(4):
        rate = numpy.random.choice(red_black, p=[0.25, 0.75])
        if rate == 2:
            if red not in ball_pool:
                ball_pool += [red]
            else:
                ball_pool += [black]
        else:
            if len(ball_pool) == 3 and red not in ball_pool:
                ball_pool += red
            else:
                ball_pool += [black]

    for b in ball_pool:
        if len(envelope_one) < 2:
            envelope_one += [b]
        else:
            envelope_two += [b]
    # randomly pick one envelope pr[1/2]
    pick = numpy.random.choice([0, 1], p=[0.5, 0.5])
    # randomly pick one ball from the envelope pr[1/2]
    ball_pick = numpy.random.choice([0, 1], p=[0.5, 0.5])
    pick_tmp = ball_pick
    success = False
    # 0 == envelope_one, 1 == envelope_two
    if pick == 0:
        # check the first pick
        if envelope_one[ball_pick] == 'r':
            success = True
        else:
            # if its black, switch or don't switch according to the value of the argument
            if switch:
                # if switch, check if there is red in the other envelope
                if red in envelope_two:
                    success = True
            # if don't switch, select the remaining ball
            else:
                if ball_pick == 0:
                    if envelope_one[1] == 'r':
                        success = True
                else:
                    if envelope_one[0] == 'r':
                        success = True
    # for envelope_two
    else:
        # check whether the first pick is red
        if envelope_two[ball_pick] == 'r':
            success = True
        else:
            # if switch, randomly select a ball from switched envelope
            if switch:
                if red in envelope_one:
                    success = True
            # if don't switch, select the remaining ball
            else:
                if ball_pick == 0:
                    if envelope_two[1] == 'r':
                        success = True
                else:
                    if envelope_two[0] == 'r':
                        success = True
    # if verbose parameter is set to True, printout
    if verbose:
        # printout envelope elements
        print('Envelope 0: ', envelope_one[0], envelope_one[1])
        print('Envelope 1: ', envelope_two[0], envelope_two[1])
        # show the user's random pick
        if pick == 0:
            print('I picked envelope 0')
        else:
            print('I picked envelope 1')
        # show which one the user picked
        s = 'and drew {} {}'
        if pick == 0:
            if pick_tmp == 0 and envelope_one[0] == 'r':
                print(s.format('r','b'))
            elif pick_tmp == 1 and envelope_one[1] == 'r':
                print(s.format('a', 'r'))
            else:
                print(s.format('a', 'b'))
        else:
            if pick_tmp == 0 and envelope_two[0] == 'r':
                print(s.format('r', 'b'))
            elif pick_tmp == 1 and envelope_two[1] == 'r':
                print(s.format('a', 'r'))
            else:
                print(s.format('a', 'b'))

        if switch:
            if pick == 0:
                print('Switch to envelope 1')
            else:
                print('Switch to envelope 0')

        return success
    # else just return True or False
    else:

        return success


def run_simulation(n):
    '''
    This function runs n simulations of envelope picking under both strategies and prints the percent of times the
    correct envelopes was chosen for each
    :param n: the number of times it will run pick_envelope()
    :return: None
    '''
    switch_count = 0
    count = 0
    for i in range(n):
        if pick_envelope(False, False):
            count += 1

        if pick_envelope(True, False):
            switch_count += 1

    switch_percent = switch_count / n * 100
    no_switch_percent = count / n * 100
    print('After', n, 'simulations: ')
    success = '\tSwitch successful: {0:.2f}%'
    s_success = '\tNo-switch successful: {0:.2f}%'
    print(success.format(switch_percent))
    print(s_success.format(no_switch_percent))
