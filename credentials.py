class Credentials :
  """
  Class that generates new instances for credentials.
  """

  credential_list = []

  def __init__(self,account, username,password):
    self.account = account
    self.username = username
    self.password = password