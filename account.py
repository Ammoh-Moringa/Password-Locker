class Account:
  """
  Class that generates new instances of account
  """

  account_list = []

  def __init__(self,account_name,user_name,password):

    self.account_name = account_name
    self.user_name = user_name
    self.password = password