from src.utils.validation import is_in_sentence
import pytest

def test_found_char():
  assert is_in_sentence('abcde','e')

def test_not_found_char():
  assert is_in_sentence('abcde','f') is False

def test_nonetype_sentence():
  with pytest.raises(AttributeError):
    assert is_in_sentence(None,':')

def test_wrong_type_char():
  with pytest.raises(TypeError):
    assert is_in_sentence('1234,5',5)

def test_list_type_sentence():
  with pytest.raises(AttributeError):
    assert is_in_sentence([1,2,3,4],'2')
