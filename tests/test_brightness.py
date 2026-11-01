import unittest

from lantern.brightness import display_lumens


class DisplayLumensTests(unittest.TestCase):
    def test_zero_stays_zero(self):
        self.assertEqual(display_lumens(0), 0)

    def test_rounds_down_to_ten(self):
        self.assertEqual(display_lumens(47), 40)


if __name__ == "__main__":
    unittest.main()
