


class WordScoreBase:
    """
    Word Scoring base class.  Implement score_word in a subclass
    with scoring specific logic
    """
    def score_word(self,  word:str ) -> int:
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
           