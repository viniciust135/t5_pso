from django.test import TestCase

# Create your tests here.

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData")
        pass

    def setUp(self):
        print("setUp")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse(False)

    def test_one_plus_one_equals_two(self):
        print("Teste 1+1=2")
        self.assertEqual(1 + 1, 2)

