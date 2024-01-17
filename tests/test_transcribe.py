# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # Blank case
    seq = ''
    correct_ans = ''
    transcribed = transcribe(seq)
    assert transcribed == correct_ans


    # Bad seq case
    with pytest.raises(KeyError):
        seq = 'Foo'
        transcribed = transcribe(seq)

    # Single base case not T
    seq = 'G'
    correct_ans = 'C'
    transcribed = transcribe(seq)
    assert transcribed == correct_ans
        
    # Single base case T
    seq = 'A'
    correct_ans = 'U'
    transcribed = transcribe(seq)
    assert transcribed == correct_ans

    # Regular case
    seq = 'ACTGAACCC'
    correct_ans = 'UGACUUGGG'
    transcribed = transcribe(seq)
    assert transcribed == correct_ans


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Blank case
    seq = ''
    correct_ans = ''
    transcribed = reverse_transcribe(seq)
    assert transcribed == correct_ans


    # Bad seq case
    with pytest.raises(KeyError):
        seq = 'Foo'
        transcribed = reverse_transcribe(seq)

    # Single base case not T
    seq = 'G'
    correct_ans = 'C'
    transcribed = reverse_transcribe(seq)
    assert transcribed == correct_ans
        
    # Single base case T
    seq = 'A'
    correct_ans = 'U'
    transcribed = reverse_transcribe(seq)
    assert transcribed == correct_ans

    # Regular case
    seq = 'ACTGAACCC'
    correct_ans = 'GGGUUCAGU'
    transcribed = reverse_transcribe(seq)
    assert transcribed == correct_ans

    # Symmetric case
    seq = 'CCCCCCC'
    correct_ans = 'GGGGGGG'
    transcribed = reverse_transcribe(seq)
    assert transcribed == correct_ans