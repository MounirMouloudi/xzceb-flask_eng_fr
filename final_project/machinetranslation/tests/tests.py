import unittest
from translator import english_to_french, french_to_english


class TestEnToFr(unittest.TestCase):
    def testWords(self):
        self.assertEqual(english_to_french('Good'), 'Bonne')
        self.assertEqual(english_to_french('Man'), 'Homme')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrToEn(unittest.TestCase):
    def testWords(self):
        self.assertEqual(french_to_english('Bonne'), 'Good')
        self.assertEqual(french_to_english('Homme'), 'Man')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()
