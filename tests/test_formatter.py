import unittest

from app.utils.formatter import format_average


class TestFormatAverage(unittest.TestCase):
    def test_formats_value_with_two_decimal_places(self):
        self.assertEqual(format_average(4.4), "Средний результат: 4.40")


if __name__ == "__main__":
    unittest.main()
