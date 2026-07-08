import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
    except Exception:
        pass

def main():
    target = input("Enter target IP or hostname (e.g., localhost): ").strip()
    if not target:
        target = "localhost"
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Could not resolve hostname {target}")
        return

    print(f"\nStarting scan on target: {target_ip}")
    print("Scanning ports 1 to 1024...")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, 1025):
            executor.submit(scan_port, target_ip, port)

    print("Scan complete.")

if __name__ == "__main__":
    main()
