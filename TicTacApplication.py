#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError
import sys
from board import Board
from game_command import GameCommand
from panel import Panel

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TicTacApplication:
    """ A Tic Tac Toe Game """

    def __init__(self):
        self._panel = Panel()
        self._board = Board()
    #END


    def _runGameLoop(self):
        currentUserCommand = self._panel.getCommandFromUser()
        currentUserCommand.executeCommandOnBoard(self._board)
        currentUserCommand = GameCommand(GameCommand.PRINT_COMMAND)
        currentUserCommand.executeCommandOnBoard(self._board)
    #END

    def runApplication(self):
        while(True):
            self._runGameLoop()
    #END

#------------------------------------------------------------------------------------------------------
# Application Main
#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    # Check corret length of command line arguement string
    if not (len(sys.argv) == 2):
        print "Test Bench: Not Correct Number Testing Arguements\n"
        sys.exit(0)

    # Check valid command line arguements entered
    if ((not (sys.argv[1] == '-interactive')) and (not (sys.argv[1] == '-compilation')) and (not (sys.argv[1] == '-run')) ):
        print "Test Bench: Not Correct Testing Arguements\n"
        sys.exit(0)

    # Set the testing flag for the testing level for the module
    testFlag = ((sys.argv[1]) + '.')[:-1]
    del sys.argv[1]

    if(testFlag == '-run'):
        app = TicTacApplication()
        app.runApplication()