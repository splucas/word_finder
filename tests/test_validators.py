from wordfinder import validators



class TestValidators:

    def test_basic(self):
        basic_validator = validators.ValidatorBasic(3, 5)

        assert basic_validator.is_valid(None) == False
        assert basic_validator.is_valid("") == False
        assert basic_validator.is_valid("a") == False
        assert basic_validator.is_valid("an") == False
        assert basic_validator.is_valid("ant") == True
        assert basic_validator.is_valid("ants") == True
        assert basic_validator.is_valid("aunts") == True
        assert basic_validator.is_valid("uncles") == False