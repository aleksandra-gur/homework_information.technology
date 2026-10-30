import unittest

from app.services.calculater import calculate_average


class TestCalculateAverage(unittest.TestCase):
    def test_calculates_average(self):
        self.assertEqual(calculate_average([5, 4, 5, 3, 5]), 4.4)

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_average([])


if __name__ == "__main__":
    unittest.main()
