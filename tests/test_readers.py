import pathlib
from wordfinder import readers

_datapath = pathlib.Path(__file__).resolve().parent / "data"
_test_data_zip = _datapath / "words.zip"

class TestReaders:

    def test_read_zip_default(self):
        zipped_data = readers.read_zipfile()
        assert zipped_data != None

    def test_read_zip_test(self):
        """
        Reads the test zipfile which contains good and bad data
        """
        zipped_data = readers.read_zipfile(_test_data_zip)
        assert zipped_data != None
        assert len(zipped_data) == 4

        words = ["red", "blue", "green", "valley"]
        for word in words:
            assert word in zipped_data

        for word in words:
            assert word.upper() not in zipped_data
