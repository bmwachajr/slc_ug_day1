import unittest
from unittest import TestCase

class functionTestCases(TestCase):
  def test_returns_correct_list(self):
    arg = 10
    result = function(arg)
    self.assertEqual(result, [2,3,5,7], msg='Expected {}, got {}'.format([2,3,5,7], result))
    
  def test_1_returns_empty_list(self):
    arg = 1
    result = function(arg)
    self.assertEqual(result, [], msg='Expected {}, got {}'.format([], result))

  def test_non_integer_argument(self):
    with self.assertRaises(ValueError) as context:
      arg = -10
      result = function(arg)
      self.assertEqual(
        'Argument must be positive interger',
        context.exception.message,
        'Only positive integers are allowed as input'
      )
  
  def test_non_integer_argument(self):
    with self.assertRaises(TypeError) as context:
      arg = 'arg'
      result = function(arg)
      self.assertEqual(
        'Argument must be interger',
        context.exception.message,
        'Only integers are allowed as input'
      )