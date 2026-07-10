import time

from simulator import get_speed
from simulator import get_rpm

from src.logger import save_log

from src.analyzer import check_speed
from src.analyzer import check_rpm

print("Car Telemetry System Started\n")

while True:

    speed = get_speed()
    rpm = get_rpm()

    print(f"Speed: {speed} km/h")
    print(f"RPM: {rpm}")

    check_speed(speed)
    check_rpm(rpm)

    save_log(speed, rpm)

    print()

    time.sleep(2)