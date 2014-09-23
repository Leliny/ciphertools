DICT_PATH = '/usr/share/dict/words'

def get_words():
  with open(DICT_PATH, 'r') as file:
    lines = file.readlines()
    return set([w.lower().strip() for w in lines])

