
import argparse
from pymavlink import mavutil

def spoof_gps(master):
    print("[DRY-RUN] Would send spoofed GPS signal...")

def reboot_px4(master):
    print("[DRY-RUN] Would send reboot command...")

def mode_spam(master):
    print("[DRY-RUN] Would send mode spam...")

def main():
    parser = argparse.ArgumentParser(description="MAVLink Payload CLI")
    parser.add_argument("--reboot", action="store_true", help="Send reboot command")
    parser.add_argument("--spoof", action="store_true", help="Send spoofed GPS")
    parser.add_argument("--spam", action="store_true", help="Send mode spam")
    parser.add_argument("--dry-run", action="store_true", help="Simulate payloads without sending")
    args = parser.parse_args()

    if args.dry_run:
        print("[SIMULATION MODE] No packets will be transmitted.")
    else:
        master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

    if args.reboot:
        reboot_px4(master if not args.dry_run else None)
    if args.spoof:
        spoof_gps(master if not args.dry_run else None)
    if args.spam:
        mode_spam(master if not args.dry_run else None)

if __name__ == "__main__":
    main()
