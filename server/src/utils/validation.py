def is_in_sentence(word: str, chr: str) -> bool:
  try:
    char_in_word = word.find(chr)
    if char_in_word == -1:
      return False
    return True
  except (AttributeError) as e:
    raise e
  except TypeError as err:
    raise err

