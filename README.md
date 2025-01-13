## Features
- Multi-user brute-forcing: Test multiple usernames against a target.
- Supports custom password wordlists.
- Lightweight and easy-to-use design.
- Real-time attempt tracking for better visibility.


### **Usage**:
```bash
python3 brute_force_tool.py <target_url> <usernames> <passwords_file> <needle> [--delay <seconds>]
```

Where:
- `<target_url>`: The URL of the login page (For example: `http://example.com/login`).
- `<usernames>`: A comma-separated list of usernames (For example: `admin,user,guest`).
- `<passwords_file>`: The path to the file containing passwords to attempt (For example: `passwords.txt`).
- `<needle>`: A string in the response page that indicates a successful login (For example: `Welcome back`).
- `--delay <seconds>` (Optional): The delay between requests to avoid overwhelming the server (For example: `--delay 1` for a 1-second delay).

### **Example**:
```bash
python3 brute_force_tool.py http://example.com/login admin,user,guest passwords.txt "Welcome back" --delay 2
```
