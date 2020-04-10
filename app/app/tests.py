from django.test import TestCase
from app.calc import add, subtract


class CalsTests(TestCase):

    def test_add_numbers(self):
        """Test that two number added together"""

        self.assertEqual(add(3, 4), 7)

    def test_subtract_numbers(self):
        """Test that two numbers are subtract"""

        self.assertEqual(subtract(4, 3), 1)
