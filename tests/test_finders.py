from wordfinder import array2d, wordsbag, finders, readers, validators


class TestFinders:

    def test_finder_arr2d(self):
        # Setup initial data elements
        words = readers.read_zipfile()
        validator = validators.ValidatorBasic(3, 25)
        bagowords = wordsbag.WordsBag([validator])
        bagowords.from_collection(words)
        # Create array 2d w/ data 
        arr2d = array2d.Array2D(5,5)
        arr_data = [ ["c", "a", "g", "i", "p"],
                     ["t", "b", "v", "w", "b"],
                     ["y", "n", "s", "w", "a"],
                     ["b", "e", "p", "f", "g"],
                     ["qu", "e", "k", "t", "s"],
                   ]

        for y in range(0, len(arr_data)):
            row = arr_data[y]
            for x in range(0, len(row)):
                arr2d.set_at(row[x], x, y)


        finder_arr2d = finders.FinderArray2D(arr2d, bagowords)
        found_words = finder_arr2d.find_words()

        word_set = set()
        for word_data in found_words:
            word_set.add(word_data[0])

        for word in word_set:
            assert bagowords.contains_word(word)

        print("...")
        print("Full Words:", len(bagowords.full_words) )
        print("Stems:", len(bagowords.word_stems) )
        print("Found Word Count:", len(found_words))

