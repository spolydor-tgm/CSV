import unittest

from Csv import Csv


class CSVtest(unittest.TestCase):
#test
    def setUp(self):
        self.c = Csv('csv_file.csv')

    def test_load(self):
        try:
            self.c.read()
        except FileNotFoundError as e:
            self.fail("Where is the CSV-file?\n %s" % e)


if __name__ == '__main__':
    unittest.main()