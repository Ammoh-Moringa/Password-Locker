import unittest
from account import Account


class TestAccount(unittest.TestCase):

      """
      Test class that defines test cases for the account class behaviours.

        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
      """

      def setUp(self):
        """
        setUp method to run before each test case.
        """
        self.new_account = Account ("Amos", "Kiprotich", "qwerty")

      def test_init(self):
        """
        test_init test cases to test if the object is initialized properly.
        """

        self.assertEqual(self.new_account.account_name,"Amos")
        self.assertEqual(self.new_account.user_name,"Kiprotich")
        self.assertEqual(self.new_account.password,"qwerty")

if __name__ == '__main__':
    unittest.main()   
