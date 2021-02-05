# Connner Foster (932777502)
# cs362 section 001
# Code to calculate the average of a list
import unittest  

def sumList(my_list, n):
  if n == 0:
    return sum(my_list)
  else:
    return sum(my_list) / n

a = "test"

class TestCase(unittest.TestCase):
  #Case 1 (pass and fail)
  def test1(self): self.assertEqual(sumList([1, 2, 3, 4, 5],5),3)
  def test2(self): self.assertEqual(sumList([1, 2, 3, 4, 5],6),4)

  #Case 2 (pass and fail)
  def test3(self): self.assertEqual(sumList([-1, 2, -3, 4, -5],5),-0.6)
  def test4(self): self.assertEqual(sumList([-1, 2, -3, 4, -5],0),3)

  #Case 3 (pass and fail)
  def test5(self): self.assertEqual(sumList([1.5, 2.5, 3.5, 4.5, 5.5],5),3.5)
  def test6(self): self.assertEqual(sumList([],5),3)

if __name__ == '__main__':
  unittest.main()