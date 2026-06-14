import psutil

def get_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return float(f.read()) / 1000
    except:
        return "N/A"

def start():
    print("Raspberry Pi Performance Monitor")
    print("Press Ctrl+C to stop\n")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            temp = get_temp()
            print(f"CPU: {cpu:5.1f}% | RAM: {ram:5.1f}% | TEMP: {temp}°C")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")