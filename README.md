
# Linux System Monitoring & Automation Dashboard

## Installation
```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
```

## Run Monitoring Script
```bash
python3 monitor.py
```

## Run Dashboard
```bash
python3 app.py
```

## Automate with Cron
```bash
crontab -e
# Add line to run every 5 minutes
*/5 * * * * /usr/bin/python3 /path/to/monitor.py
```
