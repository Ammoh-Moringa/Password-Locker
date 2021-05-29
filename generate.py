import random   
import string  
import secrets  
num = 10 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
# Print the Secure string with the combination of ascii letters and digits  
print("Your password is :"+ str(res))  
  
 