

class WordsBag:
    def __init__(self, validators=None):

        # Word "Stems" are valid character combinations that lead to actual
        # words.  For example, the word "bug" has the following stems:
        #  "b" and "bu" 
        self.word_stems = set()  

        # Set containing full words
        self.full_words = set()

        self.validators = validators

    def contains_word(self, word:str) -> bool:
        return word in self.full_words
    
    def contains_stem(self, stem:str) -> bool:
        return stem in self.word_stems

    def _fixup_word(self, word:str):
        """
        Trim/strip whitespace and set to lowwercase
        """
        out_word = word.strip()
        out_word = out_word.lower()
        return out_word
    
    def _check_valid(self, word:str):
        """
        Check the word against the list of validators (if exists);
        Return NONE if no errors, or a list of error messages
        """
        errors = None
        if self.validators:
            errors = []
            for validator in self.validators:
                if not validator.is_valid(word):
                    errors.append(validator.get_error())
            if len(errors) == 0: 
                errors = None

        return errors
    def _add_word(self, word:str):
        """
        Adds a word to the collections. 
        Naively assumes the word is valid and of the correct form.
        """

        # Add the full word
        self.full_words.add(word)

        # Create and add stems
        cnt = 1
        while cnt < len(word):
            stem = word[0:cnt]
            self.word_stems.add( stem )
            cnt += 1


    def from_list(self, word_list:list[str]):
        """
        Iniitializes values from a list of words. 
        """
        for word_value in word_list:
            if word_value:
                word = self._fixup_word(word_value)
                errors = self._check_valid(word)
                if errors == None:
                    self._add_word(word)