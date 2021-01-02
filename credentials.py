# Our requirement for wrapper is that- we assume that one one set of credentials is saved for the given service.
# Neither of the username or password should be given while retriving credentials.
# we should be able to retrive credentials only using service name.

# this will be very basic. we will not try to catch any error thrown.

# %%
import keyring


def save_cred():
    service_name = input("Enter service name:")
    username = input('Enter username:')
    password = input('Enter password:')

    keyring.set_password(service_name, 'username', username)
    keyring.set_password(service_name, username, password)

    print('Credentials saved successfully!')


# save_credentials()

# %%


def get_cred(service_name):

    username = keyring.get_password(service_name, 'username')
    password = keyring.get_password(service_name, username)

    return username, password


# %%
# get_credentials('python')
# %%
