from django.test import TestCase

from word_count.core.forms import WordCountForm

class TestWordCountForm(TestCase):
    def setUp(self):

        self.bag_of_five_words = "uno dos tes cuatro cinco"
        self.bag_of_ten_words = "uno dos tes cuatro cinco sies siete ocho nueve diez"

    def test_clean_username(self):
        # A user with proto_user params does not exist yet.


        form = WordCountForm(
            {
                "words": self.bag_of_five_words,
             }
        )

        assert form.is_valid()
