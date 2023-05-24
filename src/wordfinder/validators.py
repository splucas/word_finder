# Contains Word Validator classes.  

class WordValidatorBase:
    """
    Base class from which to derive word validators.  Validators ensure
    that words meet certain rules/criteria prior to their use.
    """
    def _set_error(self, err_str:str):
        """
        Sets the internal error message. The error message indicates why
        a word failed validation

        Args:
            err_str (str):  String message describing the error
        """
        self.error = err_str

    def get_error(self) -> str:
        """
        Returns:
        String indicating the validation failure error message
        """
        return getattr(self, "error", None)
    
    def is_valid(self, word:str) -> bool:
        """
        Validation rule implementation.

        Override in sublcass

        Args:
            word (str): The word to check against this particular rule

        Returns:
        Boolean indicating valid(True) or not valid(False). If not valid, then
        use get_error to understand why.
        """
        raise NotImplemented
    

class ValidatorWordLength(WordValidatorBase):
    """
    Validates that a word is within a min/max length range.
    """
    def __init__(self, min_len:int, max_len:int):
        """
        Initializes the validator

        Args:
            min_len (int): The minimum allowed word length
            max_len (int): The maximum allowed word length
        """
        self.min_word_len = min_len
        self.max_word_len = max_len

    def is_valid(self, word: str) -> bool:
        """
        Validates that word is within the given length range

        Args:
            word (str): The word to check 

        Returns:
        True if the word length fits within the given limits, otherwise False        
        """        
        
        if not word:
            self._set_error("Invalid Word (null/None) or empty")
            return False
        
        word_len = len(word)
        if word_len < self.min_word_len:
            err_msg = f"Word {word} too short. Min length {self.min_word_len}"
            self._set_error(err_msg)
            return False
        elif word_len > self.max_word_len:
            err_msg = f"Word {word} too long. Max length {self.max_word_len}"
            self._set_error(err_msg)
            return False
        
        return True


