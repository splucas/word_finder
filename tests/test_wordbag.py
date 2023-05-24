import pytest

from wordfinder import wordsbag, validators

@pytest.fixture
def test_words():
    return ["an", "red", "green", "blue", "colors"]

@pytest.fixture
def word_bag(test_words):
    validator = validators.ValidatorWordLength(3, 5)
    wordbag = wordsbag.WordsBag([validator])
    wordbag.from_collection(test_words)
    return wordbag

@pytest.fixture
def word_sizes():
    return 3,5

@pytest.fixture
def word_stems(test_words):
    wstems = {}
    for word in test_words:
        stems = []
        wstems[word] = stems
        cnt = 1
        while cnt < len(word):
            stems.append( word[0:cnt]  )
            cnt += 1
    return wstems


class TestWordbag:

    def test_wordbag_words(self, test_words, word_bag, word_sizes):
        min_size,  max_size = word_sizes
        # Test for words:
        for word in test_words:
            if len(word) >= min_size and len(word) <= max_size:
                assert word_bag.contains_word(word) == True
            else:
                assert word_bag.contains_word(word) == False

    def test_wordbag_stems(self, test_words, word_bag, word_sizes, word_stems):
        min_size, max_size = word_sizes

        # Test for stems:
        for word in test_words:
            stems_list = word_stems[word]
            for stem in stems_list:
                if len(word) >= min_size and len(word) <= max_size:
                    assert word_bag.contains_stem(stem) == True
                else:
                    assert word_bag.contains_stem(stem) == False


