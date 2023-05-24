from wordfinder import validators



class TestValidators:

    def test_basic(self):
        length_validator = validators.ValidatorWordLength(3, 5)

        assert length_validator.is_valid(None) == False
        assert length_validator.is_valid("") == False
        assert length_validator.is_valid("a") == False
        assert length_validator.is_valid("an") == False
        assert length_validator.is_valid("ant") == True
        assert length_validator.is_valid("ants") == True
        assert length_validator.is_valid("aunts") == True
        assert length_validator.is_valid("uncles") == False