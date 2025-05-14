
import time
import os
import subprocess
from pymavlink import mavutil
from datetime import datetime

BASE_DIR = os.path.expanduser("~/mav_hunter")
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOG_DIR, f"event_{timestamp}.log")
    with open(log_file, "w") as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    print("[*] Starting WRAITH MAVLink Listener...")
    master = mavutil.mavlink_connection('udp:0.0.0.0:14550', timeout=10)
    
    while True:
        try:
            hb = master.recv_match(type='HEARTBEAT', blocking=True, timeout=30)
            if hb:
                msg = f"Heartbeat detected: System ID {hb.get_srcSystem()}, Component ID {hb.get_srcComponent()}"
                print(f"[+] {msg}")
                log_event(msg)

                # Simulate payload execution
                print("[+] Executing payloads (dry-run)...")
                log_event("Simulated payload execution: reboot + GPS spoof")
                # subprocess.call(["python3", os.path.join(BASE_DIR, "mavlink_payload_cli.py")])

                time.sleep(5)
        except Exception as e:
            print(f"[!] Error: {e}")
            log_event(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
