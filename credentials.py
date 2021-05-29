class Credentials :
  """
  Class that generates new instances for credentials.
  """

  credential_list = []

  def __init__(self,account, username,password):
    self.account = account
    self.username = username
    self.password = password

  def save_credentials(self):
    """
    method saves credentials object into credential_list
    """

    Credentials.credential_list.append(self)