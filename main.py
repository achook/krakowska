from os import environ
from datetime import datetime

import sentry_sdk as sentry

from api import get_money
from db import save_data


sentry_url = environ["SENTRY_URL"]
sentry.init(
    sentry_url,
    traces_sample_rate=1.0
)

print("Sentry is set up")

print("Executing...")

money = get_money()
now = datetime.now()
save_data(now, money)

print("Exiting...")
