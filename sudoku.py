# This code requires an 81 character string with 0 representing blank spaces, right to left, top to bottom
# run with "python sudoku.py 81-character-string"

import sys

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)

def r(a):
  i = a.find('0')
  if i == -1:
    sys.exit(a)

  excluded_numbers = set()
  for j in range(81):
    if same_row(i,j) or same_col(i,j) or same_block(i,j):
      excluded_numbers.add(a[j])

  for m in '123456789':
    if m not in excluded_numbers:
      r(a[:i]+m+a[i+1:])

if __name__ == '__main__':
  if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
    r(sys.argv[1])
  else:
    print 'Usage: python sudoku.py puzzle'
    print '  where puzzle is an 81 character string 
             representing the sudoku read left-to-right
             top-to-bottom with 0 being the blank spaces'
