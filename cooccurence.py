import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class co_occurence_matrix:

    def __init__(self):
        self.matrix = []
        self.feature_words = []
        self.column_index = {}
        self.row_index = {}
        self.reverse_row_index = {}

    def set_row_index(self, feature_words):
        self.feature_words = feature_words
        self.column_index = {}
        for i in xrange(0, len(feature_words)):
            self.column_index[feature_words[i]] = i

    def set_column_index(self, words):
        self.row_index = {}
        self.matrix = []
        self.words = words
        j = 0
        len_to_appen = len(self.column_index)
        for i in xrange(0, len(words)):
            if not self.row_index.has_key(words[i]):
                self.row_index[words[i]] = j
                self.reverse_row_index[j] = words[i]
                j += 1
                arr = [0 for x in xrange (0, 2 * len_to_appen)]
                self.matrix.append(arr)

    def get_matrix(self):
        return self.matrix

    def get_row_index(self):
        return self.row_index

    def get_column_index(self):
        return self.column_index

    def get_reverse_index(self):
        return self.reverse_row_index

    def fill_matrix(self, window):
        gap = len(self.feature_words)
        wordarrlen = len(self.words)
        for index in xrange(0, len(self.words)):
            if self.column_index.has_key(self.words[index]):
                columnind = self.column_index[self.words[index]]
                for i in xrange(1, window + 1):
                    if (index + i) > (wordarrlen - 1):
                        break
                    wordright = self.words[index + i]
                    rowind = self.row_index[wordright]
                    self.matrix[rowind][columnind] += 1
                for i in xrange(1, window + 1):
                    if (index - i) < 0:
                        break
                    wordleft = self.words[index - i]
                    rowind = self.row_index[wordleft]
                    self.matrix[rowind][columnind + gap] += 1

            #if index == 0:
            #    if self.column_index.has_key(self.words[index]):
            #        columnind = self.column_index[self.words[index]]
            #        wordright = self.words[index + 1]
            #        rowind = self.row_index[wordright]
            #        self.matrix[rowind][columnind] += 1
            #elif index == len(self.words) - 1:
            #    if self.column_index.has_key(self.words[index]):
            #        columnind = self.column_index[self.words[index]]
            #        wordleft = self.words[index - 1]
            #        rowind = self.row_index[wordleft]
            #        self.matrix[rowind][columnind + gap] += 1
            #else: 
            #    if self.column_index.has_key(self.words[index]):
            #        columnind = self.column_index[self.words[index]]
            #        wordright = self.words[index + 1]
            #        rowind = self.row_index[wordright]
            #        self.matrix[rowind][columnind] += 1
            #        wordleft = self.words[index - 1]
            #        rowind = self.row_index[wordleft]
            #        self.matrix[rowind][columnind + gap] += 1

        return self.matrix
