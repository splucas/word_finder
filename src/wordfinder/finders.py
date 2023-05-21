from wordfinder import array2d, wordsbag


class FinderArray2D:
    """
    Searches for words located in a 2D Array. The array should be preloaded
    with valid characters(strings) that will make up search-words
    """
    # Offsets to search
    _neighbors = ( (-1, -1), (0, -1),  (1, -1),        
                   (-1,  0),           (1,  0),
                   (-1,  1), (0,  1),  (1,  1))

    def __init__(self, char_array2d, word_bag):
        assert char_array2d != None
        assert isinstance(char_array2d, array2d.Array2D)
        assert word_bag != None
        assert isinstance(word_bag, wordsbag.WordsBag)

        self.array2d = char_array2d
        self.word_bag = word_bag

        self.min_word_length = 3
        self.neighbors_cache = {}

        self.word_paths = []

    def get_neighbors(self, in_loc):
            out_neighbors = []
            width = self.array2d.width
            height = self.array2d.height

            for item in self._neighbors:
                xy = ( in_loc[0]+item[0], in_loc[1] + item[1]  )
                if xy[0] >= 0 and xy[0] < width and xy[1]>=0 and xy[1] < height:
                    out_neighbors.append(xy)
            return out_neighbors
    
    
    def build_neighbors_cache(self):
        for y in range(0, self.array2d.height):
            for x in range(0, self.array2d.width):
                pos = (x,y) 
                neighbors = self.get_neighbors( pos )
                if len(neighbors) > 0:
                    self.neighbors_cache[ pos ] = neighbors
        
        
    def build_word_path(self, current_path, the_word ):
        """
        current_path -- the path we're traveling; copies are created at each recursion level
        curr_root: the root node from where the path started
        the_word: accumulation of letters along the current_path
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
        for loc in self.neighbors_cache[ last_node ]:
            if loc not in current_path:
                next_path =  current_path + [loc]
                self.build_word_path(next_path, the_word )
             
        
    def find_words(self):
        """
        
        """
        self.build_neighbors_cache()

        valid_cells = []
        for y in range(0, self.array2d.height):
            for x in range(0, self.array2d.width):
                if self.array2d.get_at(x,y):
                    valid_cells.append( (x,y) )


        for root_pos in valid_cells:
            self.build_word_path( [ root_pos ], "")
        
        return self.word_paths        