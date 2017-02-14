import numpy as np
import intertools as it
import string.punctuation as punc
from collections import Counter, OrderedDict

def get_letter_freq(txt, n, letters_set):
    """
    Return 2 lists:

    comb_freq: is a list of size len(letters_set)^n  which contains
               the freq of the "n letters combination" in txt letters
               not present in letter_set are ignored

    comb: list of size len(letters_set)^n which contains the "n letters
          combinations", in the same order as comb_freq

    example: n=3       letter_set='abc'
    aaa aab aac aba abb abc aca acb acc baa bab bac bba bbb bbc bca ...
    """

    comb = []
	for i in it.product(letters_set, repeat=n):
		comb.append(''.join(map(str, i)))
	comb_freq = txt.count(combinations)

    return comb_freq, comb

def get_word_freq(txt, word_end_set=punc):
    """
    Return 2 lists:

    word_freq.values(): frequency of all the words in txt

    word_frek.keys(): all the words in txt, splited by spaces and all
                      characters in word_end_set (set to
                      string.punctuation by default), sorted by
                      word_freq.values()
    """
	words = Counter(''.join([c for c in txt if not c in word_end_set])\
	                                                           .split())
	word_freq = OrderedDict(sorted(charcount.items(), \
	                                               key=lambda t: -t[1]))

	return word_freq.values(), word_freq.keys()


class LineWiseFrameIterator:

    def __init__(self, filepath, frame_size, frame_overlap):
        #frame_size expressed in number of lines
        self.filepath = filepath
        self.frame_size = frame_size
        self.frame_overlap = frame_overlap
        self.filepath = filepath
        self.i = 0
        with open(filepath, 'r') as myfile:
            self.data = myfile.readlines()
        self.len = len(self.data)

    def __iter__(self):
        return self

    def __next__(self) :
        end = self.i + self.frame_size
        if self.i > self.len:
            raise StopIteration()
        if end < self.len:
            ret = self.data[self.i:end]
        else:
            ret = self.data[self.i:-1]
        self.i += self.frame_size - self.frame_overlap
        return ''.join(ret)


class CharWiseFrameIterator:
    def __init__(self, filepath, frame_size, frame_overlap):
        self.filepath = filepath
        self.frame_size = frame_size
        self.frame_overlap = frame_overlap
        self.filepath = filepath
        self.i = 0
        with open(filepath, 'r') as myfile:
            self.data = myfile.read().replace('\n','').replace('\r','')
        self.len = len(self.data)

    def __iter__(self):
        return self

    def __next__(self) :
        end = self.i + self.frame_size
        if self.i > self.len:
            raise StopIteration()
        if end < self.len:
            ret = self.data[self.i:end]
        else:
            ret = self.data[self.i:-1]
        self.i += self.frame_size - self.frame_overlap
        return ret



def entropy(freq_tab):
    return np.sum(np.log(freq_tab)*freq_tab)

def get_letter_entropy(txt, n, letters_set):
    return entropy(get_letter_freq(txt, n, letters_set))

def get_word_entropy(txt, word_end_set):
    return entropy(get_word_freq(txt, word_end_set))

def letters_entropy_analysis(filepath, frame_size, frame_overlap, n, letters_set):
    results = []
    for frame in FrameIterator(filepath, frame_size, frame_overlap):
        results.append(get_letter_entropy(frame, n, letters_set))
    return results

def word_entropy_analysis(filepath, frame_size, frame_overlap, word_end_set):
    results = []
    for frame in FrameIterator(filepath, frame_size, frame_overlap):
        results.append(get_word_entropy(frame, n, letters_set))
    return results
