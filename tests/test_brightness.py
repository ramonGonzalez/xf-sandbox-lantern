import unittest

from lantern.brightness import display_lumens


class DisplayLumensTests(unittest.TestCase):
    def test_zero_stays_zero(self):
        self.assertEqual(display_lumens(0), 0)

    def test_rounds_down_to_ten(self):
        self.assertEqual(display_lumens(47), 40)

    def test_fifteen_rounds_down_to_ten(self):
        self.assertEqual(display_lumens(15), 10)

    def test_nineteen_rounds_down_to_ten(self):
        self.assertEqual(display_lumens(19), 10)

    def test_exact_multiple_is_unchanged(self):
        self.assertEqual(display_lumens(20), 20)

    def test_thirty_five_rounds_down_to_thirty(self):
        self.assertEqual(display_lumens(35), 30)

    def test_ninety_nine_rounds_down_to_ninety(self):
        self.assertEqual(display_lumens(99), 90)


if __name__ == "__main__":
    unittest.main()
