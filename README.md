# Web Authentication Auditor (webbf)

A lightweight, high-velocity Python utility designed to audit web authentication layers through automated credential testing. This tool is built to deconstruct the mechanics of HTTP POST requests, session handling, and differential response analysis.

## Technical Overview
`webbf` is an offensive security tool that automates the process of identifying valid credentials on web login forms. Unlike basic scripts that rely solely on HTTP status codes, this tool performs a baseline measurement of the target application to identify successful logins through **Response Size Deviation**.

This approach is particularly effective against modern web applications that return a generic "200 OK" status for both successful and failed authentication attempts.



## Key Features
- **Multi-User Auditing:** Supports comma-separated username lists to perform targeted credential stuffing or multi-account testing in a single execution.
- **Response Size Filtering:** Establishes a baseline "failure size" and monitors for anomalies (deltas) in return content length to detect successful logins.
- **Real-time Progress Monitoring:** Utilizes `sys.stdout` buffer flushing to provide live updates of the current `user:password` attempt without polluting the terminal history.
- **Input Sanitization:** Automatically strips and encodes wordlist entries to ensure compatibility with diverse web server environments.

## How it Works
The tool follows a four-stage execution pipeline:

1. **Baseline Creation:** The script sends a known-invalid request to the target URL to measure the standard "Login Failed" response size.
2. **Wordlist Ingestion:** It parses a user-provided password file, handling newline characters and encoding the data for transmission.
3. **Automated Iteration:** It loops through the provided username list, testing each password against the target endpoint via HTTP POST requests.
4. **Differential Analysis:** The script calculates the absolute difference between the current response size and the baseline. A significant deviation (default > 20 bytes) triggers a success notification.

## Usage
1. **Clone the repo:**
   ```bash
   git clone https://github.com/shibasis-ls/webbf.git
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
