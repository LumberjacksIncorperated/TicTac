#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError 
from board import Board
import sys

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class GameCommand:
    """ A Tic Tac Toe Game Action """

    PRINT_COMMAND = 0
    MOVE_COMMAND = 1
    NOTHING_COMMAND = 2

    @preconditions( (lambda self: True),
                    (lambda commandType: (commandType == GameCommand.PRINT_COMMAND)) )
    def _create_print_command(self, commandType):
        self._commandType = commandType
    #END

    @preconditions( (lambda self: True),
                    (lambda commandType: (commandType == GameCommand.NOTHING_COMMAND)) )
    def _create_nothing_command(self, commandType):
        self._commandType = commandType
    #END

    @preconditions( (lambda self: True),
                    (lambda commandType: (commandType == GameCommand.MOVE_COMMAND)),
                    (lambda playerNumber:  playerNumber == 1 or playerNumber == 2),
                    (lambda xBoardPosition: ((isinstance(xBoardPosition, int))) and (xBoardPosition >= 0) and (xBoardPosition < Board.BOARD_SIZE)), 
                    (lambda yBoardPosition: ((isinstance(yBoardPosition, int))) and (yBoardPosition >= 0) and (yBoardPosition < Board.BOARD_SIZE)) )
    def _create_move_command(self, commandType,playerNumber, xBoardPosition, yBoardPosition):
        self._commandType = commandType
        self._playerNumber = playerNumber
        self._xBoardPosition = xBoardPosition
        self._yBoardPosition = yBoardPosition
    #END
    
    @preconditions( (lambda self: True),
                    (lambda *arguements: (len(arguements) == 1) or (len(arguements) == 4)) )
    def __init__(self, *arguements):
        '''
        DESCRIPTION:
            Constructs either a move command or an execute command

        PARAMETERS:
            arguements(0): GameCommand.PRINT_COMMAND
            or
            arguements(0): GameCommand.NOTHING_COMMAND            
            or
            arguements(0): GameCommand.PRINT_COMMAND
            arguements(1): an integer which is 1 for 'player 1' and 2 for 'player 2'
            arguements(2): a board coordinate in the x direction between 0 and 2 as an integer
            arguements(3): a board coordinate in the y direction between 0 and 2 as an integer

        RETURNS:
            (valid arguement) 
                A Game Command Object
            (invalid arguement)
                a PreconditionError is thrown
        '''
        if len(arguements) == 1 and (arguements[0] == GameCommand.PRINT_COMMAND):
            self._create_print_command(*arguements)
            return
            
        if len(arguements) == 1 and (arguements[0] == GameCommand.NOTHING_COMMAND):
            self._create_nothing_command(*arguements)
            return

        if len(arguements) == 4 and (arguements[0] == GameCommand.MOVE_COMMAND):
            self._create_move_command(*arguements)
            return

        raise PreconditionError
    #END

    def executeCommandOnBoard(self, board):
        '''
        DESCRIPTION:
            Executes the command instance on a board

        RETURNS:
            (valid arguement) 
                None
            (invalid arguement)
                a PreconditionError is thrown
        '''
        if self._commandType == GameCommand.PRINT_COMMAND:
            boardString = board.getBoardAsString()
            print(boardString)

        if self._commandType == GameCommand.MOVE_COMMAND:
            board.placePlayerMarkerOnBoardAtPosition(self._playerNumber, self._xBoardPosition, self._yBoardPosition)

        if self._commandType == GameCommand.NOTHING_COMMAND:
            pass
    #END

#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestConstructor(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _player_numbers = [1,2]

    _known_constructor_invalid_arguement_number_for_nothing_command = [(GameCommand.NOTHING_COMMAND, 1),
                                                                     (GameCommand.NOTHING_COMMAND, 1, 1),
                                                                     (GameCommand.NOTHING_COMMAND, 1, 1, 1)] 

    _known_constructor_invalid_arguement_number_for_print_command = [(GameCommand.PRINT_COMMAND, 1),
                                                                     (GameCommand.PRINT_COMMAND, 1, 1),
                                                                     (GameCommand.PRINT_COMMAND, 1, 1, 1)]
    _known_constructor_invalid_arguement_number_for_move_command =  [(GameCommand.MOVE_COMMAND),
                                                                     (GameCommand.MOVE_COMMAND, 1),
                                                                     (GameCommand.MOVE_COMMAND, 1, 1),
                                                                     (GameCommand.MOVE_COMMAND, 1, 1, 1, 1) ]
    _invalid_player_numbers = [0, 3, 4, 5, 6, 7, 8, 9]

    _invalid_board_positions = [-1, 3, 4, 5, 6, 7, 8, 9]

    _invalid_types = [1.2, "hello", (1, 2), []]

    def setUp(self):
        pass

    def tearDown(self):
    	pass
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction_for_nothing_command(self):
        printCommand = GameCommand(GameCommand.NOTHING_COMMAND)
        self.assertEqual(printCommand._commandType, GameCommand.NOTHING_COMMAND)

    def test_construction_for_print_command(self):
        printCommand = GameCommand(GameCommand.PRINT_COMMAND)
        self.assertEqual(printCommand._commandType, GameCommand.PRINT_COMMAND)

    def test_construction_for_move_command_for_correct_player_number(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in self._player_numbers:
                    moveCommand = GameCommand(GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition)
                    self.assertEqual(moveCommand._playerNumber, playerNumber)  

    def test_construction_for_move_command_for_correct_x_position(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in self._player_numbers:
                    moveCommand = GameCommand(GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition)
                    self.assertEqual( moveCommand._xBoardPosition, boardXPosition)  

    def test_construction_for_move_command_for_correct_y_position(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in self._player_numbers:
                    moveCommand = GameCommand(GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition)
                    self.assertEqual( moveCommand._yBoardPosition, boardYPosition)  

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction_for_invalid_numbers_of_arguements_for_nothing_command(self):
        for invalid_constructor_arguements in self._known_constructor_invalid_arguement_number_for_nothing_command:
            self.assertRaises(PreconditionError, GameCommand, (invalid_constructor_arguements))

    def test_construction_for_invalid_numbers_of_arguements_for_print_command(self):
        for invalid_constructor_arguements in self._known_constructor_invalid_arguement_number_for_print_command:
            self.assertRaises(PreconditionError, GameCommand, (invalid_constructor_arguements))

    def test_construction_for_invalid_numbers_of_arguements_for_move_command(self):
        for invalid_constructor_arguements in self._known_constructor_invalid_arguement_number_for_move_command:
            self.assertRaises(PreconditionError, GameCommand, (invalid_constructor_arguements))

    def test_construction_for_invalid_player_number_for_move_command(self):
        for invalid_player_number in self._invalid_player_numbers:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, invalid_player_number, 1, 1))

    def test_construction_for_invalid_x_board_position_for_move_command(self):
        for invalid_x_board_position in self._invalid_board_positions:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, 1, invalid_x_board_position, 1))

    def test_construction_for_invalid_y_board_position_for_move_command(self):
        for invalid_y_board_position in self._invalid_board_positions:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, 1, 1, invalid_y_board_position))

    def test_construction_for_invalid_player_type_for_move_command(self):
        for invalid_player_type in self._invalid_types:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, invalid_player_type, 1, 1))

    def test_construction_for_invalid_x_type_for_move_command(self):
        for invalid_x_type in self._invalid_types:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, 1, invalid_x_type, 1))

    def test_construction_for_invalid_y_type_for_move_command(self):
        for invalid_y_type in self._invalid_types:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, 1, 1, invalid_y_type))

    def test_constructor_move_command_valid_positions_with_player_number_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in range(2,100):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition) )

    def test_constructor_move_command_valid_positions_with_player_number_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in (0, -1, -2, -3, -4, -5, -6, -7):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition) )

    def test_constructor_move_command_valid_positions_with_player_number_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition) ) 

    def test_constructor_move_command_invalid_positions_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in range(3,100):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, 1, invalidPosition, boardYPosition) )
                for invalidPosition in range(3,100):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, 1, boardXPosition, invalidPosition) ) 

    def test_constructor_move_command_invalid_positions_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, 1, invalidPosition, boardYPosition) )
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, 1, boardXPosition, invalidPosition) )

    def test_constructor_move_command_invalid_positions_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):       
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, 1, invalidPosition, boardYPosition) )
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self.assertRaises( PreconditionError, GameCommand,( GameCommand.MOVE_COMMAND, 1, boardXPosition, invalidPosition) )

class TestExecuteCommandOnBoard(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _game_command = None
    _board = None

    _known_empty_board_string = "\n_______\n"+"| | | |\n"+"| | | |\n"+"| | | |\n"+"_______\n"
    _known_player1_full_board_string = "\n_______\n"+"|O|O|O|\n"+"|O|O|O|\n"+"|O|O|O|\n"+"_______\n"
    _known_player2_full_board_string = "\n_______\n"+"|X|X|X|\n"+"|X|X|X|\n"+"|X|X|X|\n"+"_______\n"
    _known_random_board_one_board_string = "\n_______\n"+"|O| |O|\n"+"| | |X|\n"+"|X| | |\n"+"_______\n"
    _known_random_board_two_board_string = "\n_______\n"+"| | | |\n"+"| |O| |\n"+"|O|X|X|\n"+"_______\n"

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None

    def __setup_random_board_two(self):
        self._board.placePlayerMarkerOnBoardAtPosition(1, 1, 1)
        self._board.placePlayerMarkerOnBoardAtPosition(1, 2, 0)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 2, 2)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 2, 1)

    def __setup_random_board_one(self):
        self._board.placePlayerMarkerOnBoardAtPosition(1, 0, 0)
        self._board.placePlayerMarkerOnBoardAtPosition(1, 0, 2)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 1, 2)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 2, 0)

    def _print_interactive_user_message_for_test_board_description_and_string(self, boardDescription, boardString):
        print(chr(27) + "[2J") # Just clears terminal screen
        print("This is the expected "+ boardDescription +":")
        print(boardString)
        print("This is the given empty board:")        

    def _request_user_confirmation(self):
        user_answer = raw_input("Enter <y> if they were or same, or <n> if they were different:\n")
        if(user_answer == 'y'):
            return
        if(user_answer == 'n'):
            raise Exception('Test Failed')
        raise Exception('Incorrect user testing arguement: Test Discounted and Failed')

    def __setup_full_board_for_player_number(self, playerNumber):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board.placePlayerMarkerOnBoardAtPosition(playerNumber, boardXPosition, boardYPosition)

    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_execute_move_command(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for playerNumber in [1, 2]:
                    moveCommand = GameCommand(GameCommand.MOVE_COMMAND, playerNumber, boardXPosition, boardYPosition)        
                    moveCommand.executeCommandOnBoard(self._board)
                    self.assertEqual(self._board.getMarkerAtBoardPosition(boardXPosition, boardYPosition), playerNumber)

    def test_empty_board_print_command(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'test_execute_print_command' is not run on this testing mode.>")
            return
        self._print_interactive_user_message_for_test_board_description_and_string("empty board", self._known_empty_board_string)
        moveCommand = GameCommand(GameCommand.PRINT_COMMAND)        
        moveCommand.executeCommandOnBoard(self._board)
        try:
            self._request_user_confirmation()
        except Exception:
            raise Exception

    def test_full_player1_board_print_command(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'test_execute_print_command' is not run on this testing mode.>")
            return
        self._print_interactive_user_message_for_test_board_description_and_string("full player 1 board", self._known_player1_full_board_string)
        self.__setup_full_board_for_player_number(1)
        moveCommand = GameCommand(GameCommand.PRINT_COMMAND)        
        moveCommand.executeCommandOnBoard(self._board)
        try:
            self._request_user_confirmation()
        except Exception:
            raise Exception

    def test_full_player2_board_print_command(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'test_execute_print_command' is not run on this testing mode.>")
            return
        self._print_interactive_user_message_for_test_board_description_and_string("full player 2 board", self._known_player2_full_board_string)
        self.__setup_full_board_for_player_number(2)
        moveCommand = GameCommand(GameCommand.PRINT_COMMAND)        
        moveCommand.executeCommandOnBoard(self._board)
        try:
            self._request_user_confirmation()
        except Exception:
            raise Exception

    def test_random_board_one_board_print_command(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'test_execute_print_command' is not run on this testing mode.>")
            return
        self._print_interactive_user_message_for_test_board_description_and_string("random board one", self._known_random_board_one_board_string)
        self.__setup_random_board_one()
        moveCommand = GameCommand(GameCommand.PRINT_COMMAND)        
        moveCommand.executeCommandOnBoard(self._board)
        try:
            self._request_user_confirmation()
        except Exception:
            raise Exception

    def test_random_board_two_board_print_command(self):
        if not (testFlag == "-interactive"):
            print("\n<Test function 'test_execute_print_command' is not run on this testing mode.>")
            return 
        self._print_interactive_user_message_for_test_board_description_and_string("random board two", self._known_random_board_two_board_string)
        self.__setup_random_board_two()
        moveCommand = GameCommand(GameCommand.PRINT_COMMAND)        
        moveCommand.executeCommandOnBoard(self._board)
        try:
            self._request_user_confirmation()
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