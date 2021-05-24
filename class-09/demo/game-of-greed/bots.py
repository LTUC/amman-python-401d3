from abc import ABC, abstractmethod
import builtins
import re
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game of Greed bots"""

    def __init__(self, print_all=False):

        # Variables for storing useful data
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0
        self.total_score = 0

        # Provide our bot with the ability to interact with the game
        # Since the game uses stdin and stdout via print and input calls
        # We will create mock versions of those calls

        # First we backup the real print and input
        self.real_print = print
        self.real_input = input

        # Then we replace them with out mock versions
        builtins.print = self._mock_print
        builtins.input = self._mock_input

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""
        # self.real_print(args)
        line = " ".join(args)
        # exit()
        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))
        # *** 1 1 3 4 5 5 ***
        elif line.startswith("*** "):

            self.last_roll = [int(ch) for ch in line if ch.isdigit()]
            # [1,1,3,4,5,5]
        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice() # -> "1155"

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit() # b, r, q

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = "" 

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""

        mega_total = 0

        for _ in range(num_games):
            player = cls() # Create an instance of our Bot Subclass
            game = Game()
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class MuBot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        if self.dice_remaining < 3:
            return "b"
        else:
            return "r"
class AbedBot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        if self.dice_remaining < 4:
            return "b"
        else:
            return "r"
class MoMoneyBot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        if self.unbanked_points > 1000:
            return "b"
        else:
            return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        return super()._enter_dice()


if __name__ == "__main__":
    num_games = 100
    NervousNellie.play(num_games)
    MuBot.play(num_games)
    AbedBot.play(num_games)
    MoMoneyBot.play(num_games)

# BaseBot -> Bot1, Bot2, etc...
# read the screen
## parse some of the data it read and store as useful variables
## dice_remaining, unbanked points, last_prompt, last_roll
# Implement different strategies for when to roll / bank and for which dice to keep
# simple logical conditions based the information that we read
# send input back to game
## We have to know which promp we are responding to in order to ensure we are sending meaningful input
