

class WordsBag:
    def __init__(self, validators=None):
        """
        Word "Stems" are valid character combinations that lead to actual
        words.  For example, the word "bug" has the following stems:
        "b" and "bu" 
        """
        self.word_stems = set()  

        # Set containing full words
        self.full_words = set()

        self.validators = validators

    def contains_word(self, word:str) -> bool:
        """
        Is word contained within this collection?

        Args:
            word (str): The word to check

        Returns:
            bool: True if word exists in the collection, otherwise False
        """
        return word in self.full_words
    
    def contains_stem(self, stem:str) -> bool:
        """
        Checks to see if a stem exists in the collection. A stem is a group
        of letters that ultimately ends as a full word.

        Args:
            stem (str): A partial word beginning to check

        Returns:
            bool: True if the stem is in the collection, otherwise False
        """
        return stem in self.word_stems

    def _fixup_word(self, word:str):
        """
        Trim/strip whitespace and set to lowwercase

        Args:
            word (str): The word to fixup
        """
        out_word = word.strip()
        out_word = out_word.lower()
        return out_word
    
    def _check_valid(self, word:str):
        """
        Check the word against the list of validators (if exists);
        Return NONE if no errors, or a list of error messages

        Args:
            word (str): The word to validate
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
    def add_word(self, word:str):
        """
        Adds a valid word to the collections. Words are first trimmed and then 
        validated against the validation rules (if any).  From the word, stems 
        are then created and stored for later use.

        Args:
            word (str): source word to store
        """
        if not word or not isinstance(word, str): return

        word = self._fixup_word(word)
        errors = self._check_valid(word)
        if errors != None: 
            return

        # Add the full word
        self.full_words.add(word)

        # Create and add stems
        cnt = 1
        while cnt < len(word):
            stem = word[0:cnt]
            self.word_stems.add( stem )
            cnt += 1


    def from_collection(self, word_list:list[str] | set):
        """
        Iniitializes values from a collection (list or set) of words. 

        Args:
            word_list (list or tuple): A list or tuple containing words to use

        """
        for word_value in word_list:
            self.add_word(word_value)

