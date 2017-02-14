import numpy as np
import intertools as it


def get_letter_freq(txt, n, letters_set):
    """
    return 2 arrays:
    
    comb_freq: is an array of size len(letters_set)^n  which contains
    the freq of the "n letters combination" in txt letters not present 
    in letter_set are ignored
    
    comb: array of size len(letters_set)^n which contains the 
    "n letters combinations", in the same order as comb_freq
    
    example: n=3       letter_set='abc'
    aaa aab aac aba abb abc aca acb acc baa bab bac bba bbb bbc bca ...
    """
    
    comb = []
	for i in it.product(letters_set, repeat=n):
		comb.append(''.join(map(str, i)))
	comb_freq = txt.count(combinations)
	
    return comb_freq, comb

def get_word_freq(txt, word_end_set):
    """
    return word freq
    """

class LineWiseFrameIterator:
    """
    usage:

    for frame in LineWiseFrameIterator('../data/bible/xxx.txt', 1000, 500):
        print(frame)
    """

    def __init__(self, filepath, frame_size, frame_overlap):
        #frame_size expressed in number of lines
        pass

    def __iter__(self) :
        pass

    def next(self) :
        pass


class CharWiseFrameIterator:
    """
    usage:

    for frame in LineWiseFrameIterator('../data/bible/xxx.txt', 1000, 500):
        print(frame)
    """

    def __init__(self, filepath, frame_size, frame_overlap):
        #frame_size expressed in number of char
        pass

    def __iter__(self) :
        pass

    def next(self) :
        pass


def entropy(freq_tab):
    """
    returns the entropy
    """
    pass

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
