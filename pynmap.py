import nmap
import sys

def nmap_port_scanner():
    # Instantiate the PortScanner object
    scanner = nmap.PortScanner()
    
    # Get user input for target and ports
    target = input("Enter the target IP address: ")
    port = input("Enter the port or port range (e.g., 80 or 22-443): ")
    
    print(f"\n[+] Scanning {target} on port(s) {port} using Nmap...")
    
    try:
        # Perform the scan
        scanner.scan(target, port)
        
        # Check if the host is up
        if target in scanner.all_hosts():
            print(f"Host Status: {scanner[target].state()}")
            
            # Check if TCP protocol was scanned
            if 'tcp' in scanner[target]:
                ports = scanner[target]['tcp'].keys()
                for p in ports:
                    state = scanner[target]['tcp'][p]['state']
                    print(f"Port {p} is {state}")
        else:
            print("[-] Host appears to be down or unresponsive.")
            
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    nmap_port_scanner()