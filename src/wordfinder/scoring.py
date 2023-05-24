


class WordScoreBase:
    """
    Word Scoring base class.  Implement score_word in a subclass
    with scoring specific logic

    This class is meant to be subclassed.
    """
    def score_word(self,  word:str ) -> int:
        """
        Scores a word based on specific implementation rules.
        Override in a subclass and implement your scoring rules here.

        Args:
            word (str): The word to score

        Returns:
        A score value (integer)

        """
        raise NotImplemented
    

class WordScoreSimple(WordScoreBase):
    """
    Scores a word based on word length, using the following data and logic:

    Word Length | Score
    -------------------
         <= 4   |  1
         == 5   |  2
         == 6   |  3
         == 7   |  4
         >= 8   |  5

    """
    def __init__(self):
        self.length_score = ( (4,1), (5,2 ), (6,3), (7,4), (8,5) )
        
    def score_word(self, word: str) -> int:
        """
        Checks word length and provides a score value

        Args:
            word (str): The word to score

        Returns:
        A score value (integer)

        """

        assert isinstance(word, str)

        word_len = len(word)
        # Empty words are worth 0. 
        if word_len == 0: return 0

        word_score = 0
        for length_score in self.length_score:
            length, word_score = length_score
            if word_len <= length:
                break
        return word_score
           