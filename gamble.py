#!/usr/bin/env python

"""
Author: John D. Anderson
Email: jander43@vols.utk.edu
Description: Gambler's Ruin simulator for command line
References: https://en.wikipedia.org/wiki/Gambler%27s_ruin
Usage:
    gamble [-mi] [<games> <sets>]
"""

# libs
import sys
import random
import readline
import termcolor
import numpy


# funcs
def print_matrix(matrix):
    """Print out numpy matrix."""
    print ''
    print matrix
    print ''


def ctxt(txt, color='yellow'):
    """Print out colored text to stdout."""
    return termcolor.colored(txt, color)


def warn(txt, exit=True):
    """Print exit message and exit."""
    if exit:
        sys.exit(ctxt(txt, color='red'))
    else:
        print ctxt(txt, color='red')


# classes
class GamblersRuin(object):
    """A class with various methods for simulating Gambler's Ruin."""
    def __init__(self, clargs):
        # startup readline
        readline.parse_and_bind("tab: complete")

        # store clargs
        self.clargs = clargs

        # get user prompt
        self.prompt = '> '

        # get totals
        self.record = {'wins': 0, 'losses': 0}

        # command dictionary
        self.commands = {'run': self.run,
                         'total': self.total,
                         'matrix': self.matrix,
                         'help': self.print_help
                         }

    @staticmethod
    def simulate(params):
        """Run simulation."""
        # init heads and tails counters
        wins = 0
        losses = 0

        # get matrix size
        params['total'] = params['games'] * params['sets']

        # create numpy array
        outcome = numpy.zeros((params['sets'], params['games']))

        # start simulation
        for i in range(params['sets']):
            # init count and outcome
            count = 0
            for j in range(params['games']):
                rand = random.randint(1, 2)
                # Checks if head or tail #
                if rand == 1:
                    wins += 1
                    outcome[i][j] = 1
                else:
                    losses += 1
                count += 1

        # result
        if params['matrix']:
            print_matrix(outcome)

        # Basic formula for calculating percentage #
        percentage = (float(wins) / params['total']) * 100

        # Print statements #
        print ctxt("Wins = " + str(wins))
        print ctxt("Losses = " + str(losses))
        print ctxt("Percentage Wins = " + str(percentage) + "%")
        print ctxt("Percentage Edge = " + str(percentage - 50.00) + "%\n")

        # return wins/losses
        return {'1': wins, '0': losses}

    def interpreter(self):
        """Starts interactive session to store state of games."""
        while True:
            try:
                cmd = raw_input(self.prompt)
                self.execute_cmd(cmd)
            except EOFError:
                warn('\nClosing interactive session')
            except KeyboardInterrupt:
                print ''

    def parse_cmd(self, cmd):
        """Parse commands for interactive mode."""
        # first split
        return cmd.split()

    def execute_cmd(self, command):
        """Execute commands passed in interactive mode."""
        # first parse
        cmd_list = self.parse_cmd(command)

        # now execute
        try:
            self.commands[cmd_list[0]](cmd_list)
        except KeyError:
            warn('Unknown command {0}'.format(cmd_list[0]), exit=False)

    def matrix(self, args):
        """Just flip -m flag."""
        self.clargs['-m'] = not self.clargs['-m']

    def print_help(self, args):
        """Prints help message."""
        help_msg = ('run [<games> <sets>] Runs the simulation with inputs\n'
                    'matrix               Turns off/on matrix printing\n'
                    'total                Prints running total\n'
                    'help                 Prints this help message\n')

        # print help
        print ctxt(help_msg, color='red')

    def total(self, args):
        """Calculates and prints running total."""
        # calculate totals
        wins = self.record['wins']
        losses = self.record['losses']
        percent_wins = (float(wins) / (wins + losses)) * 100
        edge = percent_wins - 50.00

        # get format string
        total_string = (
            'Total Wins = {0}\n'
            'Total Losses = {1}\n'
            'Total Percentage Wins = {2}%\n'
            'Total Percentage Edge = {3}%\n'
        ).format(wins, losses, percent_wins, edge)

        # print totals
        print ctxt(total_string)

    def run(self, cmd_list):
        """Runs the simulation."""
        # get parameters
        try:
            params = {'games': int(cmd_list[1]), 'sets': int(cmd_list[2]),
                      'matrix': self.clargs['-m']}
            # now update clargs
            self.clargs['<games>'] = params['games']
            self.clargs['<sets>'] = params['sets']

        except IndexError:
            if self.clargs['<games>'] and self.clargs['<sets>']:
                params = {'games': int(self.clargs['<games>']),
                          'sets': int(self.clargs['<sets>']),
                          'matrix': self.clargs['-m']}
            else:
                print 'Usage Error: Type \'help\' for more details'
                return

        # execute simulation
        results = self.simulate(params)

        # update total
        self.record['wins'] += results['1']
        self.record['losses'] += results['0']


# executable only
if __name__ == '__main__':

    # libs
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # check interactive
    if args['-i']:
        # we need to store state
        game = GamblersRuin(args)

        # start interactive
        game.interpreter()

    else:
        # parameters
        params = {'games': int(args['<games>']), 'sets': int(args['<sets>']),
                  'matrix': args['-m']}
        # run
        GamblersRuin.simulate(params)
