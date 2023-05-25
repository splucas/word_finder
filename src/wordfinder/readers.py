# Data readers used to read and import word data; read functions
# return a python set of words
import pathlib
import string 
from zipfile import ZipFile

_datapath = pathlib.Path(__file__).resolve().parent / "data" 
_zipdata = _datapath / "english_words.zip"


def to_word_set(words:list[str]) -> set:
    """
    Create a set of words where a word must be at least 1 character
    in length and contain only ascii lowercase letters
    """
    out_set = set()
    for word in words:
        word = word.strip()
        if word:
            out_set.add(word)
    return out_set


def read_zipfile( fpath:pathlib.Path = _zipdata ) -> set:
    """
    Read a zipfile; expects one entry with the same name as the zipfile, but
    with a .txt suffix.  Entries must be newline delimited, with one
    word per line

    Args:
        fpath: Path to Zip file

    Returns:
        set of words
    """
    name = fpath.stem
    word_data = None
    with ZipFile(str(fpath)) as zipped_file:
        with zipped_file.open(f'{name}.txt') as wordfile:
            # With zips, read() returns bytes
            word_data = wordfile.read()
            # Decode
            word_data = word_data.decode("utf-8")
            word_data = word_data.split("\n")
            
    return  to_word_set( word_data )
