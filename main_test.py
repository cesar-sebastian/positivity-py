import unittest
from main import Positivity


class PositivityTest(unittest.TestCase):
  
  def test_cast_to_lower(self):
    p = Positivity()
    self.assertEqual(p.cast_to_lower('Hola'), 'hola')

  def test_cast_to_lower_error(self):
    p = Positivity()
    self.assertRaises(AttributeError, p.cast_to_lower, 55)
  
  def test_clear_text(self):
    p = Positivity()
    self.assertEqual(p.clear_text('Holá,.'), 'Hola')

  def test_split_text(self):
    p = Positivity()
    self.assertEqual(p.split_text('Hola como  estan'), ['Hola', 'como', '', 'estan'])

  def test_compute_A(self):
    p = Positivity()
    self.assertEqual(p.compute('Esto esta fantástico . , - * a veces estuvo detestable fantastico', {'fantastico': 10, 'detestable': -10 }), 1.25)
  
  def test_compute_B(self):
    p = Positivity()
    self.assertEqual(p.compute('El dia esta Fantástico', {'fantastico': 8, 'detestable': -3 }), 2.0)

unittest.main()