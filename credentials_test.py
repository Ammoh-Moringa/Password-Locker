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

  def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credential_list = []    



  def test_save_multiple_credentials(self):
            '''
            test_save_multiple_account to check if we can save multiple credentials
            objects to our credential_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("youtube","Amos","Ammoh96") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credential_list),2)

  def test_delete_credentials(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("youtube","Amos","Ammoh96") # account
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting an account object
            self.assertEqual(len(Credentials.credential_list),1) 

  def test_find_credentials_by_username_name(self):
        '''
        test to check if we can find an account by username and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("youtube","Amos","Ammoh96") # new account
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_username("Amos")

        self.assertEqual(found_credentials.password,test_credentials.password)  


  def test_delete_credentials(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","user","0712345678") # account
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting an account object
            self.assertEqual(len(Credentials.credential_list),1) 
  
  def test_display_all_credentials(self):
        '''
        method that returns a list of all credetianls saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)



if __name__ == '__main__':
    unittest.main()    