from datetime import datetime
from math import floor
from os import environ

def save_data(last_read: datetime, money: str, next_update: datetime) -> None:
    filename = environ["DB_FILE"]

    parsed_last_read = str(floor(last_read.timestamp()))
    parsed_next_update = str(floor(next_update.timestamp()))

    with open(filename, "w") as file:
        file.write(money + "\n")
        file.write(parsed_last_read + "\n")
        file.write(parsed_next_update + "\n")
    