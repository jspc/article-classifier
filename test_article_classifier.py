import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from article_classifier import Classify

import unittest


class ClassifyTests(unittest.TestCase):
    article = 'On Monday evening everybody in the world declared James Condron to something something and etc.'
    orgs_dict = {'James Condron':'CnA'}

    def test_new(self):
        doc = Classify(self.article)

        self.assertIsNotNone(doc)


    def test_entities(self):
        self.doc = Classify(self.article, self.orgs_dict)

        expect = ["CnA"]
        got = self.doc.entities()['entities'].values.tolist()

        self.assertCountEqual(expect, got)


if __name__ == '__main__':
    unittest.main()
