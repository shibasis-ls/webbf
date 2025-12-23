# Web Authentication Auditor (webbf)

A Python-based utility for performing automated credential testing against web authentication forms. This tool utilizes **Response Size Analysis** to detect successful logins, making it effective against applications that return consistent HTTP 200 OK status codes for failed attempts.

## Technical Overview
Many modern web applications do not use HTTP 302 redirects or 401 Unauthorized codes to signal login failures. Instead, they serve a "Login Failed" message within a standard 200 OK response. 

`webbf` bypasses this by:
1. Sending a baseline "known-bad" request to calculate the standard failure response size.
2. Iterating through a wordlist and comparing the byte-count of each response to the baseline.
3. Flagging any response that deviates significantly from the baseline as a potential successful login.



## Key Features
- **Differential Analysis:** Detects success based on response content-length delta (>20 bytes by default).
- **Multi-User Support:** Iterates through a provided list of usernames for a single password file.
- **Real-time Terminal Output:** Uses `sys.stdout` flushing to provide a clean, live update of the current user:password combination being tested.
- **Dynamic Baseline:** Automatically calculates the failure size at runtime to adapt to the specific target environment.

## How it Works
1. **Baseline Request:** Sends `admin:admin` (or any dummy creds) to the target URL.
2. **Measurement:** Records the length of the response content.
3. **Iteration:** Loops through the username list and the provided password dictionary.
4. **Comparison:** Calculates the absolute difference between the current response size and the baseline.
5. **Success Trigger:** If the difference exceeds the defined threshold, the script identifies the match and terminates.

## Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/shibasis-ls/webbf.git](https://github.com/shibasis-ls/webbf.git)
    ```
### Installation

2. **Install the required library:**
    ```bash
    pip install requests
    ```
## How It Works
* **Input**: The user provides the target URL, a comma-separated list of usernames, and the path to a password wordlist.
* **Baseline**: The script sends a dummy request (admin:admin) to gauge the byte size of a standard "Login Failed" page.
* **Attack Loop**: It iterates through every password for the first username, then moves to the next username.
* **Heuristic Check**: For every attempt, it calculates abs(current_response_size - failure_size). If the difference is greater than 20 bytes, it treats the attempt as a success.

## Usage

Run the script interactively:
```bash
python3 brute_forcer.py
```
Prompts:

    Target URL: The endpoint where the form submits (e.g., http://target-site.com/login.php).

    Usernames: Comma-separated list (e.g., admin,root,user).

    Password File: Path to your wordlist (e.g., Documents/passwords.txt or password.txt).

## Disclaimer
*This tool is intended for educational purposes and authorized security testing (Red Teaming/Penetration Testing) only. Do not use this tool against websites or systems you do not have explicit permission to audit. The author is not responsible for any misuse or legal consequences resulting from the use of this software.*
