"""Script for a Tik Tak Toe game"""

class GameState:
    """
    A class to hold track of the current state of the game
    
    ...
    Attributes
    ----------
    players : typle
        name of player1 and name of player2
    pos : list
        list of the current fillage of the board positions
    turn : pair
        the name of the player who's on turn and its mark

    Methods
    -------
    set_pos(pos):
        takes a position (int) and updates the pos attribute.

    next_turn():
        overwrites the turn attribute to contain the other of the two players.

    next_game():
        overwrites the turn attribute to contain the other of the two players.
    """
    def __init__(self, players):
        """
        Constructs attributes to keep track of the created game.

        Parameters
        ----------
        players : tuple pair
            tuple pair consiting of a name for player1 and a name for player2
        """
        self.players = ([players[0],'X'],[players[1],'O'])
        self.pos = ['none',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.turn = self.players[0]

    def set_pos(self, pos):
        """
        takes a position (int) and updates the pos attribute.
        
        parameters
        ----------
        pos : int
            interger 1 to 9 to represent a position on the board
        """
        self.pos[pos] = self.turn[1]

    def next_turn(self):
        """overwrites the turn attribute to contain the other of the two players."""
        if self.turn == self.players[0]:
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]

    def next_game(self):
        """
        sets the class attributes ready for a new round.
        
        overwrites the pos attribute back to its initial state. 
        switches the players marks.
        overwrites the turn attribute with the player who has the X mark
        """
        self.pos = ['none',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        mark1 = self.players[0][1]
        mark2 = self.players[1][1]
        self.players[1][1] = mark1
        self.players[0][1] = mark2
        if self.players[0][1] == 'X':
            self.turn = self.players[0]
        else:
            self.turn = self.players[1]

def screen(pos):
    """prints the layout of the board with the current state of the game."""
    print(f" {pos[7]} | {pos[8]} | {pos[9]} ")
    print("---|---|---")
    print(f" {pos[4]} | {pos[5]} | {pos[6]} ")
    print("---|---|---")
    print(f" {pos[1]} | {pos[2]} | {pos[3]} ")

def set_name():
    """Asks for userinput twice. Returns the given input as a tuple pair"""
    player1 = input('Player1 pick a name: ')
    player2 = input('Player2 pick a name: ')
    return (player1, player2)

def move(player, pos):
    """
    Asks the user where to place its next mark. Returns a position (int 1-9).

    keeps asking for input until a number 1-9 is given
    and the related position on the board is not filled.
    
        parameters:
            player (tuple pair): retrieve from GameState class turn attribute
            pos (list): retrieve from GameState class pos attribute
    """
    spot = ''
    while not spot.isdigit() or int(spot) not in range(1,10) or not pos[int(spot)] == ' ':
        spot = input(f"{player[0]}, pick a spot to place your mark '{player[1]}': ")
        if not spot.isdigit() or int(spot) not in range(1,10):
            print('Use numpad 1-9 to define your spot')
        elif not pos[int(spot)] == ' ':
            print("that spot is already filled! pick another spot.")
    return int(spot)

def check_win(pos):
    """loop untill a winning situation is found and return True, else return False."""
    win = [(1,2,3),(4,5,6),(7,8,9),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1)]
    for tup in win:
        if pos[tup[0]] != ' ' and pos[tup[0]]==pos[tup[1]]==pos[tup[2]]:
            break
    else:
        return False
    return True

def check_tie(pos):
    """loop to check if there are emty spots available and return False, else return True."""
    for i in pos:
        if i == ' ':
            break
    else:
        return True
    return False

def keep_playing():
    """
    Asks for userinport. Returns True for input 'Y', and False for 'N'.
    
    keeps asking for input untill eigther 'Y', 'y', 'N' or 'n' is given.
    """
    answer = ''
    while answer not in ('Y','y','N','n'):
        answer = input("Next round? (Y/N): ")
        if answer not in ('Y','y','N','n'):
            print("please enter 'Y' or 'N'.")
    return answer in ('Y','y')

if __name__ == "__main__":
    print("\nWelcome to Tic Tac Toe!")
    print("The first player to hit three marks in a row wins.\n")
    game = GameState(set_name())
    while True:
        print(f"\n{game.players[0][0]} plays with {game.players[0][1]}.")
        print(f"{game.players[1][0]} plays with {game.players[1][1]}.")
        while True:
            print(f"\n{game.turn[0]} is on turn.")
            screen(game.pos)
            game.set_pos(move(game.turn, game.pos))
            if check_win(game.pos):
                print(f"\n{game.turn[0]} won the game!")
                screen(game.pos)
                break
            if check_tie(game.pos):
                print("\nNo more moves available. Thats a tie!")
                screen(game.pos)
                break
            game.next_turn()
        if keep_playing():
            game.next_game()
        else:
            break
    print("\nSee you next time!")
