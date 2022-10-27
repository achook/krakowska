from os import environ

import sentry_sdk as sentry

sentry_url = environ["SENTRY_URL"]
sentry.init(
    sentry_url,
    traces_sample_rate=1.0
)

print("Sentry is set up")

from time import sleep
from datetime import datetime

from api import get_money
from db import save_data


print("Executing...")

money = get_money()

if money is not None:
    now = datetime.now()
    save_data(now, money)

print("Exiting...")