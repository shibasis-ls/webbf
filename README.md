# Python Web Login Brute Forcer

A conceptual Python tool designed to automate login attempts against web forms using a dictionary attack approach. This project demonstrates how HTTP requests can be automated and how response analysis (specifically response length) can be used to infer valid credentials without relying on specific error messages.

## Technical Overview

This script interacts with a target web application by sending HTTP `POST` requests. Unlike tools that look for specific strings (e.g., "Incorrect password"), this tool uses **Response Size Analysis**.

It first establishes a "baseline" for a failed login by sending a known incorrect credential set. It then compares the size (in bytes) of subsequent responses against this baseline. A significant deviation in response size suggests a change in the server's behavior, often indicating a successful login or a different state (like a redirection or 2FA prompt).

## Key Features

* **Response Length Heuristics:** Detects successful logins by analyzing the `Content-Length` of the HTTP response rather than parsing HTML text.
* **Multi-User Support:** Accepts a list of usernames to iterate through, allowing for credential stuffing tests.
* **Real-Time Feedback:** uses `sys.stdout` to print the current attempt without flooding the terminal with new lines.
* **Automated Baseline:** Automatically calculates the size of a failed login request before starting the attack.

## Prerequisites

* Python 3.x
* `requests` library

### Installation

Install the required library:

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
