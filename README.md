# raspberry-pi-monitor
A simple Raspberry Pi performance monitor. Very helpful for constant monitoring when testing something

## Installation

A Python package for real-time Raspberry Pi performance monitoring (CPU, RAM, Temperature).

## Installation

### On Raspberry Pi (Recommended)
pip install raspberry_pi_monitor --break-system-packages

### On other systems
pip install raspberry_pi_monitor

## Usage
import pi_monitor
pi_monitor.start()

Note: This package displays CPU, RAM and Temperature 
## Output
Raspberry Pi Performance Monitor

Press Ctrl+C to stop
CPU:  12.5% | RAM:  45.2% | TEMP: 52.3°C
CPU:   8.1% | RAM:  45.3% | TEMP: 52.1°C

## Stopping the monitor
Press Ctrl+C — it will safely stop and print "Monitoring stopped."

## Works on
- Raspberry Pi Zero
- Raspberry Pi 3
- Raspberry Pi 4
- Raspberry Pi 5
- Any Raspberry Pi model running Raspberry Pi OS

## Troubleshooting

### "externally-managed-environment" error
You're on a newer Pi OS (Bookworm or above). Use:
pip install raspberry_pi_monitor --break-system-packages

### "pip: command not found"
Run:
sudo apt install python3-pip
Then try installing again.

### "ModuleNotFoundError: No module named 'pi_monitor'"
The package didn't install correctly. Try:
pip install raspberry_pi_monitor --break-system-packages --force-reinstall

### Temperature shows N/A
This is normal on Windows and non-Pi Linux systems.
Temperature only works on Raspberry Pi OS where the thermal sensor file exists.

### "ModuleNotFoundError: No module named 'psutil'"
psutil is a dependency and should install automatically.
If it doesn't, install it manually:
pip install psutil --break-system-packages

### Permission error during install
Try adding sudo:
sudo pip install raspberry_pi_monitor --break-system-packages

### Package installs but import fails
Make sure you're using Python 3.6 or above:
python3 --version
If below 3.6, update Python:
sudo apt update && sudo apt upgrade python3

### CPU shows 0.0% on first reading
This is normal — psutil needs 1 second to measure CPU accurately.
It will show correct values from the second line onwards.

## Requirements
- Python 3.6 or above
- Raspberry Pi OS (for temperature monitoring)
- psutil (auto-installed)

## License
MIT License
