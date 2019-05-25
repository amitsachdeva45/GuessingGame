from stringDatabase import stringDatabase
class game:
    """
    Class Game
    In this class, going to do different operations like guessing the words, calculating final score,
    requesting letter, and can request to give up, even reading frequency of all letters

    Attributes
    ----------
    current_str : str
        The word which is written by User or on which we are running operations
    guessed_str: str
        The word which is guessed by machine or secret word
    status: str
        Final status of game i.e. success or gave up
    missed_letters: str
        Entering wrong letter
    bad_guesses: str
        Entering whole word wrong
    totalScore: int
        Final Scores of game
    frequency: dict
        Frequency of all letters

    Methods
    -------

    option_selected(self, option)
        Calling specific function on selecting different options

    guessed(self)
        Function in which we are guessing whole word and checking
        if word guessed is bad guess or correct guess so that we can calculate
        final score

    tell_me(self)
        Function in which we request whole word and want to give up

    letter(self)
        Function in which we are requesting one letter and checking if guessed letter is corect or not

    final_score(self)
        Function writing final score in proper format
    """
    current_str = ""
    guessed_str = ""
    status = ""
    missed_letters = 0
    bad_guesses = 0
    tellMeCounter = 0
    totalScore = 0.0
    frequency = dict()
    totalRequestCount = 0
    def __init__(self,current_str, guessed_str):
        """
        Intializing user strings for proper operations, guessed string, storing frequency of each letter

        Parameters
        ----------
        current_str : str
            The word which is written by User or on which we are running operations
        guessed_str: str
            The word which is guessed by machine or secret word
        """
        self.sD = stringDatabase()
        self.current_str = current_str
        self.guessed_str = guessed_str
        self.tellMeCounter = 0
        self.totalScore = 0.0
        self.frequency = self.sD.read_all_frequency()

    def option_selected(self, option):
        """
        Calling specific function on selecting different options

        Parameters
        ----------
        option : int
            Option entered by user either g => guess, t=> tell me, l=>letter

        Returns
        -------
        int
            return 1=>if game is done or 0=> if game continues
        """
        if option == "g":
            return self.guessed()
        elif option == "t":
            return self.tell_me()
        else:
            return self.letter()

    def guessed(self):
        """
        Taking input from user and check if guessed letter is correct or not
        If guess is incorrect, increment bad_guess
        if guess is correct, calculate total scores

        Returns
        -------
        int
            return 1=>if game is done or 0=> if game continues
        """
        value = input("Enter a word:  ")
        score = 0
        if value != self.guessed_str:
            print("Current Guess: ",self.current_str)
            self.bad_guesses += 1
            return 0
        else:
            i = 0
            while i<len(self.current_str):
                if self.current_str[i] == '-':
                    score = score + self.frequency[self.guessed_str[i]]
                i = i+1
            self.status = 'success'
            if self.totalRequestCount == 0:
                self.totalRequestCount = 1
            val = (score/self.totalRequestCount)
            self.totalScore =  val *(1- ((self.bad_guesses * 10.0)/100.0))
            return 1


    def tell_me(self):
        """
        Requesting whole word as user wants to gave up

        Returns
        -------
        int
            return 1=>game is done
        """
        i = 0
        self.totalScore = 0.0
        while i<len(self.current_str):
            if self.current_str[i] == "-":
                self.totalScore = self.totalScore + self.frequency[self.guessed_str[i]]
            i = i +1
        self.totalScore = self.totalScore*(-1)

        print("Current Guess: ", self.guessed_str)
        self.status = "Give up"
        return 1


    def letter(self):
        """
        Requesting one letter and input from users
        If Letter is correct, add letter to correct empty score
        if letter is incorrect, increment missed_letters

        Returns
        -------
        int
            return 1=>if game is done or 0=> if game continues
        """
        self.totalRequestCount += 1
        value = input("Enter a Letter:  ")
        flag = 0
        i=0
        str = ""
        count = 0
        while i<len(self.guessed_str):
            if self.guessed_str[i] == value:
                str = str + self.guessed_str[i]
                count += 1
                flag = 1
            else:
                str = str + self.current_str[i]
            i = i +1
        self.current_str = str
        if flag == 0:
            self.missed_letters += 1
        print("You found ",count," letters\n")
        print("Current Guess: ", self.current_str)
        if self.guessed_str == self.current_str:
            self.status = 'Success'
            return 1
        else:
            return 0

    def final_score(self, i):
        """
        Write final Score of a game in proper format as required
        """
        print(i, "    ",self.guessed_str," ",self.status,"     ",self.bad_guesses,"   ", self.missed_letters,"    ",self.totalScore)
        return self.totalScore

    def get_status(self):
        """
        Get status of a particular game
        """
        return self.status

