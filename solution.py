"""
At least 5 test cases defined in your public Github repo for the function you are to code

A working function to generate prime numbers from 0 to n with asymptotic analysis in your public Github repo

At least 5 commits on your public Github repo

"""

"""
Input: an integer n > 1.
 
 Let A be an array of Boolean values, indexed by integers 2 to n,
 initially all set to true.
 
 for i = 2, 3, 4, ..., not exceeding vn:
   if A[i] is true:
     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
       A[j] := false.
 
 Output: all i such that A[i] is true.
 
"""
import unittest
from unittest import TestCase

class functionTestCases(TestCase):
  def test_returns_correct_list(self):
    arg = 10
    result = function(arg)
    self.assertEqual(result, [2,3,5,7], msg='Expected {}, got {}'.format([2,3,5,7], result))
    
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

def function(arg):
  if arg < 0:
    raise ValueError('Argument must be positive interger')
  elif isinstance(arg, int):
    prime_list = [2]
    if arg > 1:
      i = 2
      while i < arg:
        j = 2
        while j < i:
          if (i % j == 0): 
            break
          if(i == j+1):
            prime_list.append(i)
          j += 1
        i += 1
      print (prime_list)
  else:
    raise TypeError('Argument must be interger')
  
  return prime_list
  
if __name__ == '__main__':
  unittest.main()