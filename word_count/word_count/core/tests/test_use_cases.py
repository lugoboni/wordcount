from django.test import TestCase
from word_count.core.use_cases import count_words_use_case

class TestCoutWordsUseCase(TestCase):

    def setUp(self):
      self.bag_of_five_words = "uno dos tres cuatro cinco"
      self.bag_of_ten_words = "uno dos tres cuatro cinco sies siete ocho nueve diez"
      self.bag_of_mess = "1          2, 4"
      self.bag_of_mix = "@ , 10, 2"
      self.bag_of_garbage = "^ { ]"
      
    def test_string_variation_success(self):

        self.assertEqual(count_words_use_case(self.bag_of_five_words), 5)
        self.assertEqual(count_words_use_case(self.bag_of_ten_words), 10)
        self.assertEqual(count_words_use_case(self.bag_of_mess), 3)
        self.assertEqual(count_words_use_case(self.bag_of_mix), 3)
        self.assertEqual(count_words_use_case(self.bag_of_garbage), 0)