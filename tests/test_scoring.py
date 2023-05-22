from wordfinder import scoring

class TestScoring:

    def test_basic_word_score(self):
        simple_scorer = scoring.WordScoreSimple()
        
        assert simple_scorer.score_word("") == 0
        assert simple_scorer.score_word("red") == 1
        assert simple_scorer.score_word("read") == 1
        assert simple_scorer.score_word("ready") == 2
        assert simple_scorer.score_word("sixwrd") == 3
        assert simple_scorer.score_word("svnword") == 4
        assert simple_scorer.score_word("eghtword") == 5
        assert simple_scorer.score_word("stupification") == 5