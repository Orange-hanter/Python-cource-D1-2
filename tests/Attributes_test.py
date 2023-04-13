import unittest
from Module5.Attriburtes import *


class TestAttributes(unittest.TestCase):
    
    def test_get_noexist_att(self):
        u = Uber()
        self.assertEqual( u.noexist, None)
        self.assertEqual( u.hello, "Hello world")
    
    def test_set_noexist_attr(self):
        u = Uber()
        u.boris = "UwU"
        self.assertEqual(u.boris, "UwU")

    def test_set_vasia(self):
        u = Uber()
        u.vasia = "UwU"
        self.assertEqual(u.vasiapupkin, "UwU")
        with self.assertRaises(KeyError):
            u.__dict__["vasia"]

    def test_get_with_love(self):
         u = Uber()
         self.assertEqual(u.love, "love you")
            

if __name__ == '__main__':
    unittest.main()