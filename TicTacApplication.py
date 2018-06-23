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
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

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
    app = TicTacApplication()
    app.runApplication()