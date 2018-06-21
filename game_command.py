#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError 
from board import Board

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class GameCommand:
    """ A Tic Tac Toe Game Action """

    PRINT_COMMAND = 0
    MOVE_COMMAND = 1

    @preconditions( (lambda self: True),
                    (lambda commandType: (commandType == GameCommand.PRINT_COMMAND)) )
    def _create_print_command(self, commandType):
        self._commandType = commandType


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
    
    @preconditions( (lambda self: True),
                    (lambda *arguements: (len(arguements) == 1) or (len(arguements) == 4)) )
    def __init__(self, *arguements):
        '''
        DESCRIPTION:
            Places a token at a given board position for a given player

        PARAMETERS:
            playerNumber: an integer which is 1 for 'player 1' and 2 for 'player 2'
            boardXPosition: a board coordinate in the x direction between 0 and 2 as an integer
            boardYPosition: a board coordinate in the y direction between 0 and 2 as an integer

        RETURNS:
            (valid arguement) 
                None
            (invalid arguement)
                a PreconditionError is thrown
        '''
        if len(arguements) == 1:
            self._create_print_command(*arguements)
        if len(arguements) == 4:
            self._create_move_command(*arguements)

    def executeCommandOnBoard(self, board):
        '''
        DESCRIPTION:
            Places a token at a given board position for a given player

        PARAMETERS:
            playerNumber: an integer which is 1 for 'player 1' and 2 for 'player 2'
            boardXPosition: a board coordinate in the x direction between 0 and 2 as an integer
            boardYPosition: a board coordinate in the y direction between 0 and 2 as an integer

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

#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestConstructor(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _player_numbers = [1,2]
    _known_constructor_invalid_arguement_number_for_print_command = [(GameCommand.PRINT_COMMAND, 1),
                                                                     (GameCommand.PRINT_COMMAND, 1, 1),
                                                                     (GameCommand.PRINT_COMMAND, 1, 1, 1)]
    _known_constructor_invalid_arguement_number_for_move_command =  [(GameCommand.MOVE_COMMAND),
                                                                     (GameCommand.MOVE_COMMAND, 1),
                                                                     (GameCommand.MOVE_COMMAND, 1, 1),
                                                                     (GameCommand.MOVE_COMMAND, 1, 1, 1, 1) ]
    _invalid_player_numbers = [0, 3, 4, 5, 6, 7, 8, 9]

    _invalid_board_positions = [-1, 3, 4, 5, 6, 7, 8, 9]

    def setUp(self):
        pass

    def tearDown(self):
    	pass
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
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
    def test_construction_for_invalid_numbers_of_arguements_for_print_command(self):
        for invalid_constructor_arguements in self._known_constructor_invalid_arguement_number_for_print_command:
            self.assertRaises(PreconditionError, GameCommand, (invalid_constructor_arguements))

    def test_construction_for_invalid_numbers_of_arguements_for_move_command(self):
        for invalid_constructor_arguements in self._known_constructor_invalid_arguement_number_for_move_command:
            self.assertRaises(PreconditionError, GameCommand, (invalid_constructor_arguements))

    def test_construction_for_invalid_player_number_for_move_command(self):
        for player_number in self._invalid_player_numbers:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, player_number, 1, 1))

    def test_construction_for_invalid_x_board_position_for_move_command(self):
        for invalid_x_board_position in self._invalid_board_positions:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, 1, invalid_x_board_position, 1))

    def test_construction_for_invalid_y_board_position_for_move_command(self):
        for invalid_y_board_position in self._invalid_board_positions:
            self.assertRaises(PreconditionError, GameCommand, (GameCommand.MOVE_COMMAND, 1, 1, invalid_y_board_position))
"""
class TestExecuteCommandOnBoard(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_column_create_of_correct_length(self):
        createdColumn = self._board._create_column_of_empty_value()
        self.assertEqual( len(createdColumn), 3) 

    def test_column_create_of_correct_entries(self):
        createdColumn = self._board._create_column_of_empty_value()
        for columnIndex in range(Board.BOARD_SIZE):
            self.assertEqual( createdColumn[columnIndex], Board.EMPTY_VALUE) 

class TestPlacePlayerMarkerOnBoardAtPosition(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_board_intially_empty_marked(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self.assertEqual( self._board._boardGrid[boardXPosition][boardYPosition], Board.EMPTY_VALUE)  

    def test_marking_random_position_player1(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board = Board()
                self._board.placePlayerMarkerOnBoardAtPosition(1, boardXPosition, boardYPosition)
                self.assertTrue( self._board._boardGrid[boardXPosition][boardYPosition], Board.PLAYER_TOKEN_VALUE[1 - 1] )
                self._board = None

    def test_marking_random_position_player2(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board = Board()
                self._board.placePlayerMarkerOnBoardAtPosition(2, boardXPosition, boardYPosition)
                self.assertTrue( self._board._boardGrid[boardXPosition][boardYPosition], Board.PLAYER_TOKEN_VALUE[2 - 1] )
                self._board = None

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_marking_valid_positions_with_player_number_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for player in range(2,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (player, boardXPosition, boardYPosition) )
                    self._board = None 

    def test_marking_valid_positions_with_player_number_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for player in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (player, boardXPosition, boardYPosition) )
                    self._board = None 

    def test_marking_valid_positions_with_player_number_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for player in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (player, boardXPosition, boardYPosition) )
                    self._board = None 

    def test_marking_invalid_positions_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (1, invalidPosition, boardYPosition) )
                    self._board = None 
                for player in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (1, boardXPosition, invalidPosition) )
                    self._board = None 

    def test_marking_invalid_positions_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (1, invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (1, invalidPosition, boardYPosition) )
                    self._board = None 

    def test_marking_invalid_positions_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (1, invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.placePlayerMarkerOnBoardAtPosition, (1, invalidPosition, boardYPosition) )
                    self._board = None 

class TestGetMarkerOnBoardAtPosition(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
        self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_board_intially_empty_marked(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self.assertEqual( self._board.getMarkerAtBoardPosition(boardXPosition,boardYPosition), Board.EMPTY_VALUE)  

    def test_marking_random_position_player1(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board = Board()
                self._board._boardGrid[boardXPosition][boardYPosition] = Board.PLAYER_TOKEN_VALUE[0]
                self.assertTrue( self._board.getMarkerAtBoardPosition(boardXPosition,boardYPosition), Board.PLAYER_TOKEN_VALUE[1 - 1] )
                self._board = None


    def test_marking_random_position_player2(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board = Board()
                self._board._boardGrid[boardXPosition][boardYPosition] = Board.PLAYER_TOKEN_VALUE[1]
                self.assertTrue( self._board.getMarkerAtBoardPosition(boardXPosition,boardYPosition), Board.PLAYER_TOKEN_VALUE[2 - 1] )
                self._board = None

    #------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_marking_invalid_positions_too_high(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None 
                for player in range(3,100):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (boardXPosition, invalidPosition) )
                    self._board = None 

    def test_marking_invalid_positions_too_low(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0, -1, -2, -3, -4, -5, -6, -7):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None 

    def test_marking_invalid_positions_invalid_type(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None
                for invalidPosition in (0.0, -1.134234, "asd", [1, 2], (1, 2)):
                    self._board = Board()
                    self.assertRaises( PreconditionError, self._board.getMarkerAtBoardPosition, (invalidPosition, boardYPosition) )
                    self._board = None 

class TestGetBoardString(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
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
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_empty_board_string(self):
        boardString = self._board.getBoardAsString()
        self.assertEqual(boardString, self._known_empty_board_string)

    def test_full_player1_board_string(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board.placePlayerMarkerOnBoardAtPosition(1, boardXPosition, boardYPosition)
        boardString = self._board.getBoardAsString()
        self.assertEqual(boardString, self._known_player1_full_board_string)

    def test_full_player2_board_string(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self._board.placePlayerMarkerOnBoardAtPosition(2, boardXPosition, boardYPosition)
        boardString = self._board.getBoardAsString()
        self.assertEqual(boardString, self._known_player2_full_board_string)

    def test_random_board_one_board_string(self):
        self._board.placePlayerMarkerOnBoardAtPosition(1, 0, 0)
        self._board.placePlayerMarkerOnBoardAtPosition(1, 0, 2)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 1, 2)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 2, 0)
        boardString = self._board.getBoardAsString()
        self.assertEqual(boardString, self._known_random_board_one_board_string)

    def test_random_board_two_board_string(self):
        self._board.placePlayerMarkerOnBoardAtPosition(1, 1, 1)
        self._board.placePlayerMarkerOnBoardAtPosition(1, 2, 0)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 2, 2)
        self._board.placePlayerMarkerOnBoardAtPosition(2, 2, 1)
        boardString = self._board.getBoardAsString()
        self.assertEqual(boardString, self._known_random_board_two_board_string)
"""
#------------------------------------------------------------------------------------------------------
# TESTING DRIVER
#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()