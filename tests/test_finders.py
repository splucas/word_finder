import pytest

from wordfinder import array2d, wordsbag, finders, readers, validators

@pytest.fixture
def words_bag():
    # Setup initial data elements
    words = readers.read_zipfile()
    validator = validators.ValidatorBasic(3, 25)
    bagowords = wordsbag.WordsBag([validator])
    bagowords.from_collection(words)
    return bagowords

@pytest.fixture
def chrs_5x5():
    return [ ["c", "a", "g", "i", "p"],
             ["t", "b", "v", "w", "b"],
             ["y", "n", "s", "w", "a"],
             ["b", "e", "p", "f", "g"],
             ["qu", "e", "k", "t", "s"],
           ]
    

class TestFinders:

    def test_finder_on_5x5(self, chrs_5x5, words_bag):
        # Create array 2d w/ data 
        arr2d = array2d.Array2D(5,5)

        for y in range(0, len(chrs_5x5)):
            row = chrs_5x5[y]
            for x in range(0, len(row)):
                arr2d.set_at(row[x], x, y)


        finder_arr2d = finders.FinderArray2D(arr2d, words_bag)
        found_words = finder_arr2d.find_words()

        word_set = set()
        for word_data in found_words:
            word_set.add(word_data[0])

        for word in word_set:
            assert words_bag.contains_word(word)

        print("...")
        print("Full Words:", len(words_bag.full_words) )
        print("Stems:", len(words_bag.word_stems) )
        print("Found Word Count:", len(found_words))

