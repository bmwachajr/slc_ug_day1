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
def function(n):
  #create empty list
  prime_list = [2]
  if n > 1:
    i = 2
    while i < n:
      j = 2
      while j < i:
        if (i % j == 0): 
          break
        if(i == j+1):
          prime_list.append(i)
        j += 1
      i += 1
    print (prime_list)
  
n = 100
"""
tests
n must be int
n mustnt be empty
n must be > 0
"""
function(n)