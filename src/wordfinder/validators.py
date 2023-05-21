# Contains Word Validator classes.  

class WordValidator:
    def _set_error(self, err_str:str):
        self.error = err_str

    def get_error(self) -> str:
        return getattr(self, "error", None)
    
    def is_valid(self, word:str) -> bool:
        raise NotImplemented
    

class ValidatorBasic(WordValidator):
    def __init__(self, min_len:int, max_len:int):
        self.min_word_len = min_len
        self.max_word_len = max_len

    def is_valid(self, word: str) -> bool:
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


