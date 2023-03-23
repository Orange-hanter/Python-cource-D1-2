import unittest
from Module5.Car import *

class Dummy:
    ...    

class TestCars(unittest.TestCase):

    def test_car_add_excavator(self):
        self.assertEqual(Car(10) + Excavator(20), 30)
        
    def test_car_add_Dummy(self):
        with self.assertRaises(TypeError):
            Car(10) + Dummy()
            
    def test_car_add_int(self):
        self.assertEqual(Car(10) + 20, 30)
        self.assertEqual(Car(10) + 0, 10)
        
    def test_type_error_float(self):
        with self.assertRaises(TypeError):
            Car(10) + 55.55

    def test_type_wrang_call(self):
        with self.assertRaises(TypeError):
            111 + Car(10)
        with self.assertRaises(TypeError):
            Excavator(20) + Car(10)


if __name__ == '__main__':
    unittest.main()