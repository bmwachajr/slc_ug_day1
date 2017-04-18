"""
The sieve of Eratosthenes >>

Input: an integer n > 1.
 
 Let A be an array of Boolean values, indexed by integers 2 to n,
 initially all set to true.
 
 for i = 2, 3, 4, ..., not exceeding vn:
   if A[i] is true:
     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n:
       A[j] := false.
 
 Output: all i such that A[i] is true.
 
"""

def function(arg):
  if type(arg) != int:
    raise TypeError('Argument must be interger')
  elif arg < 0:
    raise ValueError('Argument must be positive interger')
  else:
    if arg > 1:
      prime_list = [2]
      for i in range(arg):
        j = 2
        while j < i:
          if (i % j == 0): 
            break
          if(i == j+1):
            prime_list.append(i)
          j += 1
    else:
      prime_list = []
      return prime_list
  return prime_list