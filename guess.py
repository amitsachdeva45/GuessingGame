from stringDatabase import stringDatabase
from game import game
import random
class guess:
    """
    Class Guess
    This is main class where execution will be started

    In this class, we are keeping tracks of all games, keeping menu of all options
    and displaying the final scores, and executions of all games

    Attributes
    ----------
    game_list : list
        List of all games
    maxGameSize: int
        Max number of games which can be played
    sd: Object
        Object of stringDatabase class

    Methods
    -------

    read_file(self)
        Function to just read file from stringDatabase

    play_game(self)
        Function for executions of game by creating object and keeping records
        of all games and also providing menu to user

    show_score(self)
        Function to show all scores at end of playing all games/ after quiting
    """
    maxGameSize = 0
    maxCurrentString = 0
    def __init__(self):
        """
        Intializing stringDatabase class and values of maxGameSize, list of keeping tracks of game object
        """
        self.sD = stringDatabase()
        self.maxGameSize = 100
        self.maxCurrentString = 4
        self.game_list = list()

    def read_file(self):
        self.sD.read_data_file()
        self.sD.read_all_frequency()

    def play_game(self):
        """
        Function for executions of game by creating object and keeping records
        of all games and also providing menu to user
        """
        i = 0

        print(" *** Great Guessing Game ***\n")
        while i<self.maxGameSize:
            val = random.randint(0,len(self.sD.get_file_data())-1)
            guessed_str = self.sD.get_file_data()[val]
            print("********************************\n")
            current_str = "-"*self.maxCurrentString
            print("*********************Start Game*********************\n")
            print("Current Guess: ",current_str,"\n")
            quit = 0
            temp_game = game(current_str,guessed_str)
            while True:
                value = input("g = guess, t = tell me, l for a letter, and q to quit\n")
                if value == 'q':
                    quit = 1
                    break
                else:
                    if temp_game.option_selected(value) == 1:
                        break

            if temp_game.get_status() == '':
                temp_game.status = "Gave up"
            if quit == 1:
                break
            self.game_list.append(temp_game)


            i = i+1

    def show_score(self):
        """
        Show final scores after execution of all games
        """
        i =0
        print("Game  Word  Status  Bad Guess  Missed Letters  Score\n")
        print("----  ----  ------  ---------  --------------  -----\n")
        finalScore = 0.0
        while i<len(self.game_list):
            finalScore = finalScore + self.game_list[i].final_score(i+1)
            i = i+1
        print("\n Final Score: ",finalScore)


if __name__ == '__main__':
    guess = guess()
    guess.read_file()
    guess.play_game()
    guess.show_score()

