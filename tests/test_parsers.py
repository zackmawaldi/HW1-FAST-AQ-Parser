# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    
    # Check bad seq files. First is bad.fa
    with pytest.raises(ValueError):
        bad_fa = FastaParser('bad.fa')
        seq_inter = iter(bad_fa)
        next(seq_inter)
    

    # Check bad seq files. Second is blank.fa
    with pytest.raises(ValueError):
        blank_fa = FastaParser('blank.fa')
        seq_inter = iter(blank_fa)
        next(seq_inter)
    

    # check good_single.fa
    single_seq = FastaParser('good_single.fa')
    seq_inter = iter(single_seq)
    name, seq = next(seq_inter)
    
    assert name == 'seq1'
    assert seq == 'ACGGACCACCATGAA'

    
    # check good_two.fa
    two_seq = FastaParser('good_two.fa')
    seq_inter = iter(two_seq)
    name, seq = next(seq_inter)
    
    assert name == 'seq1'
    assert seq == 'ACGGACCACCATGAA'

    name, seq = next(seq_inter)
    
    assert name == 'seq2'
    assert seq == 'ACGGACCTGAA'



def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    pass