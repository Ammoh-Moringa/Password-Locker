import unittest
from credentials import Credentials #import credentials class



class TestCredentials(unittest.TestCase):
  """
    Test class that defines test credential behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  """

  def setUp(self):
      """
      method runs before other test
      """

      self.new_credentials = Credentials("facebook", "Ammoh", "Ammoh76")

  def test_init(self):
      """
      test_init to test if the object is initialized properly
      """

      self.assertEqual(self.new_credentials.account,"facebook")
      self.assertEqual(self.new_credentials.username,"Ammoh")
      self.assertEqual(self.new_credentials.password,"Ammoh76")

if __name__ == '__main__':
    unittest.main()    