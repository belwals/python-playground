'''
This is the docstring for the Markov module.

>>> m= Markov('ab')
>>> m.predict('a')
'b'
'''
import random

class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)

    def predict(self, data):
        options = self.table.get(data, {})
        if not options:
            raise KeyError(f'{data} not found')
        possibles = []
        for char in options:
            for i in range(options[char]):
                possibles.append(char)
        return random.choice(possibles)
            
def get_table(txt, size=1):
    ''' This is the get_table function
    >>> get_table('ab')
    {'a': {'b': 1})
    '''
    results = {}
    for i in range(len(txt) -size):
        chars = txt[i:size+i]
        out =txt[i+size]
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results
            
    
