# Connner Foster (932777502)
# cs362 section 001
# Code to find the volume of a cube
import unittest  

def volume(x, y, z):
  return x * y * z

a = "test"

class TestCase(unittest.TestCase):
  #Case 1 (pass and fail)
  def test1(self): self.assertEqual(volume(2,2,2),8)
  def test2(self): self.assertEqual(volume(2,2,2),7)

  #Case 2 (pass and fail)
  def test3(self): self.assertEqual(volume(-2,2,2),-8)
  def test4(self): self.assertEqual(volume(-2,2,2),8)

  #Case 3 (pass and fail)
  def test5(self): self.assertEqual(volume(a,1,1),"test")
  def test6(self): self.assertEqual(volume(a,2,2),8)



if __name__ == '__main__':
  unittest.main()