from django.test import TestCase

# Create your tests here.

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_false_is_false(self):
        self.assertFalse(True)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 5)

