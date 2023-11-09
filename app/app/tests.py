from . import calc
from django.test import SimpleTestCase

class CalcTest(SimpleTestCase):
    
    def test_add(self):
        res = calc.add(4,6)
        
        self.assertEqual(res, 10)
        