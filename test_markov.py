import unittest
import markov

class TestMarkov(unittest.TestCase):
    def test_get_table(self):
        res = markov.get_table('abacab')
        self.assertEqual(res, {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}})


    def test_get_table2(self):
        res = markov.get_table('abc', size=2)
        
        self.assertEqual(res, {'ab': {'c':1}})

        
    def test_predict(self):
        m = markov.Markov('xyz')
        res = m.predict('y')
        self.assertEqual(res, 'z') 
    
if __name__ == '__main__':
    # i'm executing main file
    unittest.main()
