![WRAITH Banner](A_banner_for_a_project_named_WRAITH_is_displayed_i.png)

# WRAITH  
**Wireless Reconnaissance & Autonomous Interdiction Terminal Hub**

---

### 📡 Overview

**WRAITH** is a research-oriented, field-deployable tool designed to **highlight risks associated with unencrypted UAV telemetry links** that use the MAVLink protocol. It passively monitors for MAVLink heartbeat messages and, upon detection, can autonomously execute predefined scripts for simulation or training purposes in explicitly authorized environments.

WRAITH was developed to support ethical security research, red team training, and system hardening exercises where telemetry encryption is absent or weak. It does not interact with encrypted traffic, does not perform denial-of-service attacks, and does not target commercial systems.

---

### 🧰 Core Features

- Passive MAVLink heartbeat detection
- Autonomous payload scripting (via Python)
- Real-time .log file creation for event tracking
- Headless operation with systemd auto-start
- Discord webhook integration for push alerts
- Runs within Python virtual environment for isolation

---

### 🗂️ Project Structure

```
~/mav_env/              # Python virtual environment
~/mav_hunter/
├── px4_attack_cli.py   # Optional CLI payload launcher
├── hunter_listener.py  # Passive scanner + trigger engine
└── logs/               # Timestamped log output
```

---

### 🛠️ Setup Instructions

#### Requirements
- Raspberry Pi 5
- Kali Linux
- Python 3.9+
- Wi-Fi adapter (e.g., Panda PAU09, Ralink RT5572)

#### Environment Setup

```bash
mkdir -p ~/mav_hunter/logs
python3 -m venv ~/mav_env
source ~/mav_env/bin/activate
pip install pymavlink requests
```

Place your `.py` files in `~/mav_hunter/`.

---

### 🧪 Manual Run

```bash
source ~/mav_env/bin/activate
python3 ~/mav_hunter/hunter_listener.py
```

Logs are saved in `~/mav_hunter/logs/` on detection.

---

### ⚙️ Auto-Start with systemd

Create `/etc/systemd/system/mav_hunter.service`:

```ini
[Unit]
Description=WRAITH MAVLink Listener
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

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable mav_hunter.service
sudo systemctl start mav_hunter.service
```

---

### 🧪 Testing with QGroundControl

- Set up a UDP link in QGroundControl:
  - Port: 14551
  - Target: `<Your Pi IP>:14550`
- Ensure PX4-based system is transmitting telemetry
- WRAITH will log heartbeat and trigger response
- Discord notifications will be sent (if configured)

---

### 📸 Screenshots

![Virtualenv Activated](media/20250418_002425.jpg)  
![Script Running](media/20250418_002505.jpg)  
![Payloads Executing](media/20250418_002538.jpg)

---

### 🚧 Future Upgrades

- Target filtering (system ID/firmware type)
- Configurable payload delays and conditions
- Optional Slack/Mattermost integrations
- Expanded GPS spoof testing (in simulation only)

---

### ⚠️ Legal + Ethical Disclaimer

WRAITH is intended for **authorized security research, academic training, and red team simulation** only.  
It must **never** be used to target, interfere with, or disrupt real-world systems unless you have **explicit, written permission** from the system owner.

Misuse may violate **local, state, or federal laws**, including U.S. FCC and FAA regulations.

Use responsibly. Train ethically. Document legally.

---

### 📎 Attribution

WRAITH uses [pymavlink](https://github.com/ArduPilot/pymavlink), developed by the ArduPilot and Dronecode communities.  
This project is not affiliated with or endorsed by PX4, Dronecode, ArduPilot, or any other organization.

Linux OS provided by [Kali Linux](https://www.kali.org/).  
Created and maintained by Ryan Schwarz.

Licensed under the [MIT License](LICENSE).
