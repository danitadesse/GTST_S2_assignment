import socket
import sys

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")

        s.close()
    except KeyboardInterrupt:
        print("\nExiting script.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nCould not connect to server.")
        sys.exit()
if __name__ == "__main__":
    target = "127.0.0.1"
    port_to_check = 8080

    print(f"Scanning {target} on port {port_to_check}...")
    scan_port(target, port_to_check)