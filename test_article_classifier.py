import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from article_classifier import Classify

import unittest


class ClassifyTests(unittest.TestCase):
    article = 'On Monday evening everybody in the world declared James Condron to something something and etc.'

    def test_new(self):
        self.assertIsNotNone(Classify(self.article))


if __name__ == '__main__':
    unittest.main()
