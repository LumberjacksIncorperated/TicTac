#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError 
from game_command import GameCommand
import sys

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class Panel:
    """ User Panel For Tic Tac To """

    def __init__(self):
        pass
    #END

    def getCommandFromUser(self):
        '''
        DESCRIPTION:
            Gets A Tic Tac Toe Move Command From User

        RETURNS:
            (valid arguement) 
                A Game Command Object
            (invalid arguement)
                a PreconditionError is thrown
        '''
        print("Please Follow Instructions.")
        playerNumber = int(raw_input("First, enter player number: "))
        xBoardPosition = int(raw_input("Next, enter x-axis board position (0 -> 2): "))
        yBoardPosition = int(raw_input("Next, enter y-axis board position (0 -> 2): "))
        userCommand = GameCommand(GameCommand.MOVE_COMMAND, playerNumber, xBoardPosition, yBoardPosition)
        return userCommand
    #END

#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestGetCommandFromUser(unittest.TestCase):

    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    def setUp(self):
        self._panel = Panel()

    def tearDown(self):
        self._panel = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def _print_interactive_user_message(self, playerNumber, xBoardPosition, yBoardPosition):
        print(chr(27) + "[2J") # Just clears terminal screen
        print("Follow the prompts to create a command with:")
        print("Player Number = {}".format(playerNumber))
        print("x Board Position  = {}".format(xBoardPosition))
        print("y Board Position  = {}".format(yBoardPosition))       

    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def _test_get_user_command_for_player_number(self, playerNumber, xBoardPosition, yBoardPosition):
        self._print_interactive_user_message(playerNumber, xBoardPosition, yBoardPosition)
        userCommand = self._panel.getCommandFromUser()
        self.assertEqual(userCommand._playerNumber, playerNumber)

    def _test_get_user_command_for_x_position(self, playerNumber, xBoardPosition, yBoardPosition):
        self._print_interactive_user_message(playerNumber, xBoardPosition, yBoardPosition)
        userCommand = self._panel.getCommandFromUser()
        self.assertEqual(userCommand._xBoardPosition, xBoardPosition)

    def _test_get_user_command_for_y_position(self, playerNumber, xBoardPosition, yBoardPosition):
        self._print_interactive_user_message(playerNumber, xBoardPosition, yBoardPosition)
        userCommand = self._panel.getCommandFromUser()
        self.assertEqual(userCommand._yBoardPosition, yBoardPosition)

    def test_get_user_command_player_number(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'ttest_get_user_command' is not run on this testing mode.>")
            return

        for boardXPosition in [0,1,2]:
            for boardYPosition in [0,1,2]:
                for playerNumber in [1,2]:
                    try:
                        self._test_get_user_command_for_player_number(playerNumber, boardXPosition, boardYPosition)
                    except Exception:
                        raise Exception

    def test_get_user_command_x_position(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'ttest_get_user_command' is not run on this testing mode.>")
            return

        for boardXPosition in [0,1,2]:
            for boardYPosition in [0,1,2]:
                for playerNumber in [1,2]:
                    try:
                        self._test_get_user_command_for_x_position(playerNumber, boardXPosition, boardYPosition)
                    except Exception:
                        raise Exception

    def test_get_user_command_y_position(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'ttest_get_user_command' is not run on this testing mode.>")
            return

        for boardXPosition in [0,1,2]:
            for boardYPosition in [0,1,2]:
                for playerNumber in [1,2]:
                    try:
                        self._test_get_user_command_for_y_position(playerNumber, boardXPosition, boardYPosition)
                    except Exception:
                        raise Exception

#------------------------------------------------------------------------------------------------------
# TESTING DRIVER
#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    # Check corret length of command line arguement string
    if not (len(sys.argv) == 2):
        print "Test Bench: Not Correct Number Testing Arguements\n"
        sys.exit(0)

    # Check valid command line arguements entered
    if ((not (sys.argv[1] == '-interactive')) and (not (sys.argv[1] == '-compilation'))):
        print "Test Bench: Not Correct Testing Arguements\n"
        sys.exit(0)

    # Set the testing flag for the testing level for the module
    testFlag = ((sys.argv[1]) + '.')[:-1]
    del sys.argv[1]

    # Run test harness
    unittest.main()

#END
        