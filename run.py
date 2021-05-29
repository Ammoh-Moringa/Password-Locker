#!/usr/bin/env python3.8
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


def main():
    print("Hello there, please enter your account name, user name and password:")  
    print("Account name:")
    account_name = input()
    print("User name:")
    user_name =input()
    print("Password:")
    password = input()


if __name__ == '__main__':
    main()    