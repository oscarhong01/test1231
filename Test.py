import unittest
import production

class TestProduction(unittest.TestCase):

    def test_remove_dup(self):
        input = [1,1,2,2]
        output = [1,2]
        self.assertListEqual(output,list(production.remove_dup(input)))

if __name__ == '__main__':
    unittest.main()
