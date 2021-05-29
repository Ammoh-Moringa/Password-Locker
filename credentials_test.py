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


  def test_save_credentials(self):
      """
      test_save_account test case to test if the account object is saved into the account account_list 
      """
      self.new_credentials.save_credentials() # saving the new credentials
      self.assertEqual(len(Credentials.credential_list),1)  





if __name__ == '__main__':
    unittest.main()    