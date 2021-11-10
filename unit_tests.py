import unittest
from joke import Joke


class Test_book_methods(unittest.TestCase):

    def test_add_new_joke(self):
        self.assertEqual(Joke.add_new_joke('Knock knock', 'Who is there?'), 'Joke has been added succesfully')

    def test_joke_count(self):
        self.assertEqual(Joke.joke_count(), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
