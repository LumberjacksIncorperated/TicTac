#------------------------------------------------------------------------------------------------------
# IMPORTS
#------------------------------------------------------------------------------------------------------
import unittest
from conditions import preconditions, PreconditionError
import sys

#------------------------------------------------------------------------------------------------------
# TEST FLAG
#------------------------------------------------------------------------------------------------------
testFlag = None

#------------------------------------------------------------------------------------------------------
# IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class Board:
    """ A Tic Tac Toe Board """

    BOARD_SIZE = 3
    EMPTY_VALUE = 0
    PLAYER_TOKEN_VALUE = [1, 2]
    PLAYER_ONE_SYMBOL = "O"
    PLAYER_TWO_SYMBOL = "X"

    def _create_column_of_empty_value(self):
        column = []
        numberColumnEntriesFilled = 0
        while (numberColumnEntriesFilled < Board.BOARD_SIZE):
                column += [Board.EMPTY_VALUE]
                numberColumnEntriesFilled +=1
        return column
    #END

    def __init__(self):
        self._boardGrid = []
        numberOfBoardRowsCreated = 0
        while (numberOfBoardRowsCreated < Board.BOARD_SIZE):
            newColumn = self._create_column_of_empty_value()
            numberOfBoardRowsCreated +=1
            self._boardGrid += [newColumn]
    #END

    @preconditions( (lambda self: True),
                    (lambda playerNumber: ((isinstance(playerNumber, int))) and ((playerNumber == 1) or (playerNumber == 2))),
                    (lambda boardXPosition: ((isinstance(boardXPosition, int))) and (boardXPosition >= 0) and (boardXPosition < Board.BOARD_SIZE)), 
                    (lambda boardYPosition: ((isinstance(boardYPosition, int))) and (boardYPosition >= 0) and (boardYPosition < Board.BOARD_SIZE)) ) 
    def placePlayerMarkerOnBoardAtPosition(self, playerNumber, boardXPosition, boardYPosition):
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
        self._boardGrid[boardXPosition][boardYPosition] = Board.PLAYER_TOKEN_VALUE[playerNumber - 1]
    #END

    @preconditions( (lambda self: True),
                    (lambda boardXPosition: ((isinstance(boardXPosition, int))) and (boardXPosition >= 0) and (boardXPosition < Board.BOARD_SIZE)), 
                    (lambda boardYPosition: ((isinstance(boardYPosition, int))) and (boardYPosition >= 0) and (boardYPosition < Board.BOARD_SIZE)) ) 
    def getMarkerAtBoardPosition(self, boardXPosition, boardYPosition):
        '''
        DESCRIPTION:
            Retrieves the token value at a given board position

        PARAMETERS:
            boardXPosition: a board coordinate in the x direction between 0 and 2 as an integer
            boardYPosition: a board coordinate in the y direction between 0 and 2 as an integer

        RETURNS:
            (valid arguement) 
                Integer: Representing the token value, which is an integer defined as Board.EMPTY_VALUE, or
                         board.PLAYER_TOKEN_VALUE[0], or board.PLAYER_TOKEN_VALUE[1]
            (invalid arguement)
                a PreconditionError is thrown
        '''
        markerValue = self._boardGrid[boardXPosition][boardYPosition]
        return markerValue
    #END

    def getBoardAsString(self):
        '''
        DESCRIPTION:
             Retrieves the current board state as a printable string representation

        PARAMETERS:

        RETURNS:
            (valid arguement) 
                A string which represents the current board state
            (invalid arguement)
                a PreconditionError is thrown
        '''
        boardString = "\n_______\n"
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                if self._boardGrid[boardXPosition][boardYPosition] == Board.EMPTY_VALUE:
                    boardString += "| "
                if self._boardGrid[boardXPosition][boardYPosition] == Board.PLAYER_TOKEN_VALUE[0]:
                    boardString += "|"+Board.PLAYER_ONE_SYMBOL
                if self._boardGrid[boardXPosition][boardYPosition] == Board.PLAYER_TOKEN_VALUE[1]:
                    boardString += "|"+Board.PLAYER_TWO_SYMBOL   

            boardString += "|\n"
        boardString += "_______\n"
        return boardString
    #END
#------------------------------------------------------------------------------------------------------
# TESTING IMPLEMENTATION
#------------------------------------------------------------------------------------------------------
class TestConstructor(unittest.TestCase):
 
    #------------------------------------------------------------------------------------------------------
    # TESTING SUPPORT CODE
    #------------------------------------------------------------------------------------------------------
    _known_initial_board_value = [[0,0,0],[0,0,0],[0,0,0]]
    _board = None

    def setUp(self):
        self._board = Board()

    def tearDown(self):
    	self._board = None
 
    #------------------------------------------------------------------------------------------------------
    # POSITIVE TESTING
    #------------------------------------------------------------------------------------------------------
    def test_construction(self):
        for boardXPosition in range(Board.BOARD_SIZE):
            for boardYPosition in range(Board.BOARD_SIZE):
                self.assertEqual( self._board._boardGrid[boardXPosition][boardYPosition], 
                                  self._known_initial_board_value[boardXPosition][boardYPosition])  

class TestCreateColumnWithEmptyMarking(unittest.TestCase):
 
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
                for invalidPosition in range(3,100):
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

    # Add verbose output for compilation testing
    if testFlag == "-compilation":
        sys.argv[1] = "-v"
    else:
        del sys.argv[1]
    
    # Run test harness
    unittest.main()

#END