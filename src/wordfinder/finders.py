from wordfinder import array2d, wordsbag


class BreadthFinder:
    """
    Finds words located in a 2D Array using a breadth-first type searching
    algorithm.  The array should be preloaded with valid characters(strings) 
    that will make up search-words. 
    """
    # Offsets to search
    _neighbors = ( (-1, -1), (0, -1),  (1, -1),        
                   (-1,  0),           (1,  0),
                   (-1,  1), (0,  1),  (1,  1))

    def __init__(self, char_array2d, word_bag, min_word_len=3):
        """
        Initialize the the finder

        Args:
            char_array2d:  An Array2D Instance
            word_bagL A wordbag.Wordbag instance
            min_word_length: The minimum length required for a word to captured
        """
        assert char_array2d != None
        assert isinstance(char_array2d, array2d.Array2D)
        assert word_bag != None
        assert isinstance(word_bag, wordsbag.WordsBag)

        self.array2d = char_array2d
        self.word_bag = word_bag

        self.min_word_length = min_word_len
        self.neighbors_cache = {}

        self.word_paths = []

    def get_neighbors(self, in_pos:list|tuple) -> list: 
            """
            Builds a list of valid neighboring Array2D positions related to 
            in_pos. Neighbor discovery is based on searching the list of 
            offsets that represent cardinal and ordinal directions:
                (-1, -1), (0, -1),  (1, -1),        
                (-1,  0),           (1,  0),
                (-1,  1), (0,  1),  (1,  1)

            Args:
                in_pos:list|tuple : Source position (x,y)

            Returns:
                List of neighboring positions in the form of
                [(x1,y1), .. (xN,xN))]
            """
            out_neighbors = []
            width = self.array2d.width
            height = self.array2d.height

            for item in self._neighbors:
                xy = ( in_pos[0]+item[0], in_pos[1] + item[1]  )
                if xy[0] >= 0 and xy[0] < width and xy[1]>=0 and xy[1] < height:
                    out_neighbors.append(xy)
            return out_neighbors
    
    
    def _build_neighbors_cache(self):
        """
        For every position, create a dictionary entry of the position's nearest
        neighbors.  
        """
        for y in range(0, self.array2d.height):
            for x in range(0, self.array2d.width):
                pos = (x,y) 
                neighbors = self.get_neighbors( pos )
                if len(neighbors) > 0:
                    self.neighbors_cache[ pos ] = neighbors
        
        
    def _build_word_path(self, current_path: list, the_word: str ):
        """
        Recursively walks builds out 'current_path' to discover words in the
        2d array.  Exits early if the collection of letters along a given
        path is not part of a word.

        Args:
            current_path (list):- the path we're traveling; copies are created
                at each recursion level
            the_word (str): accumulation of letters along the current_path
        """
        
        word_bag = self.word_bag
        last_node = current_path[-1]
        
        cell_val = self.array2d.get_at( last_node[0], last_node[1])
        the_word += cell_val
        
        # Not a valid word stem, abort early
        if not word_bag.contains_stem(the_word):  
            return
        
        # Found a word, store it for processing later
        if len(the_word) >= self.min_word_length and \
           word_bag.contains_word(the_word):
            self.word_paths.append( (the_word, current_path )   )
            
        # Process neighbors, recurse if not processed
        for xy_pos in self.neighbors_cache[ last_node ]:
            if xy_pos not in current_path:
                next_path =  current_path + [xy_pos]
                self._build_word_path(next_path, the_word )
             
        
    def find_words(self) -> list:
        """
        Entry point to Searching the array 2D for all words it contains.  
                
        Returns:
        A list of tuples that contains the word, and its path:
          (word, [(x1,y1), (x2,y2), .. (xN, yN)])

        """
        self._build_neighbors_cache()

        valid_cells = []
        for y in range(0, self.array2d.height):
            for x in range(0, self.array2d.width):
                if self.array2d.get_at(x,y):
                    valid_cells.append( (x,y) )


        for root_pos in valid_cells:
            self._build_word_path( [ root_pos ], "")
        
        return self.word_paths        