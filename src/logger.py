#Salvare date
from datetime import datetime

def save_log(speed, rpm):

    with open("../log.txt", "a") as file:

        current_time = datetime.now()

        file.write(
            f"{current_time} | Speed: {speed} km/h | RPM: {rpm}\n"
        )
