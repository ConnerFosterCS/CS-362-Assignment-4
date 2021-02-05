# Connner Foster (932777502)
# cs362 section 001
# Code to create a full name from first and last name input
import unittest  

def makeName(firstName, lastName):
  if firstName.isalpha() and lastName.isalpha():
    fullName = str(firstName) + " " + str(lastName)
    return fullName
  else:
    return "Input must only be letters"

a = "test"

class TestCase(unittest.TestCase):
  #Case 1 (pass and fail)
  def test1(self): self.assertEqual(makeName("Conner","Foster"),"Conner Foster")
  def test2(self): self.assertEqual(makeName(" Conner "," Foster "),"Conner Foster")

  #Case 2 (pass and fail)
  def test3(self): self.assertEqual(makeName("One","Two"),"One Two")
  def test4(self): self.assertEqual(makeName(1, " "),"1 ")

  #Case 3 (pass and fail)
  def test5(self): self.assertEqual(makeName("testing","symbols"),"testing symbols")
  def test6(self): self.assertEqual(makeName("$", "@"),"$ @")


if __name__ == '__main__':
  unittest.main()