DICT_PATH = '/usr/share/dict/words'

def get_words():
  with open(DICT_PATH, 'r') as f:
    lines = f.readlines()
    return set([w.lower().strip() for w in lines])

