#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "[-] Error: Missing arguments!"
    echo "Usage: $0 <Target IP> <NSE Script Name>"
    echo "Example: $0 127.0.0.1 banner"
    exit 1
fi

TARGET=$1
SCRIPT_NAME=$2

echo "[+] Starting Nmap scan on target: $TARGET"
echo "[+] Using NSE script: $SCRIPT_NAME"
echo "----------------------------------------"

nmap --script "$SCRIPT_NAME" "$TARGET"

echo "----------------------------------------"
echo "[+] Scan completed successfully."