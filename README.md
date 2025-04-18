# SkyReaper
Autonomous MAVLink Drone Interdiction System

**SkyReaper** is a Raspberry Pi 5–powered autonomous MAVLink hunter-killer platform. It passively listens for drone telemetry and command traffic (MAVLink protocol), then triggers payloads on detection—executing GPS spoofing, mode spamming, and forced reboot injections against PX4-based flight controllers.

![SkyReaper Running in Terminal](../media/20250418_002425.jpg)
![Script Execution Start](../media/20250418_002505.jpg)
![Payload Trigger in Action](../media/20250418_002538.jpg)
![PX4 Comm Link Setup in QGC](../media/20250418_002559.jpg)
![MAVLink Packet Flow Confirmed](../media/20250418_002559.jpg)

---

## 🚀 Features
- Passive MAVLink heartbeat detection
- CLI-based attack engine (`px4_attack_cli.py`)
- GPS spoofing, reboot, and mode-spam payloads
- Logs all detections with timestamped `.log` files
- Fully headless operation
- Persistent `systemd` automation
- Runs in isolated Python virtual environment

---

## 🧱 Project Structure
```
/home/kali/
├── mav_env/                  # Python virtual environment (pymavlink lives here)
├── mav_hunter/
│   ├── px4_attack_cli.py     # Aggressive MAVLink payload script
│   ├── hunter_listener.py    # Passive detector + payload launcher
│   └── logs/                 # Logs each event & payload outcome
```

---

## 🔧 Setup Instructions

### 1. Create Directories
```bash
mkdir -p ~/mav_hunter/logs
```

### 2. Create Python Virtual Environment
```bash
python3 -m venv ~/mav_env
source ~/mav_env/bin/activate
pip install pymavlink
```

### 3. Drop Scripts
Save `px4_attack_cli.py` and `hunter_listener.py` in `~/mav_hunter/`

### 4. Manual Test Run
```bash
source ~/mav_env/bin/activate
python3 ~/mav_hunter/hunter_listener.py
```
Watch for:
- Heartbeat detection
- Payload execution
- New log file in `~/mav_hunter/logs/`

---

## 🤖 Automation (Auto-Start on Boot)

### 1. Create systemd Service
```bash
sudo nano /etc/systemd/system/mav_hunter.service
```
Paste:
```ini
[Unit]
Description=SkyReaper MAVLink Listener
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=kali
WorkingDirectory=/home/kali/mav_hunter
ExecStart=/home/kali/mav_env/bin/python3 /home/kali/mav_hunter/hunter_listener.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 2. Enable Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable mav_hunter.service
sudo systemctl start mav_hunter.service
```

### 3. Reboot Test
```bash
sudo reboot
```
Your Pi is now a self-starting SkyReaper node.

---

## 🧪 Testing With QGroundControl
- Setup a UDP link in QGC:
  - **Port:** `14551` (QGC)
  - **Server address:** `<Pi_IP>:14550`
- Start QGC *after* the drone/flight controller is live
- QGC will forward MAVLink heartbeats to the Pi
- SkyReaper logs and executes automatically

---

## 📸 Documentation
### 📷 Screenshots
1. Virtualenv activated on Pi: `20250418_002425.jpg`
2. Listener script launched: `20250418_002505.jpg`
3. Payloads running: `20250418_002538.jpg`
4. QGC link config: `20250418_002559.jpg`
5. MAVLink flow confirmed: `20250418_002559.jpg`

### 🎥 Execution Video
**Filename:** `20250418_002606.mp4`
**Content:** QGroundControl linking → MAVLink traffic sent → SkyReaper logs and attacks

---

## 💀 Naming
**SkyReaper** was chosen for:
- Tactical tone
- Stickiness
- Immediate relevance to drone interdiction

Other upcoming builds:
- **WRAITH** – Silent interdiction, filtered payloads
- **DRONEEATER** – Maximalist payload flooder
- **BlackICARUS** – Spoof-based navigation disruptor
- **VULTURE** – Tracker/logging-only recon node

---

## 🛡️ Future Upgrades
- Add webhook alerts (Discord, Slack)
- Target filtering (e.g., only PX4, only > System ID 0)
- Dynamic GPS spoofing / waypoint injection
- Radio & LTE traffic mirroring

---

## ⚠️ Disclaimer
SkyReaper is built for testing, educational, and authorized red team operations **only**. Unauthorized use against civilian or commercial drones is a federal offense under FCC/FAA regulations.

Stay ethical. Train smart. Fly safe.

---

**Developed by:** Ryan Schwarz
**Build Date:** April 18, 2025
**System:** Raspberry Pi 5 (Kali Linux)
**Mission Role:** Autonomous Drone Defense Node
