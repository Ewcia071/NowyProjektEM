import wyrazenia
import unittest

class TestWyrazenia(unittest.TestCase):

    def test_capitalize(self):
        txt = "hello, and welcome to my world."
        wynik = wyrazenia.capitalize(txt)
        self.assertEqual('Hello, and welcome to my world.',wynik)

    def test_lower(self):
        txt = "HELLO, AND WELCOME TO MY WORLD."
        wynik = wyrazenia.lower(txt)
        self.assertEqual('hello, and welcome to my world.',wynik)

    def test_upper(self):
        txt = "hello, and welcome to my world."
        wynik = wyrazenia.upper(txt)
        self.assertEqual('HELLO, AND WELCOME TO MY WORLD.',wynik)

    def test_isalpha(self):
        txt = "helloandwelcometomyworld"
        wynik = wyrazenia.isalpha(txt)
        self.assertTrue(wynik)

    def test_isdigit(self):
        txt = "1234567890"
        wynik = wyrazenia.isdigit(txt)
        self.assertTrue(wynik)

if __name__ == '__main__':
    unittest.main()



#capitalize
#lower
#upper
#isalpha
#isdigit
