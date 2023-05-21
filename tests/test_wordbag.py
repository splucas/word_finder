from wordfinder import wordsbag, validators

class TestWordbag:
    def _get_valid_wordbag(self, minsize, maxsize, testwords):
        # Create the validator(s) used by the wordbag
        validator = validators.ValidatorBasic(minsize, maxsize)
        wordbag = wordsbag.WordsBag([validator])
        wordbag.from_collection(testwords)
        return wordbag
    def _get_stems_list(self, word):
        stems = []
        cnt = 1
        while cnt < len(word):
            stems.append( word[0:cnt]  )
            cnt += 1
        return stems

    def test_wordbag_words(self):
        min_size = 3
        max_size = 5
        test_words = ["an", "red", "green", "blue", "colors"]
        wordbag = self._get_valid_wordbag(min_size, max_size, test_words)

        # Test for words:
        for word in test_words:
            if len(word) >= min_size and len(word) <= max_size:
                assert wordbag.contains_word(word) == True
            else:
                assert wordbag.contains_word(word) == False

    def test_wordbag_stems(self):
        min_size = 3
        max_size = 5
        test_words = ["an", "red", "green", "blue", "colors"]
        wordbag = self._get_valid_wordbag(min_size, max_size, test_words)

        # Test for words:
        for word in test_words:
            stems_list = self._get_stems_list(word)
            for stem in stems_list:
                if len(word) >= min_size and len(word) <= max_size:
                    assert wordbag.contains_stem(stem) == True
                else:
                    assert wordbag.contains_stem(stem) == False


