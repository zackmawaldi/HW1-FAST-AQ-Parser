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
        bad_fa = FastaParser('./tests/bad.fa')
        seq_inter = iter(bad_fa)
        next(seq_inter)
    

    # Check bad seq files. Second is blank.fa
    with pytest.raises(ValueError):
        blank_fa = FastaParser('./tests/blank.fa')
        seq_inter = iter(blank_fa)
        next(seq_inter)
    

    # check good_single.fa
    single_seq = FastaParser('./tests/good_single.fa')
    seq_inter = iter(single_seq)
    name, seq = next(seq_inter)
    
    assert name == 'seq1'
    assert seq == 'ACGGACCACCATGAA'

    
    # check good_two.fa
    two_seq = FastaParser('./tests/good_two.fa')
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
    
    # Test a good .fa file
    single_seq = FastaParser('./tests/good_single.fa')
    seq_inter = iter(single_seq)
    name, seq = next(seq_inter)
    assert name is not None

    # Test reading a fastq file. First item should be None
    single_seq = FastaParser('./data/test.fq')
    seq_inter = iter(single_seq)
    name, seq = next(seq_inter)
    assert name is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    
    # check good fastaq, ../data/test.fq
    single_seq = FastqParser('./data/test.fq')
    seq_inter = iter(single_seq)
    name, seq, qual = next(seq_inter)

    assert name == 'seq0'
    assert seq == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    assert qual == """*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="""

    name, seq, qual = next(seq_inter)

    assert name == 'seq1'
    assert seq == 'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG'
    assert qual == """'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%"."-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""""

    # Check bad seq files. Second is blank.fq
    with pytest.raises(ValueError):
        blank_fq = FastqParser('./tests/blank.fq')
        seq_inter = iter(blank_fq)
        next(seq_inter)

    # Check bad seq files. First is bad.fq
    bad_fq = FastqParser('./tests/bad.fq')
    seq_inter = iter(bad_fq)
    name, seq, qual = next(seq_inter)
    assert name == None


def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Testing a good fastq file 
    single_seq = FastqParser('./data/test.fq')
    seq_inter = iter(single_seq)
    name, seq, qual = next(seq_inter)
    assert name is not None

    # Test a .fa file. first line should be None
    single_seq = FastqParser('./tests/good_single.fa')
    seq_inter = iter(single_seq)
    name, seq, qual = next(seq_inter)
    assert name is None

def test_should_fail():
    assert 1 == 2