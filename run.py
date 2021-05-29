#!/usr/bin/env python3.8
from credentials import Credentials
from account import Account

def create_account(account_name, user_name,password):
    '''
    function to create a new account
    '''
    new_account = Account(account_name,user_name,password)
    return new_account


def save_accounts(account):
    '''
    function to save account
    '''
    account.save_account()

def check_account_exists(user_name, password):
    '''
    Function that check if a account exists with that password and a username and return a Boolean
    '''
    return Account.account_exists(user_name,password)

def create_contact(account,username,password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(account,username,password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def delete_credential(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(username):
    '''
    Function that finds an account by username and returns the credentials
    '''
    return Credentials.find_by_username(username)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()



def main():
    print("Hello there, please enter your account name, user name and password:")  
    print("Account name:")
    account_name = input()
    print("User name:")
    user_name =input()
    print("Password:")
    password = input()

    print("Confirm password ....")
    confirm_password = input()

    while confirm_password != password:
                print("Password did not match...")
                print("password ....")
                password = input()
                print("Confirm  your password ....")
                confirm_password = input()
    else:
                save_accounts(create_account(account_name,user_name, password))
                print(f'Congratulations, New Account has been created for: {user_name} using password: ({password}).....keep it last past-pass always')
                print("proceed to login")
                print("username")
                entered_user_name = input()
                print("Your password:")
                entered_password = input()

    while entered_user_name != user_name or entered_password != password:
                print("Invalid username or password")
                print('username')
                entered_user_name = input()
                print("Your password")
                entered_password = input()
    else:                
        
                print(f'Welcome back  {entered_user_name} 😍. please choose an option to continue')


if __name__ == '__main__':
    main()    