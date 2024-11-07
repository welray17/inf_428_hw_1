import unittest


def time_difference(hour1, hour2):
    difference = (hour2 - hour1)
    if difference < 0:
        difference += 24
    return difference


class TestTimeDifference(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(time_difference(23, 1), 2)
        self.assertEqual(time_difference(22, 2), 4)

    def test_positive(self):
        self.assertEqual(time_difference(1, 23), 22)
        self.assertEqual(time_difference(2, 22), 20)

    def test_same_time(self):
        self.assertEqual(time_difference(3, 3), 0)

    def test_half(self):
        self.assertEqual(time_difference(0, 12), 12)
        self.assertEqual(time_difference(12, 0), 12)


if __name__ == "__main__":
    unittest.main()
