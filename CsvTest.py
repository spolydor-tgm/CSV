import unittest

from src.CSV.Csv import Csv


class CSVtest(unittest.TestCase):
#test
    def setUp(self):
        self.c = Csv('csv_file.csv')

    def test_load(self):
         self.cc = Csv('tc.csv')
         self.cc.read()

    def test_load2(self):
        try:
            self.assertRaises(FileNotFoundError, self.c.read())
        except FileNotFoundError as e:
            self.fail("CSV-file?\n %s" % e)

    def test_load3(self):
        try:
            self.cc = Csv('tc2.csv')
            t = self.cc.read()
            txt = "1, abc\n18, ae\n19, ai\n"
            self.assertTrue(t == txt, "good job")
        except IOError as e:
            self.fail("CSV-file?\n %s" % e)

    def test_load4(self):
        try:
            self.cc = Csv('tc2.csv')
            t = self.cc.read()
            txt = "1, abc\n\n18, ae\n19, ai\n"
            self.assertFalse(t == txt, "Nice try")
        except IOError as e:
            self.fail("multipe whitespaces\n %s" % e)

    def test_load5(self):
        try:
            self.cc = Csv('tc2.csv')
            t = self.cc.read()
            txt = "1, abc\n18, ae\n19, ai\na"
            self.assertFalse(t == txt, "Nice try")
        except IOError as e:
            self.fail("too much characters\n %s" % e)



if __name__ == '__main__':
    unittest.main()